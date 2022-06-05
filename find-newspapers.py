# find-newspapers.py

# The script will read a list of IA identifiers and use that to search for newspapers in
# the Chronicling America library which were published within just a few years of the IA item
#
# The list should be a .txt file and contain one IA identifier on each line

import internetarchive, json, requests
import glob
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import pdist, squareform

listName = 'pressbook-search-list.txt' # Specify the file that contains IA identifiers
yearRange = 5 # Specify how many years after the Pressbook date we should search within
outputDirectory = 'find-newspapers-tmp/'

def findNewspapers(pressbooks):
	for item in pressbooks:
		print(f'Now searching for {item}...\n')
		for i in internetarchive.search_items('identifier:' + item).iter_as_items():
			print(i.item_metadata['metadata']['identifier'] + ' : ' + i.item_metadata['metadata']['year'])
			print(i.item_metadata['metadata']['title'] + ' : ' + i.item_metadata['metadata']['creator'])
			print(i.item_metadata['metadata']['identifier-access'])
			print('')
			download(i.item_metadata['metadata']['identifier'])
			yearOne = int(i.item_metadata['metadata']['year'])
			yearTwo = int(i.item_metadata['metadata']['year']) + yearRange
			
			print(f'Searching LOC Chronicling America for newspapers from {yearOne} to {yearTwo}')
			
			newspapers = makeQuery(formQuery(yearOne, yearTwo))
			print('Found ' + str(newspapers['totalItems']) + ' newspaper pages')
			if(newspapers['totalItems'] == 0):
				print('Skipping to next Pressbook!\n')
				break
			
			
			print('(Only working with first page of results for now)')
			
			for page in newspapers['items']:
				print(page['id'])
				# print(page['url'])
				# print(page['ocr_eng'])
				
				# write the OCR data into a .txt file
				cleanID = page['id'].replace('/','-')[1:-1] # The LOC identifiers include slashes, so we replace those to avoid problems. We also chop off the leading and trailing characters (which would just be a '/' or '-')
				filename = outputDirectory + '/' + i.item_metadata['metadata']['identifier'] + '/' + cleanID + '.txt'
				with open(filename, 'w') as f:
					try:
						f.write(page['ocr_eng'])
					except KeyError:
						print('Error saving OCR to file - [ocr_eng] does not exist')
					except:
						print('Something went wrong saving OCR to file')
						
			print('Downloaded some files to work with!')
			textSimilarity(i.item_metadata['metadata']['identifier'])
			

def textSimilarity(identifier):
	# Make a list of file names
	filenames = glob.glob(outputDirectory + '/' + identifier + '/*.txt')
	# Parse the list of file names to get a list of keys (ID numbers) for us to use later
	filekeys = [f.split('/')[-1].split('.')[0] for f in filenames]
	
	# Create a CountVectorizer instance with the parameters you need
	vectorizer = CountVectorizer(input="filename", max_features=1000, max_df=0.7)
	# Run the vectorizer on your list of filenames to create your wordcounts
	# Use the toarray() function so that SciPy will accept the results
	wordcounts = vectorizer.fit_transform(filenames).toarray()
	comparison_target = identifier + '_djvu' # SciPy expects the filekey to match the exact file name, which includes this little bit of extra
	
	# Euclidean Distances
	print("\n\nEUCLIDEAN DISTANCES\n*******************")
	euclidean_distances = pd.DataFrame(squareform(pdist(wordcounts)), index=filekeys, columns=filekeys)
	print(euclidean_distances)
	euclidean_distances.to_csv(outputDirectory + '/' + identifier + '/euclidean.csv')
	print('\n\n')
	print('TOP 5 TEXTS THAT ARE MOST SIMILAR TO ' + comparison_target + ":")
	top5_euclidean = euclidean_distances.nsmallest(6, comparison_target)[comparison_target][1:]
	print(top5_euclidean)
	print('(Lower score is more similar)')
	
	
	# Cosine Distances
	print("\n\nCOSINE DISTANCES\n***************")
	cosine_distances = pd.DataFrame(squareform(pdist(wordcounts, metric='cosine')), index=filekeys, columns=filekeys)
	print(cosine_distances)
	cosine_distances.to_csv(outputDirectory + '/' + identifier + '/cosine.csv')
	print('\n\n')
	print('TOP 5 TEXTS THAT ARE MOST SIMILAR TO ' + comparison_target + ":")
	top5_cosine = cosine_distances.nsmallest(6, comparison_target)[comparison_target][1:]
	print(top5_cosine)
	print('(Ranges from 0 - 1. Lower score is more similar)')
	print('\n\n')
	

def formQuery(yearOne, yearTwo):
	query = 'https://chroniclingamerica.loc.gov/search/pages/results?' + 'dateFilterType=yearRange' + '&date1=' + str(yearOne) + '&date2=' + str(yearTwo) + '&format=json' + '&language=eng'
	return query
	
def makeQuery(query):
	response = requests.get(query)
	text = response.text
	result = json.loads(text)
	return result
	

def importList():
	print(f'Reading Internet Archive identifiers from {listName}')
	file = open(listName, 'r')
	data = file.read()
	pressbooksList = data.split("\n")
	print('Loaded ' + str(len(pressbooksList)) + ' items as a list')
	return pressbooksList
	
def download(identifier):
	internetarchive.download(identifier, verbose=True, glob_pattern="*txt", no_directory=False, destdir=outputDirectory)

if __name__ == "__main__":
	pressbooks = importList()
	findNewspapers(pressbooks)
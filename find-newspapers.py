# find-newspapers.py

# The script will read a list of IA identifiers and use that to search for newspapers in
# the Chronicling America library which were published within just a few years of the IA item
#
# The list should be a .txt file and contain one IA identifier on each line

import internetarchive, json, requests

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
			print('(Only working with first page of results for now)')
			for page in newspapers['items']:
				print(page['id'])
				# print(page['url'])
				# print(page['ocr_eng'])
				
				# write the OCR data into a .txt file
				cleanID = page['id'].replace('/','-')[1:-1] # The LOC identifiers include slashes, so we replace those to avoid problems. We also chop off the leading and trailing characters (which would just be a '/' or '-')
				filename = outputDirectory + '/' + i.item_metadata['metadata']['identifier'] + '/' + cleanID + '.txt'
				with open(filename, 'w') as f:
					f.write(page['ocr_eng'])
			


def formQuery(yearOne, yearTwo):
	query = 'https://chroniclingamerica.loc.gov/search/pages/results?' + 'year1=' + str(yearOne) + '&year2=' + str(yearTwo) + '&format=json' + '&language=eng'
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
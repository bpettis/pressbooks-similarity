# Heavily drawing on the tutorial here: https://programminghistorian.org/en/lessons/common-similarity-measures#installation-and-setup

import glob
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import pdist, squareform


def process():
	# Make a list of filenames to process
	filenames = glob.glob("mhdl-pressbooks/*.txt")

	# Parse those filenames to get just the identifier string
	filekeys = [f.split('/')[-1].split('_djvu.')[0] for f in filenames]


	# Create a CountVectorizer instance with the parameters you need
	vectorizer = CountVectorizer(input="filename", max_features=1000, max_df=0.7)
	# Run the vectorizer on your list of filenames to create your wordcounts
	# Use the toarray() function so that SciPy will accept the results
	wordcounts = vectorizer.fit_transform(filenames).toarray()
	
	metadata = pd.read_csv("mhdl-pressbook-metadata.csv", index_col="identifier")
	
	
	# Calculate Euclidean Distance
	print("EUCLIDEAN DISTANCES")
	euclidean_distances = pd.DataFrame(squareform(pdist(wordcounts)), index=filekeys, columns=filekeys)
	print(euclidean_distances)
	print('\n\n')
	
	
	# Top texts similar to 'pressbook-black-heat_djvu'
	comparison_target = 'pressbook-black-heat'
	print('TOP 5 TEXTS THAT ARE MOST SIMILAR TO ' + comparison_target + ":")
	top5_euclidean = euclidean_distances.nsmallest(6, comparison_target)[comparison_target][1:]
	print(metadata.loc[top5_euclidean.index, ['title','creator','year']])
	print('\n**********\n')
	
	# Cosine Distances
	print("COSINE DISTANCES")
	cosine_distances = pd.DataFrame(squareform(pdist(wordcounts, metric='cosine')), index=filekeys, columns=filekeys)

	print('TOP 5 TEXTS THAT ARE MOST SIMILAR TO ' + comparison_target + ":")
	top5_cosine = cosine_distances.nsmallest(6, comparison_target)[comparison_target][1:]
	print(top5_cosine)
	print('\n\n')
	print(metadata.loc[top5_cosine.index, ['title','creator','year']])
	
if __name__ == "__main__":
	print("Cool stuff is happening, hopefully!")
	print('\n**********\n')
	process()
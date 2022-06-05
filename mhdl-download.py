# This script will search the Internet Archive collection for anything where the 'Format' field is set as pressbook
# Then, it will attempt to download the associated .txt file for each item
# These will all be saved into a directory named 'mhdl-pressbooks'
# The script will also create a CSV file with some basic metadata about each downloaded item

import internetarchive
import csv

# https://archive.org/search.php?query=collection%3A%28mediahistory%29%20AND%20Format%3A%28Pressbooks%29



def search():
	with open ('mhdl-pressbook-metadata.csv', 'w') as f:
			writer = csv.writer(f)
			row = ['identifier', 'title', 'year', 'creator', 'identifier-acces']
			writer.writerow(row)
			
	for i in internetarchive.search_items('collection:mediahistory AND Format:Pressbooks').iter_as_items():
		download(i.item_metadata['metadata']['identifier'])
		with open ('mhdl-pressbook-metadata.csv', 'a') as f:
			writer = csv.writer(f)
			row = [i.item_metadata['metadata']['identifier'], i.item_metadata['metadata']['title'], i.item_metadata['metadata']['year'], i.item_metadata['metadata']['creator'], i.item_metadata['metadata']['identifier-access']]
			writer.writerow(row)
		

def download(identifier):
	internetarchive.download(identifier, verbose=True, glob_pattern="*txt", no_directory=True, destdir="mhdl-pressbooks")


if __name__ == "__main__":
	search()
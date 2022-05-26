# Pressbook Similarity

Early exploration and experimentation with using automated text-similarity tools to assess how newspapers in the US drew upon the Pressbooks and other publicity materials shared by major movie studios.

- Newspaper data from the [Library of Congress Chronicling America]('https://chroniclingamerica.loc.gov/ocr/') collection
- Pressbooks from the [Media History Digital Library]('https://mediahistoryproject.org') collections

## Library Dependencies
Using a bunch of external python libraries. I'm trying my best to track them all in requirements.txt so that you can install everything with:

`pip install -r requirements.txt`

or possibly 

`python3 -m pip install -r requirements.txt`
(if you local Python environment is as malformed as mine is...)

## Downloading MHDL Pressbooks

The `mhdl-downlad.py` file will download items from the 'mediahistory' collection on the Internet Archive that match 'format: Pressbooks'

Currently I have it set up to only download the .txt files, and to drop them all into the 'mhdl-pressbooks' directory. 

It will also create a CSV file with some basic item metadata - this will be useful when automating similarity detection
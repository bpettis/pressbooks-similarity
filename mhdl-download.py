import internetarchive

# https://archive.org/search.php?query=collection%3A%28mediahistory%29%20AND%20Format%3A%28Pressbooks%29



def search():
	for i in internetarchive.search_items('collection:mediahistory AND Format:Pressbooks'):
		download(i['identifier'])

def download(identifier):
	internetarchive.download(identifier, verbose=True, glob_pattern="*txt", no_directory=True, destdir="mhdl-pressbooks")


if __name__ == "__main__":
	search()
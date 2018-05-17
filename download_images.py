import os.path
import urllib

DOWNLOADS_DIR = '/images/'


# For every line in the file
links=open('toy_filenames.csv','r')
for link in links:
    link = link.strip()
    name = link.rsplit('/', 1)[-1]
    filename = os.path.join('images', name)

    if not os.path.isfile(filename):
        print('Downloading: ' + filename)
        try:
            urllib.urlretrieve(link, filename)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')

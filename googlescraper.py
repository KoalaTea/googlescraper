#!/usr/bin/python3

import pprint
import code
from googleapiclient.discovery import build

def main():
	key=importkey("googlecustomsearch")
	if (key is None):
		print("no key")
		sys.exit()
	print(key)
	service = build("customsearch", "v1", developerKey=key)
	#res = service.cse().list(q='saunders', fileType="pdf", siteSearch="saunders.rit.edu", cx='011869109180613770264:mfpcqwsg38w', start=99).execute()
	res = service.cse().list(q='site:saunders.rit.edu filetype:pdf', cx='011869109180613770264:mfpcqwsg38w', filter='0', start=1).execute()
	for result in res['items']:
		print(result['link'])

def importkey(keyid):
	key=None
	myfile = open("api.keys", "r")
	for line in myfile:
		if (len(line) > len(keyid)):
			if (line[0:len(keyid)-1]==keyid):
				key = line[len(keyid)+1:]
	return key

if __name__ == '__main__':
	main()

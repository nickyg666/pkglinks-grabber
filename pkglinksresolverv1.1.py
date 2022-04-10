import json, requests
import re, base64

#using JSON instead of RSS, way easier
filename = input("What should we name the output file? \n Please include .txt if you want extension. (lookin' at you, Windows users) \n .txt file will be stored in directory you ran me from. \n make sure clipboard monitor is enabled in JDownloader2 \n and simply select all text in file and copy, \n JD2 will do the rest. \n You can resolve most confusing entries in JD2 by searching against the .txt we will generate once you type a name and press ENTER: ")

with open (filename, "w+") as file:
	file.write("\n        \n")
url = "https://www.reddit.com/r/PkgLinks/new.json?sort=newest&limit=100&after="
r = requests.get(url, headers = {'User-agent': 'Chrome'})
thejson = r.json()
for x in range(100):
	entry = thejson["data"]["children"][x]["data"]["selftext"]
	title = thejson["data"]["children"][x]["data"]["title"]
	b64only = re.findall(r'((?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==))',entry)
	btostr = str(b64only)
	bstr2byte = btostr.encode('ascii')
	decodebyte = base64.b64decode(bstr2byte)
	link = decodebyte.decode('ascii')
	with open (filename, "r+") as file:
		file.write(title)
		file.write("\n")
		file.write(entry)
		file.write("\n")
		file.write(link)
		file.write("\n")
	print(title)
	print(entry)
	print(link)

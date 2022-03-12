import feedparser, base64, re, sys

filename = input("What should we name the output file? \n Please include .txt if you want extension. (lookin' at you, Windows users) \n .txt file will be stored in directory you ran me from. \n make sure clipboard monitor is enabled in JDownloader2 \n and simply select all text in file and copy, \n JD2 will do the rest. \n You can resolve most confusing entries in JD2 by searching against the .txt we will generate once you type a name and press ENTER: ")
with open (filename, "w+") as file:
	file.write("\n        \n")
o = sys.stdout
d = feedparser.parse('https://www.reddit.com/r/PkgLinks.rss?limit=100')
for x in range(102):
	
	string_value = d.entries[x].content[0]['value']
	#print(string_value)
	totrim = "<p>(.*?)</p>"
	ready4b64 = re.search(totrim, string_value).group(1)
	b64exc = re.search(totrim,string_value).group(0)
	try:
		b64s1 = ready4b64.encode('ascii', errors='ignore')
		b64s2 = base64.b64decode(b64s1)
		string_new = b64s2.decode('ascii', errors='ignore')
	except base64.binascii.Error:#necessary
		continue
		b64s1x = b64exc.encode('ascii')
		b64s2x = base64.b64decode(b64s1x)
		string_alt = b64s2x.decode('ascii')
	with open (filename, "r+") as file:
		for line in file:
			if d.entries[x].title in line:
				break #if you find it, do nothing
			if string_new in line:
				break
		else:#or else write to file
			file.write("\n    ")
			file.write(d.entries[x].title)
			file.write("\n    ")
			file.write (string_new) 
			file.write("\n    ")
			file.write("\n    ")

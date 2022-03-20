import feedparser, base64, re, sys
import ssl, binascii

if hasattr(ssl, '_create_unverified_context'):#really don't like but works on my pc because ssl have problem this machine
    ssl._create_default_https_context = ssl._create_unverified_context
    
##Prompt and github should let you know everything you need. If not, open an issue please!

filename = input("What should we name the output file? \n Please include .txt if you want extension. (lookin' at you, Windows users) \n .txt file will be stored in directory you ran me from. \n make sure clipboard monitor is enabled in JDownloader2 \n and simply select all text in file and copy, \n JD2 will do the rest. \n You can resolve most confusing entries in JD2 by searching against the .txt we will generate once you type a name and press ENTER: ")

with open (filename, "w+") as file:
	file.write("\n        \n")
	
d = feedparser.parse('https://www.reddit.com/r/PkgLinks.rss?limit=100')

for x in range(102):#something about my for loop creates duplicate entries, but it runs on my pc now at least
	t = d.entries[x].title
	c = d.entries[x].content
	print(t)
	string_value = str(c)
	presnip = "<p>(.*?)</p>"
	snip = re.findall(presnip, string_value)
	snip0 = str(snip[0])
	snip1 = str(snip)
	try:
		b64encodestr = snip0.encode('ascii', errors='ignore')
		b64bytes = base64.b64decode(b64encodestr)
		final = b64bytes.decode('ascii', errors='ignore')
		print(final)
	except binascii.Error:
		b64encodestr = snip1.encode('ascii', errors='ignore')
		continue
	with open (filename, "r+") as file:
		for line in file:
			if d.entries[x].title in line:
				break #if you find it, do nothing, BREAK FOOL
			if final in line:
				break
			else:
				o = ++ 1
				file.write(t)
				file.write(" \n ")
				file.write(final) 
				file.write("\n ")
				file.write("\n ")
				file.write(str(o))

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
	b64_re = r'((?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==))' #if alt_snip returns no matches, try again somehow
	snip = re.findall(presnip, string_value)
	alt_snip = re.findall(b64_re, string_value)
	matches = str(snip[0])
	alt_matches = str(alt_snip[0])
	try:
		b64encodestr = matches.encode('ascii', errors='ignore')
		b64bytes = base64.b64decode(b64encodestr)
		final = b64bytes.decode('ascii', errors='ignore')
		print(final)
	except binascii.Error:
		b64encodestr = alt_matches[0].encode('ascii', errors='ignore')
		b64bytes = base64.b64decode(b64encodestr)
		final = b64bytes.decode('ascii', errors='ignore')
		print(final)
		print("An error has occured in base64 decryption")
		
	with open (filename, "r+") as file:
		for line in file:
			#file.write(t)
			file.write(" \n ")
			file.write(final)
			file.write("\n ")
			file.write("\n ")
				

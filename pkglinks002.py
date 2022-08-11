import feedparser, base64, re, sys
import ssl, binascii

if hasattr(ssl, '_create_unverified_context'):
	#really don't like but works on my pc because ssl have problem this machine
	ssl._create_default_https_context = ssl._create_unverified_context
filename = 'debug.txt'
for x in range(10):
	d = feedparser.parse('https://www.reddit.com/r/PkgLinks.rss?limit=100')
	t = d.entries[x].title
	c = d.entries[x].content
	#print(t)
	string_value = str(c)
	b64_re = r'((?:[A-Za-z0-9+/]{6,})*(?:[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==))' 
	#if alt_snip returns no matches, try again somehow
	alt_snip = re.findall(b64_re, string_value)
	print("this is the list of b64 matches: "+ str(alt_snip))
	## do a lambda for i in alt_snip if len(alt_snip[i]) > 6, clean_alt_snip=alt_snip[i]
	for i in range(len(alt_snip)):
		if len(alt_snip[i]) > 6:
			#print(alt_snip[i])
			clean_alt_snip = []
			clean_alt_snip.append(alt_snip[i])
			
			print("This is the 'cleaned' list: "+ str(clean_alt_snip))
			for a in range(len(clean_alt_snip)):
				str2encode = str(clean_alt_snip[a]) 
				b64_encoded_str = str2encode.encode('ascii', errors='ignore')
				b64bytes = base64.b64decode(b64_encoded_str)
				final = b64bytes.decode('ascii', errors='ignore')

				print(t+final)


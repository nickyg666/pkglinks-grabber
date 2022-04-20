import json, requests, re, base64
#done: manipulate json into clean lists/dict where key= list title value and value = list selftext value
#TO-DO: make new link parser, b64 conversion BEFORE write to file, take entries list, make into b64 matches object with re.findall, return to list with re.sub
#using JSON instead of RSS, way easier
filename = input("What should we name the output file? \n make sure clipboard monitor is enabled in JDownloader2 \n and simply select all text in file and copy, \n JD2 will do the rest. \n You can resolve most confusing entries in JD2 by searching against the .txt we will generate once you type a name and press ENTER: ")

with open (filename, "w+") as f:
	f.write("exists now")

b64_re = r'((?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==))'
b64_re_excess = r'(?:[A-Za-z0-9+/]{4})'
url = "https://www.reddit.com/r/PkgLinks/new.json?sort=newest&limit=100&after="
r = requests.get(url, headers = {'User-agent': 'Chrome'})
thejson = r.json()
#children is a list(0-99 are objects containing dictionaries) of dictionaries! 
children = thejson["data"]["children"]
titles_list = [children[x]['data']['title'] for x in range(len(children))] 
entries_list = [children[x]['data']['selftext'].replace('\n',' ') for x in range(len(children))]
m = matches_list = [re.findall(b64_re,entries_list[x]) for x in range(len(entries_list))]

decode = [(re.sub(b64_re, base64.b64decode(str(matches_list[x])).decode('ascii', errors='ignore'), entries_list[x])) for x in range(len(entries_list))]
print(decode)


clean_dict = dict(zip(titles_list, decode))

'''
for line in entries_list:
	stringed_list_entry = str(line)
	b64list = re.findall(r'((?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==))',stringed_list_entry)
		
clean_JSON = json.dumps(clean_dict)
b64_encoded_list = clean_JSON.encode('ascii')
decoded_list = base64.b64decode(b64_encoded_list) 
newlist = json.loads(decoded_list)
print(newlist)
'''
with open (filename, "r+") as f:

	for key, value in clean_dict.items():
		f.write('%s  :  %s\n' %(key, value,))
		

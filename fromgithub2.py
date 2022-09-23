#pylint:disable=W0621
import json, requests, re, base64
#done: manipulate json into clean lists/dict where key= list title value and value = list selftext value
#TO-DO: make new link parser, b64 conversion BEFORE write to file, take entries list, make into b64 matches object with re.findall, return to list with re.sub
#using JSON instead of RSS, way easier

filename = input("What should we name the output file? \n make sure clipboard monitor is enabled in JDownloader2 \n and simply select all text in file and copy, \n JD2 will do the rest. \n You can resolve most confusing entries in JD2 by searching against the .txt we will generate once you type a name and press ENTER: ")

b64_re = r'((?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==))'
url = "https://www.reddit.com/r/PkgLinks/new.json?sort=newest&limit=100&after="
post_id=""
r = requests.get(url+ post_id, headers = {'User-agent': 'Chrome'})
posts = r.json()
	
def getURL(url,post_id):
	r = requests.get(url+ post_id, headers = {'User-agent': 'Chrome'})
	posts = r.json()
	post_id = posts["data"]["after"]
	return post_id
	url = url + post_id
	return url
#children is a list(0-99 are objects containing dictionaries) of dictionaries! 

def decodePosts(url):
	children = posts["data"]["children"]
	titles_list = [children[x]['data']['title'] for x in range(len(children))] 
	entries_list = [children[x]['data']['selftext'].replace('\n',' ') for x in range(len(children))]
	m = matches_list = [re.findall(b64_re,entries_list[x]) for x in range(len(entries_list))]#each list in matches_list is all b64 entries in entries_list[x]

	decode = [(re.sub(b64_re, base64.b64decode(str(matches_list[x])).decode('ascii', errors='ignore'), entries_list[x])) for x in range(len(entries_list))]
	
	
	b64 = r'(?:[A-Za-z0-9+/]{40,2000})'
	m2 = [re.findall(b64,decode[x]) for x in range(len(decode))]
	print(m2)
	clean_dict = dict(zip(titles_list, decode))
	with open (filename, "w+") as f:
		for key, value in clean_dict.items():
			f.write('%s  :  %s\n' %(key, value,))
			
decodePosts(url)
getURL(url,post_id)
decodePosts(url)
#make this a loop for your own sake please do 10x
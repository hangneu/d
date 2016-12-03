def pro(title):
	file = open(title,'r')
	soup = BeautifulSoup(file)
	result = []
	for item in soup.find_all("pre"):
		for item1 in item.text.split(' '):
			result.append(item1.encode('utf8'))
	file.close()
	final = []
	for item in result:
		for item1 in item.split("\n"):
			if(item1 != ""):
				for item2 in item1.split("\t"):
					final.append(item2)
	result = []
	for item in final:
		for item1 in re.findall("\w+",item):
			result.append(item1.lower())
	return result
def index():
	al = {}
	for i in range(1,3205):
		a = '{:d}'.format(i).zfill(4)
		title = "cacm/CACM-"+str(a)+".html"
		final = pro(title)
		for item in final:
			item = str(item)
			if(item != ""):
				if item in al:
					if a in al[item]:
						al[item][a] += 1
					else:
						al[item][a] = 1
				else:
					al[item] = {}
					al[item][a] = 1
	return al
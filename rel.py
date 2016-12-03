def relevence():
	dic_num = dict()
	for i in range(1,65):
		dic_num[str(i)] = []
	file = open("cacm.rel","r")
	for item in file:
		b = item.split("\n")[0].split(" ")
		dic_num[b[0]].append(b[2].split("-")[1].zfill(4))
	return dic_num
dic = relevence()
for i in range(1,65):
	print i,dic[str(i)],len(dic[str(i)])
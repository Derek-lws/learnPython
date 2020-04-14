"""
	date:2020.04.14
	author:Derek_lws
"""
print("GOOD NIGHT!")

dic = {'lili':78,'momo':57,"huahua":34,"qiangqiang":92}#无序键值对容器
dic['heihei'] = 39
print(dic)

for key in dic:
	print(dic[key])

print(dic.keys())
print(dic.values())
print(dic.items())
print(len(dic))
#dic.clear()
del dic['lili']

for key in dic:
	print(dic[key])

l1 = ['tom,12,86','Lee,15,99','Lucy,11,39']
# print(len(l1))
file = open("H:/gitDepository/learnPython/src/record.txt","w")
for x in range(len(l1)):
	file.write(l1[x]+'\n')
file = open("H:/gitDepository/learnPython/src/record.txt","r")
content = file.readlines()
for x in range(len(content)):
	print(content[x],'')


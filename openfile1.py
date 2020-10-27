fileobj=open('datatext.txt','r',encoding='utf-8')
str=fileobj.read()
print(str)
fileobj.close()
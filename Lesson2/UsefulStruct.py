#list
list = ['one','two','three','four','five','six']
list[2] = '2'  #index is start from zero
print list
list.sort()
print list
	
#tuple
tuple = ('a','b','c')   #can't change the value in tuple
print tuple
	
#dict
dic = {'1':'one','2':'two','3':'three'}
key = '2'
if key in dic :
	print dic['1']
	dic.pop(key)
	if not (key in dic):
		print 'pop the key called ' , key
else:
	print 'there is not exist a key called ' , key

#set 
setA = set(['a','b','c','d'])   #create by a list
setB = set(['c','e','g'])
setA.add('c')
print setA
print setA | setB
print setA & setB
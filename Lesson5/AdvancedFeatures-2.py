#List Comprehensions
print list(range(1, 11))					#stardIndex to endIndex(not include endIndex)
print [x * x for x in range(1, 11)]			#A List Comprehensions
#print [x * y for x in range(1,11),range(2,12)]
print [x * x for x in range(1, 11) if x % 2 == 0 and x*x > 9]   #add some conditions
print [m + n for m in 'ABC' for n in 'XYZ']   #loop more than one 
dic = {'a':1,'b':2,'c':3,'d':4}
print [k + str(v) for k , v in dic.items()]
L1 = ['Hello', 'World', 18, 'Apple', None]
import types
print [x for x in L1 if type(x) is types.StringType]

#Generator
g = (x * x for x in range(10))
print 'create a generator'
for item in g:
	print item

def Fib(max):								#use yield to create a generator by function 
	n,a,b=0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n += 1
	return 
	
f = Fib(5);
for item in g:
	print item

#use generator to create a YangHui Triangles
def triangles(rowNum):
	before,current = [1],[1]
	for i in range(1,rowNum):
		if i > 1:
			current = []
			current.append(1)
			for j in range(1,i-1):
				current.append(before[j-1] + before[j])
			current.append(1)
			before = current
		yield current
	return 
	
for t in triangles(10):
    print(t)	
	
#Iterable   list,tuple,dict,set,str&generator
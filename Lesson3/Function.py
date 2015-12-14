print abs(-22)
print help(abs)

#type convert
print int('25')
#int('aa')
print str(525)
print hex(255)
print '0 to bool is' , bool(0)
print '"false" to bool is' , bool('false')

#define a function
def GetAreaOfCircle(radius):
	return radius * radius * 3.14159
	
def IsOverTen(number):
	if(number > 10):
		print 'number is over 10'
		pass
	else:
		print 'number is not over 10'	
def power(x,n=2):
	if(x <= 0):
		return 0;
	if(n == 1):
		return x;
	return x * power(x,n-1);
#function parameter
def sum(list):
	num = 0
	for item in list:
		num += item;
	return num;		
def printName(** dic):
	if 'name' in dic:
		print 'dic has a name =>',dic['name']
	else:
		print 'no parameter of name'
		
IsOverTen(20)
print power(5,4)
print sum([123,321,222])
printName(name='jiang',age=80)

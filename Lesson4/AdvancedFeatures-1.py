#slice
L = ['A', 'B', 'C', 'D', 'E']
print 'L[1:3] =',L[1:3]				#startIndex to before endIndex
print 'L[:3] =',L[:3]				#same as L[0:3]
print 'L[-2:-1] =',L[-2:-1]
print 'L[-2:] =',L[-2:]        

L = list(range(100))
print L[:31:5]						#startIndex   endIndex   step

#slice of tuple
T = (0,1,2,3,4,5)					
print T[0:2]

#slice of string
name = "Jhon Jiang"
print name[0:5]

#=========================================================================#

#Iteration
L = ['A', 'B', 'C', 'D', 'E']
for index,value in enumerate(L):
	print 'L[' , index ,']=' ,value
dic = {'Monday':'One','Tuesday':'Two','Wednesday':'Three','Thuesday':'Four'}	
for key,value in dic.items():
	print 'dic[',key,']=',value
	
#judge whether complet the Interface called "Iterable" 
from collections import Iterable	
print isinstance('abc', Iterable)	
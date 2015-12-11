print 'Python 2.x version can only convert ASCII char to int'
print ord('a')
print chr(97)
test = input("please input a number:\n")
print 'the square of number is' , test*test
if test > 10:
	print 'this number is bigger than 10'
elif test >= 5:
	print 'this number is between 5 and 10'
else:
	print 'this number is smaller than 5'
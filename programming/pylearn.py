# python learning exercises

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune')", swap('fame', 'fortune')

#Arithmetic Functions

def reverse(x):
	return -x

def plus(a, b):
	return a + b
	
def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	diff = d - b
	if diff < 0:
		diff *= -1
	return diff
	
def divide(w, p):
	return w / float(p)
	
def remainder(w, p):
	return w % p

def power(x, e):
	answer = 1
	for i in range(e):
		answer *= x
	return answer

def power2(x, e):
	return x ** e
	
def calculate(a, b, c, d, e):
	return (a + b / d - e) * c

def ratio(f1, f2):
	if f1 > f2:
		return f1 / f2
	else:
		return f2 / f1

def pythagoras(a, b):
	return (a**2 + b**2)**(.5)

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "testing plus(1, 1): ", plus(1, 1)
	print "testin' diff(12, 5): ", diff(12, 5)
	print "test abs_diff(10, 5): ", abs_diff(10, 5)
	print "test abs_diff(5, 10): ", abs_diff(5, 10)
	print "test divide(10, 2): ", divide(10, 2)
	print "test divide(2, 10): ", divide(2, 10)
	print "test remainder(40, 19): ", remainder(40, 19)
	print "test remainder(126, 19): ", remainder(126, 19)
	print "test remainder(133, 19): ", remainder(133, 19)
	print "test power(2, 3): ", power(2, 3)
	print "test calculate(1, 2, 3, 4, 5): ", calculate(1, 2, 3, 4, 5)
	print "testing ratio(7.7, 2.8): ", ratio(7.7, 2.8)
	print "testing ratio(2.8, 7.7): ", ratio(2.8, 7.7)
	print "testing pythagoras(3, 4): ", pythagoras(3, 4)
	print "testing pythagoras(28, 32): ", pythagoras(28, 32) 

#boolean expressions
def at_most_thirteen(x):
	return x <= 13

def at_least_thirteen(x):
	return x >= 13

def less_than(x, y):
	if x < y:
		return True
	else:
		return False

def not_same(x, y):
	if x != y:
		return True
	else:
		return False

def no_diff(x, y):
	if x == y:
		return True
	else: 
		return False

def bigger(x, y):
	if x > y:
		return True
	else:
		return False

def positive(num):
	if num >= 0:
		return True
	else:
		return False

def reverse(jimmy):
	return not jimmy

def main_boolean():
	print "testing reverse(True): ", reverse(True)
	print "testing reverse(False): ", reverse(False)
	print "test positive(-4):", positive(-4)
	print "test positive(23):", positive(23)
	print "test bigger(5, 4):", bigger(5, 4)
	print "test bigger(3, 7):", bigger(3, 7)
	print "test no_diff(5, 4):", no_diff(5, 4)
	print "test no_diff(5, 5):", no_diff(5, 5)
	print "test not_same(5, 4):", not_same(5, 4)
	print "test not_same(5, 5):", not_same(5, 5)
	print "test less_than(5, 4):", less_than(5, 4)
	print "test less_than(4, 5):", less_than(4, 5)
	print "test at_least_thirteen(14):", at_least_thirteen(14)
	print "test at_least_thirteen(5):", at_least_thirteen(5)
	print "test at_most_thirteen(14):", at_least_thirteen(14)
	print "test at_most_thirteen(5):", at_least_thirteen(5)
	
def main():
	main_function()
	main_arithmetic()
	main_boolean()
	
main()
#data structures
#the first function should always be called "def main():"
def students():
	n = int(input("Enter the number of students:"))
	data = {} # here we will store the data
	languages = ('Physics', 'Maths', 'History')
	for i in range(0, n): 
    		name = input('Enter the name of the student %d: ' % (i + 1)) 
    	marks = []
    for x in languages:
        marks.append(int(input('Enter marks of %s: ' % x))) 
    	data[name] = marks
	for x, y in data.items():
    	total =  sum(y)
    	print("%s 's  total marks %d" % (x, total))
    	if total < 120:
        	print("%s failed :(" % x)
    	else:
        	print("%s passed :)" % x)


def matrixmul():
	n = int(input("Enter the value of n: "))
	print("Enter values for the Matrix A")
	a = []
	for i in range(0, n):
    	a.append([int(x) for x in input("").split(" ")])
	print("Enter values for the Matrix B")
	b = []
	for i in range(0, n):
    	b.append([int(x) for x in input("").split(" ")])
	c = []
	for i in range(0, n):
    	c.append([a[i][j] * b[j][i] for j in range(0, n)])
	print("After matrix multiplication")
	print("-" * 10 * n)
	for x in c:
    	for y in x:
        	print("%5d" % y, end=' ')
    	print("")
	print("-" * 10 * n)


def main():
	students()
	matrixmul()

main()
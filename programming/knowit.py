#learning what I already know
print "Introduction program"
import math
print "Hello, World!"
print math.e
a, b = 13, 23
print a
print b
print a + b

number = int(raw_input("Enter an integer: "))
if number < 100:
	print "Your number is smaller than 100"
else:
	print "Your number is larger than 100"

print "\n new section \n"

print "this is an investment calculator"
amount = float(raw_input("Enter amount: "))
inrate = float(raw_input("Enter Interest rate: "))
period = int(raw_input("Enter period: "))
value = 0
year = 1
while year <= period:
	value = amount + (inrate * amount)
	print "Year %d Rs. %.2f" % (year, value)
	amount = value
	year += 1

print "\n new section \n"

print "this is an average calculator"
N = 10
sum = 0
count = 0
while count < N:
	number = float(raw_input(""))
	sum += number
	count += 1
average = float(sum)/N
print "N = %d , Sum = %f" % (N, sum)
print "Average = %f" % average

print "\n new section \n"

print "fahrenheit to celsius converter"
fahrenheit = 0.0
print "Fehrenheit Celsius"
while fahrenheit <= 250:
	celsius = ( fahrenheit - 32.0 ) / 1.8
	print "%5.1f %7.2f" % (fahrenheit, celsius)
	fahrenheit += 25.0

print "\n new section \n"

print "standard calculator"
sum = 0.0
for i in range(1, 11):
	sum += 1.0 / i
print "%2d %6.4f" % (i, sum)

print "\n new section \n"

print "quadratic equation calculator"
a = int(raw_input("Enter value of a: "))
b = int(raw_input("Enter value of b: "))
c = int(raw_input("Enter value of c: "))
d = b * b -4 * a * c
if d < 0:
	print "ROOTS are imaginary"
else:
	root1 = (-b + math.sqrt(d)) / (2.0 * a)
	root2 = (-b - math.sqrt(d)) / (2.0 * a)
	print "Root 1 = ", root1
	print "Root 2 = ", root2

print "\n new section \n"

print "salary for a camera salesman"
basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02
numberofcamera = int(raw_input("Enter the number of inputs sold: "))
price = float(raw_input("Enter the total prices: "))
bonus = (bonus_rate * numberofcamera)
commision = (commision_rate * numberofcamera * price)
print "Bonus        = %6.2f" % bonus
print "Commision    = %6.2f" % commision
print "Gross salary = %6.2f" % (basic_salary + bonus + commision)

print "\n new section \n"

print "fahrenheit to celsius converter"
fahrenheit = 0.0
print "Fehrenheit Celsius"
while fahrenheit <= 250:
	celsius = ( fahrenheit - 32.0 ) / 1.8
	print "%5.1f %7.2f" % (fahrenheit, celsius)
	fahrenheit += 25.0

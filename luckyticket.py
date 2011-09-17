import sys
def lucky(ticket):
	str_array = []
	good_array = []
	result = []
	main_result = []
	i = 0
	
	try:
		ticket = str(ticket)
		if (len(ticket) != 6):
			return "6 digits!!!"
	except:
		return "Can't translate to string"
	for char in ticket:
		str_array.append(char)
	good_array.append(str_array[:len(str_array)/2])
	good_array.append(str_array[len(str_array)/2:])
	for side_array in good_array:
		for numer in side_array:
			i = i + int(numer)
		result.append(i)
		i = 0
	for numer in result:
		if (numer < 10):
			main_result.append(numer)
		else:
			str_numer = str(numer)
			m = 0
			for i in str_numer:
				m = m + int(i)
			main_result.append(m)
	if (main_result[0] == main_result[1]):
		return "You have a lucky ticket"
	else:
		return "This is not lucky ticket, sorry :("
	return res
		 
try:
	ticket = input("Enter your ticket number(6 digits):\n")
except Exception:
	print "Try again!"
	sys.exit(0)
print lucky(ticket)

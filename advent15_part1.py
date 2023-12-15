def Hash(string):
	val = 0
	for char in string:
		val += ord(char)
		val *= 17
		val = val%256
	return val

with open('input15.txt') as fin:
	sum = 0
	for line in fin:
		line = line.strip("\n")
		list = line.split(",")
		for el in list:
			sum += Hash(el)
	print(sum)			
				
	

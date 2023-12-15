def Hash(string):
	val = 0
	for char in string:
		val += ord(char)
		val *= 17
		val = val%256
	return val
box = [{} for i in range(256)]
with open('input15.txt') as fin:
	sum = 0
	for line in fin:
		line = line.strip("\n")
		list = line.split(",")
		for el in list:
			if "=" in el:
				[label,foc] = el.split("=")
				box[Hash(label)][label] = int(foc)
			elif "-" in el:
				label = el.split("-")[0]
				try:
					del box[Hash(label)][label]
				except:
					pass			
				
	for i,contents in enumerate(box):
		for j,lens in enumerate(contents):
			sum+= (i+1)*(j+1)*contents[lens]
					
	print(sum)			
				
	

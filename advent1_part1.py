with open('input1.txt') as fin:
	sum = 0
	for line in fin:
		num = 0
		num_lst = []
		for char in line:
			if char.isdigit():
				num_lst.append(char)
				break	
		for char2 in reversed(line):
			if char2.isdigit():
				num_lst.append(char2)	
				break
		#print(num_lst)	
		num = int("".join(num_lst))
		sum+=num
	print(sum)			 

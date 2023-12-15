with open('input1.txt') as fin:
	sum = 0
	txt_numbers = {'one':1 , 'two':2 , 'three':3 , 'four':4, 'five':5 , 'six':6, 'seven':7, 'eight':8 , 'nine':9}
	for line in fin:
		for number in txt_numbers:
			line = line.replace(number , number + str(txt_numbers[number]) + number) 
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

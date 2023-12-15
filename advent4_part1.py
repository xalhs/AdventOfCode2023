with open('input4.txt') as fin:
	sum = 0
	for line in fin:
		part1 = (line.replace("  ", " ").split(": ")[1].split(" | ")[0])
		winning_num_str = part1.split(" ")
		winning_num = [int(i) for i in winning_num_str]
		part2 = line.replace("  ", " ").replace("\n","").split(": ")[1].split(" | ")[1]
		your_num_str = part2.split(" ")
		your_num = [int(i) for i in your_num_str]
		value = 0
		for num in your_num:
			if num in winning_num:
				if value == 0:
					value = 1
				else:
					value*=2	
		print(value)	
		sum+=value
	print(sum)			 

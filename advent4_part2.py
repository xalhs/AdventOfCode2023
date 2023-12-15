with open('input4.txt') as fin:
	mult =[]
	for j,l in enumerate(fin):
		mult.append(1)	
with open('input4.txt') as fin:		
	for j,line in enumerate(fin):
		part1 = (line.replace("  ", " ").split(": ")[1].split(" | ")[0])
		winning_num_str = part1.split(" ")
		winning_num = [int(i) for i in winning_num_str]
		part2 = line.replace("  ", " ").replace("\n","").split(": ")[1].split(" | ")[1]
		your_num_str = part2.split(" ")
		your_num = [int(i) for i in your_num_str]
		value = 0
		for num in your_num:
			if num in winning_num:
				value+=1	
		#value*= mult[j]
		for k in range(j+1,j+value+1):
			try:
				mult[k]+=mult[j]
			except:
				pass	
	print(sum(mult))		 

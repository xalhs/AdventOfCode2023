with open('input8.txt') as fin: 
	l1 = fin.readline().strip("\n")
	l1= l1.replace("L" , "0")
	l1 = l1.replace("R" , "1")
	fin.readline()
	l = {}
	for line in fin:
		l[line.split(" =")[0]] = [line.split("= (")[1].split(",")[0], line.split(", ")[1].strip(")\n")]
	loc = 'AAA'
	steps = 0
	while loc != 'ZZZ':
		loc = l[loc][int(l1[steps%len(l1)])]
		steps +=1
		#print(loc)	
	print(steps)	

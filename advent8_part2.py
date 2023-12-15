def are_we_there_yet(loc):
	thing = True
	for loc1 in loc:
		if not loc1.endswith("Z"):
			thing = False
	return thing			

import math
def lcm(a,b):
	return int(a*b/math.gcd(a,b))
total = 1
with open('input8.txt') as fin: 
	l1 = fin.readline().strip("\n")
	l1= l1.replace("L" , "0")
	l1 = l1.replace("R" , "1")
	fin.readline()
	l = {}
	starting_points =[]
	for line in fin:
		l[line.split(" =")[0]] = [line.split("= (")[1].split(",")[0], line.split(", ")[1].strip(")\n")]
		if line.split(" =")[0].endswith("A"):
			starting_points.append(line.split(" =")[0])
	for loc in starting_points:				
		steps = 0
		while not loc.endswith("Z"):
			loc = l[loc][int(l1[steps%len(l1)])]
			steps +=1
		total = lcm(total,steps)
		print(steps)
	print(total)	

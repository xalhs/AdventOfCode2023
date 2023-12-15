def abs(a):
	if a>=0:
		return a
	else:
		return -a

with open('input11.txt') as fin: 
	map = []
	for line in fin:
		if "#" in line :
			map.append(line.strip("\n"))
		else:	
			print("expanding row")
			map.append(line.strip("\n"))
			map.append(line.strip("\n"))
	i = 0		
	while i < len(map[0]): 		
		#for i in range(2*(len(map[0])-1)):
		has_galaxy = False
		for j in range(len(map)):
			if map[j][i] =="#":
				has_galaxy = True
		if has_galaxy == False:
			print("expanding column")
			for j in range(len(map)):
				map[j] = list(map[j])
				map[j].insert(i , ".")
				map[j] = "".join(map[j])
			i+=1
		i+=1		
		
	positions = []
	for i in range(len(map) ):
		for j in range(len(map[0])):
			if map[i][j] == "#":
				positions.append([i,j])	
	sum = 0			
	for i in range(len(positions)):
		for j in range(i+1 , len(positions)):
			sum+= abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
	print(sum)					

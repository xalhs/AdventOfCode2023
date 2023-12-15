def abs(a):
	if a>=0:
		return a
	else:
		return -a

with open('input11.txt') as fin: 
	map = []
	rows_to_expand = []
	cols_to_expand = []
	positions = []
	for i,line in enumerate(fin):
		if "#" in line:
			for j in range(len(line)):
				if line[j] == "#":
					positions.append([i,j])
		else:
			rows_to_expand.append(i)
					
		map.append(list(line.strip("\n")))

	i = 0		
	while i < len(map[0]): 		
		#for i in range(2*(len(map[0])-1)):
		has_galaxy = False
		for j in range(len(map)):
			if map[j][i] =="#":
				has_galaxy = True
		if has_galaxy == False:
			cols_to_expand.append(i)
		i+=1		

	sum = 0			
	exp = 999999
	dif ={}
	for i in range(len(positions)):
		for j in range(i+1 , len(positions)):
			dif[(i,j)] = 0
			for k in range(len(rows_to_expand)):
				if rows_to_expand[k] in range(min(positions[i][0] , positions[j][0] ), max(positions[i][0],positions[j][0])):
				#	print(positions[i])
				#	print(positions[j])
				#	print("##############")
					dif[(i,j)] += exp
					sum+= exp
			for k in range(len(cols_to_expand)):		
				if cols_to_expand[k] in range(min(positions[i][1] , positions[j][1] ), max(positions[i][1],positions[j][1])):
					sum+= exp  
					dif[(i,j)] += exp 
			
			sum+= abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
			dif[(i,j)] += abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
	print(sum)	
					

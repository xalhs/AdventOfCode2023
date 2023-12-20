def move(current_pos , direction, amount , pattern):
	if direction == "R":
		pattern[current_pos[0]] = pattern[current_pos[0]][:(current_pos[1]+1)] + "#"*amount + pattern[current_pos[0]][(current_pos[1] + amount+1):]
		current_pos[1] += amount
	if direction == "L":
		pattern[current_pos[0]] = pattern[current_pos[0]][:(current_pos[1]-amount)] + "#"*amount + pattern[current_pos[0]][(current_pos[1]):]
		current_pos[1] -= amount
	if direction == "U":
		for i,row in enumerate(pattern):
			if  current_pos[0] - amount <= i < current_pos[0]:
				pattern[i] = pattern[i][:(current_pos[1])] + "#" +  pattern[i][(current_pos[1]+1):] 
		current_pos[0] -= amount
	if direction == "D":
		for i,row in enumerate(pattern):
			if  current_pos[0] < i <= current_pos[0] + amount:
				pattern[i] = pattern[i][:(current_pos[1])] + "#" +  pattern[i][(current_pos[1]+1):]
		current_pos[0] += amount
	return current_pos , pattern
	
with open('input18.txt') as fin:
	max_right = 0
	right = 0
	max_bot = 0
	bot = 0 
	max_up = 0
	max_left = 0
	input18 = []
	for line in fin:
		[direction , amount, color] = line.strip("\n").split(" ")
		amount = int(amount)
		if direction == "R":
			right += amount
		if direction == "L":
			right -= amount
		if direction == "U":
			bot -= amount
		if direction == "D":
			bot+= amount
		
		if bot > max_bot:
			max_bot = bot
		if right > max_right:
			max_right = right 
		if bot < max_up:
			max_up = bot
		if right < max_left:
			max_left = right
		input18.append(line.strip("\n")	)
	row = ""
	pattern = []
	dir_pattern = []
	for j in range(max_right - max_left+1+1):	
		row += "."	
	for i in range(max_bot - max_up+1):
		pattern.append(row)
		dir_pattern.append([])
		dir_pattern[i] = [ [] for x in range(len(row)) ] 
		
	starting_pos = [-max_up , -max_left]	
	current_pos = [-max_up , -max_left]
	for line in input18:
		[direction , amount, color] = line.split(" ")
		amount = int(amount)
		prev_current_pos = current_pos.copy()
		current_pos , pattern = move(current_pos , direction , amount,pattern)
		if direction == "U":
			for i in range(amount -1):
				dir_pattern[current_pos[0] +i+ 1][prev_current_pos[1]]  = 1
				dir_pattern[prev_current_pos[0]][prev_current_pos[1]] = 0.5
				dir_pattern[current_pos[0]][prev_current_pos[1]] = 0.5  
		elif direction == "D":
			for i in range(amount -1):
				dir_pattern[prev_current_pos[0] +i+ 1][prev_current_pos[1]]  = -1
				dir_pattern[prev_current_pos[0]][prev_current_pos[1]] = -0.5 	
				dir_pattern[current_pos[0]][prev_current_pos[1]] = -0.5  	
		
	k = 0	
	list_of_pos_before = []
	list_of_pos_after = []	
	inside = 0
	for i, row in enumerate(pattern):
		upness = 0
		am = 0
		prev_upness = 0
		for j, char in enumerate(row):
			prev_upness = upness
			try:
				upness += dir_pattern[i][j]
			except:
				pass
			if upness >0 or prev_upness > 0:
				am +=1
		inside += am		
	print(inside)		

		
							
		

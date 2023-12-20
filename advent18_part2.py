def move(current_pos , direction, amount , pattern):
	if direction == "R":
		current_pos[1] += amount
	if direction == "L":
		current_pos[1] -= amount
	if direction == "U":
		current_pos[0] -= amount
	if direction == "D":
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
		amount = int(color[2:7] , 16)
		if color[-2] == "0":
			direction = "R"
		if color[-2] == "1":
			direction = "D"
		if color[-2] == "2":
			direction = "L"
		if color[-2] == "3":
			direction = "U"

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
	dir_pattern = {}
	starting_pos = [-max_up , -max_left]
	current_pos = [-max_up , -max_left]
	important_rows = []
	important_rows.append(current_pos[0])
	important_rows.append(current_pos[0]+1)
	important_rows.append(current_pos[0]-1)
	important_cols = []
	important_cols.append(current_pos[1])
	important_cols.append(current_pos[1]+1)
	important_cols.append(current_pos[1]-1)
	for k,line in enumerate(input18):
		[direction , amount, color] = line.split(" ")
		amount = int(color[2:7] , 16)
		if color[-2] == "0":
			direction = "R"
		if color[-2] == "1":
			direction = "D"
		if color[-2] == "2":
			direction = "L"
		if color[-2] == "3":
			direction = "U"
		prev_current_pos = current_pos.copy()
		current_pos , pattern = move(current_pos , direction , amount,pattern)
		important_rows.append(current_pos[0])
		important_rows.append(current_pos[0]+1)
		important_rows.append(current_pos[0]-1)
		important_cols.append(current_pos[1])
		important_cols.append(current_pos[1]+1)
		important_cols.append(current_pos[1]-1)
		if direction == "U":
			for i in range(1):
				dir_pattern[(current_pos[0] +i+ 1,prev_current_pos[1])]  = 1
				dir_pattern[(prev_current_pos[0]  -i- 1,prev_current_pos[1])]  = 1
			dir_pattern[(prev_current_pos[0],prev_current_pos[1])] = 0.5
			dir_pattern[(current_pos[0],prev_current_pos[1])] = 0.5
		elif direction == "D":
			for i in range(1):
				dir_pattern[(prev_current_pos[0] +i+ 1,prev_current_pos[1])]  = -1
				dir_pattern[(current_pos[0] -i- 1,prev_current_pos[1])]  = -1
			dir_pattern[(prev_current_pos[0],prev_current_pos[1])] = -0.5
			dir_pattern[(current_pos[0],prev_current_pos[1])] = -0.5
	current_pos = [-max_up , -max_left]
	for k,line in enumerate(input18):
		[direction , amount, color] = line.split(" ")
		amount = int(color[2:7] , 16)
		if color[-2] == "0":
			direction = "R"
		if color[-2] == "1":
			direction = "D"
		if color[-2] == "2":
			direction = "L"
		if color[-2] == "3":
			direction = "U"
		prev_current_pos = current_pos.copy()
		current_pos , pattern = move(current_pos , direction , amount,pattern)
		for row in important_rows:
			if row in range( min(prev_current_pos[0] ,current_pos [0] ) + 1, max(current_pos[0] ,prev_current_pos[0]  ) ):
				if direction == "U":
					dir_pattern[(row,current_pos[1])] = 1
				elif direction == "D":
					dir_pattern[(row,current_pos[1])] = -1

	k = 0
	list_of_pos_before = []
	list_of_pos_after = []
	inside = 0
	important_rows = list(dict.fromkeys(important_rows))
	important_cols = list(dict.fromkeys(important_cols))
	important_cols.sort()
	important_rows.sort()
	rows_passed = 0
	for k,i in enumerate(important_rows):
		if i in important_rows:
			upness = 0
			am = 0
			prev_upness = 0
			inc = 0
			for l,j in enumerate(important_cols):
				inc = 0
				prev_upness = upness
				try:
					upness += dir_pattern[(i,j)]
				except:
					pass
				if upness >0 or prev_upness > 0:
					inc = 1
				am += inc*(important_cols[l] - important_cols[l-1])

		inside += am*(important_rows[k] - important_rows[k-1])
	print(inside)

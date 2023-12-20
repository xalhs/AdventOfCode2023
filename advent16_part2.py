def move(beam_pos , beam_dir):
	if beam_dir == "up":
		beam_pos[0] -=1
	if beam_dir == "left":
		beam_pos[1] -=1
	if beam_dir == "down":
		beam_pos[0] +=1
	if beam_dir == "right":
		beam_pos[1] += 1	
	return beam_pos		

def interact(beam_pos , beam_dir , target , beams):
	#if target == "."
	if target == "\\":
		#print("hit a \\")
		if beam_dir == "right":
			beam_dir = "down"
		elif beam_dir == "left":
			beam_dir = "up"
		elif beam_dir == "down":
			beam_dir = "right"
		elif beam_dir == "up":
			beam_dir = "left"		
	if target == "/":
		#print("hit a /")
		if beam_dir == "left":
			beam_dir = "down"
		elif beam_dir == "right":
			beam_dir = "up"
		elif beam_dir == "down":
			beam_dir = "left"
		elif beam_dir == "up":
			beam_dir = "right"	
	if target == "|":
		if beam_dir == "left" or beam_dir == "right":
			beam_dir = "up"
			beams.append([[beam_pos[0],beam_pos[1]] , "down"])
		#print("hit a |")	
	if target == "-":
		#print("hit a -")
		if beam_dir == "up" or beam_dir == "down":
			beam_dir = "left"
			beams.append([[beam_pos[0],beam_pos[1]] , "right"])
		#	print(beams)
	
	return beam_dir , beams		
					
			
					
				 	

with open('input16.txt') as fin:
	starting_configs = []
	beams = [[[0,0], 'right' ]]
	
	pattern = []
	
	for line in fin:
		pattern.append(line.strip("\n"))
		
	
				
	max_bot = len(pattern)-1
	max_right = len(pattern[0]) -1
	for i in range(len(pattern)):
		starting_configs.append([[i,0] , "right"])
		starting_configs.append([[i,max_right] , "left"])
	for j in range(len(pattern[0])):
		starting_configs.append([[0,j] , "down"])
		starting_configs.append([[max_bot,j] , "up"])	
		
	max_count = 0	
	for starting_config in starting_configs:
		beams = [[[starting_config[0][0] , starting_config[0][1]] , starting_config[1]] ]	
		been_to = []
		energized = {}
		for i,line in enumerate(pattern):
			for j,char in enumerate(line):
				energized[(i,j)] = False
		count = 0
		while beams != []:
			beam = beams[0]
			#print(beam)
			if beam in been_to:
				#print("beam repeated")
				beams.pop(0)
				continue
			if beam[0][0] > max_bot or beam[0][0] <0 or beam[0][1] > max_right or beam[0][1] <0:
				#print("beam died")
				beams.pop(0)
				continue	
			been_to.append([[beam[0][0] , beam[0][1]] , beam[1]])  	
			if energized[(beam[0][0],beam[0][1])] != True:
				count +=1
				energized[(beam[0][0],beam[0][1])] = True	
			target = pattern[beam[0][0]][beam[0][1]]
			beam[1] , beams = interact( beam[0] , beam[1] , target , beams)
			beam[0] = move(beam[0] , beam[1])
			#print(beam)
		if count > max_count:
			max_count = count	
		print(count)
	print(max_count)			
			

		


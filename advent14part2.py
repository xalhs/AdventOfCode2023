def tilt(pattern):
	for i,line in enumerate(pattern):
		for j,char in enumerate(line):
			if char == ".":
				for k in range(i+1 , len(pattern)):
					if pattern[k][j] == "O":
						pattern[k] = pattern[k][:j] + "." + pattern[k][(j+1):]
						pattern[i] = pattern[i][:j] + "O" + pattern[i][(j+1):]
						break
					elif pattern[k][j] == "#":
						break	
	#for line in pattern:
	#	print(line)					
	return pattern		
	
def calc_load(pattern):
	load = 0
	for i, line in enumerate(pattern):
		for char in line:
			if char == "O":
				load += len(pattern) - i
	return load			

def spin_right(pattern):
	new_pattern = ["" for i in range(len(pattern))]
	
	neu_pat = [["a" for j in range(len(pattern))] for i in range(len(pattern[0]))]
	for i, line in enumerate(pattern):
		for j,char in enumerate(line):
			#neu_pat[len(line)-j-1][i] = char
			neu_pat[j][len(pattern) - i-1] = char
			#neu_pat[len(line)-j-1] = neu_pat[len(line) - j -1] + char
	for i,line in enumerate(neu_pat):
		for char in line:
			new_pattern[i]+= char			
	#new_pattern = [neu_pat[len(neu_pat) - i - 1] for i in range(len(neu_pat))]
	#for line in new_pattern:
	#	print(line)	
	return(new_pattern)	
				
	
with open('input14.txt') as fin:
	sum = 0
	pattern = []
	p = 0
	for line in fin:
		pattern.append(line.strip("\n"))
	for i in range(2000):
		for j in range(4):			
			pattern = tilt(pattern)
			#print("\n")
			pattern = spin_right(pattern)
			#print("\n")
		
		if (i+1)%18 == 1000000000%18:
			print(calc_load(pattern))	
#	for line in pattern:
#		print(line)		
	

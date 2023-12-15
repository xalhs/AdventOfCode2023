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
	return pattern		
	
def calc_load(pattern):
	load = 0
	for i, line in enumerate(pattern):
		for char in line:
			if char == "O":
				load += len(pattern) - i
	return load			
	
with open('input14.txt') as fin:
	sum = 0
	pattern = []
	p = 0
	for line in fin:
		pattern.append(line.strip("\n"))
	pattern = tilt(pattern)
	print(calc_load(pattern))

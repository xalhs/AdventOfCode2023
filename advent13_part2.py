def find_reflection(pattern , init_reflect):
	found = False
	for col in range(0,len(pattern[0])-1):

		ref = True
		for row in range(len(pattern)):
			if col <= len(pattern[0])/2-1:
				for i in range(col+1):
					if pattern[row][i] != pattern[row][2*col-i+1]:
						ref = False
						break
			else:
				for i in range(len(pattern[0]) -  col -1):
					if pattern[row][col -i] != pattern[row][col + i +1]:
						ref = False
						break
			if ref == False:
				break
		if ref == True:
			if [0,col] != init_reflect:
				found = True
				return[0 , col]
	for row in range(0,len(pattern)-1):
		ref = True
		for col in range(len(pattern[row])):
			if row <= len(pattern)/2-1:
				for i in range(row +1):
					if pattern[i][col] != pattern[2*row -i +1][col]:
						ref = False
						break
			else:
				for i in range(len(pattern) - row  -1 ):
					if pattern[row -i][col] != pattern[row +i +1][col]:
						ref = False
						break
		if ref == True:
			if [1,row] != init_reflect:
				found = True
				return[1 , row]

	if found == False:
		pass
	return False

with open('input13.txt') as fin:
	sum = 0
	pattern = []
	p = 0
	for line in fin:
		if line == "\n":
			init_answer =  find_reflection(pattern , [])
			found = False
			for i in range(len(pattern)):
				for j in range(len(pattern[0])):
					new_pattern = pattern.copy()
					if new_pattern[i][j] == ".":
						new_pattern[i] = new_pattern[i][:j] + "#" + new_pattern[i][j+1:]

					if new_pattern[i][j] == "#":

						new_pattern[i] = new_pattern[i][:j] + "." + new_pattern[i][j+1:]
					answer = find_reflection(new_pattern , init_answer)
					if answer == init_answer or answer == False:
						continue
					else:
						sum+= (answer[0]*99 + 1)*(answer[1] + 1)
						break
				if found:
					break

			if found == False:
				pass

			pattern = []
		else:
			pattern.append(line.strip("\n"))
print(sum)

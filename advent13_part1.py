with open('input13.txt') as fin:
	sum = 0
	pattern = []
	for line in fin:
		if line == "\n":
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
					found = True
					sum += col+1
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
					found = True
					sum += (row+1)*100

			if found == False:
				print(pattern)
			pattern = []
		else:
			pattern.append(line.strip("\n"))
print(sum)

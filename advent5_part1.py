with open('input5.txt') as fin: 
	seeds = [int(i) for i in fin.readline().strip('\n').split("seeds: ")[1].split(" ")]
	start = False
	mapp = [{}]
	i = 0
	for line in fin:
		if start == True and line == "\n":
			mapp.append({})
			i+=1
			start = False
		#	print("truool")	
		if start == True:
			args = [int(j) for j in line.strip("\n").split(" ")]
			mapp[i][range(args[1] , args[1] + args[2] )] = +args[0] - args[1]
		if ":" in line:
			start = True	
loc = []
for seed in seeds:
	print ("new seed")
	for k in range(len(mapp)):
		temp_seed = seed
		mapped = False
		for mappen in mapp[k]:
			if seed in mappen:
				#print("mappen")
				if mapped == True:
					print("big problem Okayeg")
					sys.exi()
				mapped = True
				#print(mappen)
				temp_seed += mapp[k][mappen]
				#print(temp_seed)
				#print("lol")
				if temp_seed == -1:
					sys.exit()
				
		seed = temp_seed
		print(seed)
	loc.append(seed)
print(min(loc))				

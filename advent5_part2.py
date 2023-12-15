with open('input5.txt') as fin: 
	seed_parse = [int(i) for i in fin.readline().strip('\n').split("seeds: ")[1].split(" ")]
	seed_rang = []
	for i in range(int(len(seed_parse)/2)):
		seed_rang.append(range(seed_parse[2*i] , seed_parse[2*i] + seed_parse[2*i+1]))
				
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
			
def range_dif (r1, r2):
	if r1.start == r2.start:
		return [range(r1.stop  , r2.stop)]
	if r1.stop == r2.stop:	
		return [range(r2.start , r1.start)]
	else:
		return [range(r2.start , r1.start) , range(r1.stop  ,  r2.stop)]	
ssfwlthl = [seed_rang]
for k in range(len(mapp)):
	ssfwlthl.append([])
	for seed in ssfwlthl[k]:
		rang1 = [seed]
		for mappen in mapp[k]:
			rang_temp =[]
			for another_rang in rang1:
				if mappen.start <= another_rang.start and mappen.stop >= another_rang.stop:
					ssfwlthl[k+1].append(range(another_rang.start +  mapp[k][mappen] , another_rang.stop + mapp[k][mappen]))
					if range(another_rang.start +  mapp[k][mappen] , another_rang.stop + mapp[k][mappen]) == range(90,93):
						sys.exit()
				elif max(another_rang.start , mappen.start) < min(another_rang.stop , mappen.stop) :
					intersect = range(max(another_rang.start , mappen.start) , min(another_rang.stop , mappen.stop) )	
					ssfwlthl[k+1].append(range(intersect.start + mapp[k][mappen], intersect.stop + mapp[k][mappen]))
					if range(intersect.start + mapp[k][mappen], intersect.stop + mapp[k][mappen]) == range(90,93):
						sys.exit()
					rang_temp +=  range_dif(intersect , another_rang)
					if range(90,93) in rang_temp:
						sys.exit()
				else:
					rang_temp += [another_rang]
					if range(90,93) in rang_temp:
						sys.exit()	
			rang1 = rang_temp
		ssfwlthl[k+1] += rang1		

mini = [a.start for a in ssfwlthl[-1]]
print(min(mini))									

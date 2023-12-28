global lookup_table
import traceback
lookup_table = [[] for i in range(80)]

for i in range(80):
	lookup_table[i] = [[] for j in range(80)]
def valid_config(config , list):
	list1 = []
	prev_thing = "."
	count = 0
	while config != "":
		if config[0] == "#":
			count +=1
		if config[0] == "." and prev_thing == "#":
			list1.append(count)
			count = 0
		prev_thing = config[0]
		config = config[1:]
	if count !=0:
		list1.append(count)
	if list1 == list:
		return 1
	else:
		return 0

def nested_loop1(string  , question_list , list):
	if list == [] and not "#" in string:
		return 1
	elif list == [] and "#" in string:
		return 0

	if string.count("#") > sum(list):
		return 0

	if string.count("?") == len(string):
		return f(len(string) - sum(list) + len(list) ,  len(list))

	count = 0
	sum_of_rest = 0
	max_1 = max(list)
	list1 = [i for i in list if i != max_1]
	if list1 != []:
		max_2 = max(list1)
	else:
		max_2 = 0
	if "#"*(max_2+1) in string:
		if (max_1+1)*"#" in string:
			return 0
		for y in range(max_1 , max_2 , -1):
			if "#"*y in string:
				indexy = string.find("#"*y)
				break
		tot = 0
		index = list.index(max_1)
		for v in range(list.count(max_1)):
			before_list = list[:index]
			after_list = list[index + 1:]
			if max_1 in list[index+1:]:
				index = list.index(max_1 , index+1)
			for t in range(max_1 - y + 1):
				sub_tot = 0
				try:
					if (indexy+y-max_1+t) >= 0 and  y+indexy+t<= len(string):
						new_string = string[: (indexy+y-max_1+t)] + "#"*max_1 + string[y+indexy+t:]
					else:
						new_string = string[: (indexy+y-max_1+t)] + "#"*max_1 + string[y+indexy+t:]
						continue

					before_string = new_string.split("#"*max_1 , 1)[0]

					after_string = new_string.split("#"*max_1 , 1)[1]
					if  before_string != "" and before_string[-1] == "?" :
						before_string = before_string[:-1]
					elif before_string != "" and before_string[-1] == "#":
						continue
					if  after_string != "" and after_string[0] == "?" :
						after_string = after_string[1:]
					elif  after_string != "" and after_string[0] == "#" :
						continue

					sub_tot = final_nest ( [before_string ], before_list)
					sub_tot *= nested_loop1(after_string , [] , after_list)
					tot += sub_tot

				except:
					print(new_string)
					traceback.print_exc()
					pass
		return tot



	if not "?" in string:
		return valid_config(string, list)

	if "#" in string:
		tot = 0
		max_seg_sum = 0
		max_first_seg = 1
		try:
			hash_length = string[string.index("#"):].index("?")
		except:
			hash_length = len(string[string.index("#"):])
		pre_string = string[:string.index("#")]
		for item1 in list:
			if max_seg_sum + item1 + 1 <= len(pre_string):
				max_first_seg+=1
				max_seg_sum += item1 + 1
			else:
				break
		if max_first_seg > len(list):
			max_first_seg = len(list)
		for d in range(max_first_seg):
			if list[d] < (hash_length):
				continue
			min_s = max(0, list[d]  - (hash_length) - len(pre_string) )
			max_s = min(list[d]  - (hash_length)  + 1 ,  len(string) - (string.index("#") + hash_length )  + 1 )
			for s in range(  min_s ,    max_s        ):
				part_tot = 1
				try:
					if string[string.index("#"):][hash_length+s] == "#":
						continue
				except:
					pass

				before_string = string[:string.index("#")][:-(list[d] - (hash_length) - s + 1)]
				after_string = string[string.index("#"):][hash_length+s+1:]
				b_list = list[:d]
				part_tot*=nested_loop1( before_string , [] , list[:d])
				if part_tot == 0:
					continue
				a_list = list[d+1:]
				part_tot*=nested_loop1(  after_string, [] , list[d+1:] )
				tot +=part_tot
		return tot

	for i in list:
		sum_of_rest += int(i)
	valid_dots =0
	for i, char in enumerate(string):
		char_valid = 0
		if char == "." :
			if not i ==0:
				if string[i-1] != ".":
					char_valid = 1
			if not i == len(string) -1:
				if string[i+1] != ".":
					char_valid =1
		valid_dots += char_valid

	for i, char in enumerate(string):

		if sum_of_rest + len(list) - 1 > len(string) - i: #string.count("?") + string.count("#") + valid_dots - i:
			break
		elif char == "#" :
			allowed = True
			for j in range(list[0]):
				if string[i+j] == ".":
					allowed = False
			try:
				if string[i+j+1] == "#":
					allowed = False
				else:
					pass
			except:
				pass
			if allowed:
				count += nested_loop1(string[(i+(list[0])+1):] , question_list , list[1:])
			break
		elif char == ".":
			continue
		else:
			allowed = True
			for j in range(list[0]):
				if string[i+j] == ".":
					allowed = False
			try:
				if string[i+j+1] == "#":
					allowed = False
				else:
					pass
			except:
				pass
			if allowed:
				count += nested_loop1(string[(i+(list[0]+1)):] , question_list , list[1:])

	return count

def nested_loop(string , list1 , list2):
	count = 0
	for char in ["#" , '.']:
		string = string[:list1[0]] +char+string[(list1[0]+1):]
		if "?" not in string:
			if valid_config(string, list2):
				count += 1
		else:
			count += nested_loop(string,list1[1:] , list2)
	return count

def nested_for(count , list, len_list , constraint ):
	global lookup_table
	if len(list) == 1:
		for i in range(list[0]):
			if i > constraint:
				break
			else:
				count += lookup_table[len_list[0]][i]
		return count
	for i in range(list[0]):
		if i > constraint:
			break
		else:
			count = nested_for(count , list[1:] , len_list[1:], constraint -i )
	return count

def nested_loop2(string , list ):
	global lookup_table
	print('gear second')
	sum_of_list = sum(list)
	sublist = string.split(".")
	ranges = []
	len_list = []
	count = 0
	for thing in sublist:
		ranges.append(int((len(thing) +3)/2))
		len_list.append(len(thing))
		for i in range(int((len(thing) +3)/2)):
			if lookup_table[len(thing)][i] == []:
				lookup_table[len(thing)][i] = nested_loop1(thing , [] , [1]*i)
	constraint = sum_of_list
	count = nested_for(count , ranges , len_list , constraint )

	return count

def f(n,k):
	try:
		if lookup_table[n][k] != []:
			return lookup_table[n][k]
	except:
		pass
	if 2*k-1 >n:
		return 0
	if k == 0:
		return 1
	if k == 1:
		return n
	if k==2:
		return int((n-2)*(n-1)/2)

	tot = 0
	for i in range(n-2*(k-1)):
		tot+= f(n-i-2 , k-1)
	if lookup_table[n][k] == []:
		lookup_table[n][k] = tot
	return tot

def final_nest(segments , list):
	if segments==[] and list != []:
		return 0
	elif list == [] and any(["#" in i for i in segments]):
		return 0
	elif list == []:
		return 1
	total = 0
	max_first_seg = 0
	first_sum = 0
	for el in list:
		first_sum += el
		if first_sum <= len(segments[0]):
			max_first_seg +=1
		else:
			break
		first_sum +=1
	if len(segments) == 1:
		min_i = max_first_seg
	else:
		min_i = 0

	if len(segments[0]) == segments[0].count("?"):
		for i in range(max_first_seg + 1):
			sub_total = 1
			val =0
			new_string = segments[0][sum(list[:i]) - i:]
			sub_total *= f(len(new_string) , i)
			if sub_total < 0:
				prin("A")
			sub_total *= final_nest(segments[1:] , list[i:]) #check if right order
			if sub_total < 0:
				prin("A")
			total += sub_total

	else:
		for i in range(min_i , max_first_seg + 1):
			sub_total = 1
			new_string = segments[0]

			sub_total *= nested_loop1(new_string , [], list[:i])
			coc = list[:i]
			if sub_total == 0:
				continue
			if sub_total < 0:
				prin("A")
			seg1 = 	segments[1:]
			cac = list[i:]
			sub_total *= final_nest(segments[1:] , list[i:])
			if sub_total < 0:
				prin("A")
			total += sub_total

	if sum([(len(g)) for g in segments]) > sum(list):
		pass
	return total

import time
prev_time = time.time()
with open('input12.txt') as fin:
	total = 0
	for line in fin:
		nam = 1
		init_input = line.strip("\n").split(" ")[0]
		list = line.strip("\n").split(" ")[1].split(",")
		init_input = init_input.replace(".." , ".").replace(".." , ".").replace(".." , ".").replace("..",".")
		input = init_input
		list = [int(i) for i in list]
		for i in range(4):
			input += "?" + init_input
		list = list*5
		test = input.split(".")
		while "" in test:
			test.remove("")
		while len(test[0]) < list[0] + 1 + list[1] and "#" in test[0]:       #removing sure # from the front
			nam*= nested_loop1(test[0] , [] , [list[0]])
			list.pop(0)
			test.pop(0)
			input = ""
			for part in test:
				input += part + "."
			test = input.split(".")
			while "" in test:
				test.remove("")
			if len(list) == 1:
				break
		if len(list) > 1:

			while	len(test[-1]) < list[-1] + 1 + list[-2] and "#" in test[-1]:   #removing sure # from the back
				nam*= nested_loop1(test[-1] , [] ,  [list[-1]])
				list.pop(-1)
				test.pop(-1)
				input = ""
				for part in test:
					input += part + "."
				test = input.split(".")
				while "" in test:
					test.remove("")
				if len(list) == 1:
					break


		if not "#" in input and "." not in input:
			for i,item in enumerate(list):
				if list[i] > 1:
					input = input[list[i] -1:]
				list[i] = 1


		question_list = []
		question_list2 = [0]
		for i,char in enumerate(input):
			if char == "?":
				question_list.append(i)
				question_list2.append(i+1)

		if "." in input:
			test = input.split(".")
			while "" in test:
				test.remove("")
			nam *= final_nest(test ,  list)
		else:
			nam *= nested_loop1(input , [] , list)

		total += nam

print(total)

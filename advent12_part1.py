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
		return True
	else:
		return False

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

with open('input12.txt') as fin:
	sum = 0
	for line in fin:
		input = line.strip("\n").split(" ")[0]
		list = line.strip("\n").split(" ")[1].split(",")
		question_list = []
		for i,char in enumerate(input):
			if char == "?":
				question_list.append(i)
		list = [int(i) for i in list]
		nam = nested_loop(input , question_list , list)
		sum += nam
	print(sum)

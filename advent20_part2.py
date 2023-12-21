def flip(module , pulse):
	#print(pulse)
	if pulse == 0:
		#print(0)
		module[1] = 1-module[1]
		if module[1] == 0:
			return module , 0
		else:
			return module,1
	else:
		return module , None


def conjunction(module , pulse , recent_source):
	module[3][recent_source] = pulse
	send = 1
	for source in module[3]:
		send *= module[3][source]
	module[1] = (1-send)
	return module , (1-send)

filename = 'input20.txt'
with open(filename) as fin:
	dict = {}
	#print(line)
	conj_modules = []
	for line in fin:
		if "broadcaster" in line:
			dict["broadcaster"] = line.strip("\n").split("> ")[1].split(", ")
		else:
			if line[0] == "&":
				conj_modules.append(line.split(" ->")[0][1:])
			name = line.split(" ->")[0]
			output = line.strip("\n").split("> ")[1].split(", ")
			dict[name[1:]] = [name[0] , 0 , output,{} ]
init_dict = {}
for item in dict:
	init_dict[item] = dict[item].copy()

with open(filename) as fin:
	line = fin.readline()
	for line in fin:
		if "broadcaster" in line:
			output = line.strip("\n").split("> ")[1].split(", ")
			for mod in conj_modules:
				if mod in output:
					dict[mod][2]["broadcaster"] = 0
		else:
			output = line.strip("\n").split("> ")[1].split(", ")
			name = line.split(" ->")[0]
			for mod in conj_modules:
				if mod in output:
					dict[mod][3][name[1:]] = 0

sum_low = 0
sum_high = 0
pulse_queue = []
prev_i = 0
min_dt = 1000000000
min_ts = 1000000000
min_qs = 1000000000
min_js = 1000000000
dt_min = False
ts_mis = False
qs_min = False
js_min = False

for i in range(100000000):
	sum_low +=1
	for target in dict["broadcaster"]:
		sum_low +=1
		pulse_queue.append(["broadcaster" , target , 0])


	while pulse_queue != []:
		new_pulse=pulse_queue.pop(0)
		#print(new_pulse[0] + " sent a " + str(new_pulse[2]) + " pulse to module " + new_pulse[1])
		if dict[new_pulse[1]][0] == "%":
			dict[new_pulse[1]] , newer_pulse = flip(dict[new_pulse[1]] , new_pulse[2])
		else:
			dict[new_pulse[1]] , newer_pulse = conjunction(dict[new_pulse[1]] , new_pulse[2] , new_pulse[0])
			if newer_pulse == 1 and new_pulse[1] == "dt":
				if i+1 < min_dt:
					min_dt = i+1
					dt_min = True
			if newer_pulse == 1 and new_pulse[1] == "ts":
				if i+1 < min_ts:
					min_ts = i+1
					ts_min = True
			if newer_pulse == 1 and new_pulse[1] == "qs":
				if i+1 < min_qs:
					min_qs = i+1
					qs_min = True
			if newer_pulse == 1 and new_pulse[1] == "js":
				if i+1 < min_js:
					min_js = i+1
					js_min = True

		if newer_pulse != None:
			dict[new_pulse[1]][1] = newer_pulse
			for newer_target in dict[new_pulse[1]][2]:
				if newer_pulse == 1:
					sum_high +=1
					if newer_target == "rx":
						pass
						#print(i+1)
						#sys.exit()
				else:
					sum_low += 1
					if newer_target == "rx":
						print(i+1)
						sys.exit()
				if newer_target in dict:
					pulse_queue.append([new_pulse[1]  , newer_target , newer_pulse])

	if 	js_min and 	qs_min and 	ts_min 	and dt_min:
		break

print(min_js*min_qs*min_ts*min_dt)

def evaluate_part(dict , new_dict , starting_point):
    #print("going into " + starting_point)
    for instruction in dict[starting_point]:
        if ":" in instruction:
            command = "new_dict['" + instruction[0]+"']" + instruction.split(":")[0][1:]
            if not eval(command):
                continue
            else:
                if instruction.split(":")[1] == "R" or instruction.split(":")[1] == "A":
                    return instruction.split(":")[1]
                return evaluate_part(dict , new_dict , instruction.split(":")[1])
        else:
            if instruction != "R" and instruction != "A":
                return evaluate_part(dict , new_dict , instruction)
            else:
                return instruction


with open('input19.txt') as fin:
    dict = {}
    sum = 0
    for line in fin:
        if line == "\n":
            break
        name = line.split("{")[0]
        content = line.split("{")[1].split("}")[0]
        dict[name] = content.split(",")

    for line in fin:
        new_dict = {}
        line = line.split("{")[1].split("}")[0]
        things = line.split(",")
        for thing in things:
            new_dict[thing.split("=")[0]] = int(thing.split("=")[1])
        evaluation =  evaluate_part(dict , new_dict , "in")
        if evaluation == "A":
            for param in new_dict:
                sum+=new_dict[param]
    #    print("part is "+ evaluation)
    print(sum)

def evaluate_range(dict , new_dict , starting_point , sum):
    for instruction in dict[starting_point]:
        if ":" in instruction:
            split_val = int(instruction.split(":")[0][2:])
            if "<" in instruction:
                split_val -=1
            if split_val in new_dict[instruction[0]] and split_val+1 in new_dict[instruction[0]]:
                start = new_dict[instruction[0]].start
                end = new_dict[instruction[0]].stop
                dict_copy = new_dict.copy()
                if "<" in instruction:
                    dict_copy[instruction[0]] = range(start , split_val +1)
                    new_dict[instruction[0]] = range(split_val +1 , end)
                else:
                    dict_copy[instruction[0]] = range(split_val +1 , end)
                    new_dict[instruction[0]] = range(start , split_val +1)
                if instruction.split(":")[1] == "A":
                    temp_sum = 1
                    for things in dict_copy:
                        temp_sum*=len(dict_copy[things])
                    sum += temp_sum
                elif instruction.split(":")[1] == "R":
                    continue
                else:
                    sum = evaluate_range(dict , dict_copy , instruction.split(":")[1], sum)
            elif split_val < new_dict[instruction[0]].start:
                if "<" in instruction:
                    continue
                else:
                        sum = evaluate_range(dict , new_dict  , instruction.split(":")[1] , sum)
            elif split_val + 1 >= new_dict[instruction[0]].stop:
                if ">" in instruction:
                    continue
                else:
                    sum = evaluate_range(dict , new_dict , instruction.split(":")[1] , sum)
        else:
            if instruction != "R" and instruction != "A":
                return evaluate_range(dict , new_dict , instruction , sum)
            elif instruction == "R":
                return sum
            elif instruction == "A":
                temp_sum = 1
                for things in new_dict:
                    temp_sum*=len(new_dict[things])
                sum += temp_sum
                return sum

with open('input19.txt') as fin:
    dict = {}
    sum = 0
    important_x =[1]
    important_m=[1]
    important_a=[1]
    important_s=[1]
    for line in fin:
        if line == "\n":
            break
        name = line.split("{")[0]
        content = line.split("{")[1].split("}")[0]
        dict[name] = content.split(",")
    x = range(1, 4001)
    m = range(1, 4001)
    a = range(1, 4001)
    s = range(1, 4001)
    new_dict = {"x": x , "m": m , "a": a , "s": s}

    sum =  evaluate_range(dict , new_dict , "in" , sum)
    print(sum)

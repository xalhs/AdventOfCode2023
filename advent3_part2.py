with open('input3.txt') as fin:    ####”
    sum = 0
    sum1 = 0
    thing = []
    i=0
    for line in fin:
        thing.append(list(line[:-1]))

    for i,row in enumerate(thing):
        for j,char in enumerate(row):
            num_count = 0
            temp_mult = 1
            if char=="*":
                if thing[i-1][j-1].isdigit():
                    num_count+=1
                    starting_index = j-1
                    while thing[i-1][starting_index].isdigit() and starting_index >=0:
                        starting_index -= 1
                    starting_index +=1
                    num = list(str(thing[i-1][starting_index]))
                    thing[i-1][starting_index] = "."
                    starting_index +=1
                    while thing[i-1][starting_index].isdigit() and  starting_index < len(thing[i-1]):
                        num.append(str(thing[i-1][starting_index]))
                        thing[i-1][starting_index] = "."
                        starting_index+= 1
                    temp_mult *= int("".join(num))
                if thing[i-1][j].isdigit():
                    num_count+=1
                    starting_index = j
                    while thing[i-1][starting_index].isdigit() and starting_index >=0:
                        starting_index -= 1
                    starting_index +=1
                    num = list(str(thing[i-1][starting_index]))
                    thing[i-1][starting_index] = "."
                    starting_index +=1
                    while thing[i-1][starting_index].isdigit() and  starting_index < len(thing[i-1]):
                        num.append(str(thing[i-1][starting_index]))
                        thing[i-1][starting_index] = "."
                        starting_index+= 1
                    temp_mult *= int("".join(num))
                if thing[i-1][j+1].isdigit():
                    num_count+=1
                    starting_index = j+1
                    while thing[i-1][starting_index].isdigit() and starting_index >=0:
                        starting_index -= 1
                    starting_index +=1
                    num = list(str(thing[i-1][starting_index]))
                    thing[i-1][starting_index] = "."
                    starting_index +=1
                    while thing[i-1][starting_index].isdigit() and starting_index < len(thing[i-1]):
                        num.append(str(thing[i-1][starting_index]))
                        thing[i-1][starting_index] = "."
                        starting_index+= 1
                    temp_mult *= int("".join(num))

                if thing[i][j-1].isdigit():
                    num_count+=1
                    starting_index = j-1
                    while thing[i][starting_index].isdigit() and starting_index >=0:
                        starting_index -= 1
                    starting_index +=1
                    num = list(str(thing[i][starting_index]))
                    thing[i][starting_index] = "."
                    starting_index +=1
                    while thing[i][starting_index].isdigit() and starting_index < len(thing[i]):
                        num.append(str(thing[i][starting_index]))
                        thing[i][starting_index] = "."
                        starting_index+= 1
                    temp_mult *= int("".join(num))

                if thing[i][j].isdigit():
                    num_count+=1
                    starting_index = j
                    while thing[i][starting_index].isdigit() and starting_index >=0:
                        starting_index -= 1
                    starting_index +=1
                    num = list(str(thing[i][starting_index]))
                    thing[i][starting_index] = "."
                    starting_index +=1
                    while thing[i][starting_index].isdigit() and starting_index < len(thing[i]):
                        num.append(str(thing[i][starting_index]))
                        thing[i][starting_index] = "."
                        starting_index+= 1
                    temp_mult *= int("".join(num))

                if thing[i][j+1].isdigit():
                    num_count+=1
                    starting_index = j+1
                    while thing[i][starting_index].isdigit() and starting_index >=0:
                        starting_index -= 1
                    starting_index +=1
                    num = list(str(thing[i][starting_index]))
                    thing[i][starting_index] = "."
                    starting_index +=1
                    while starting_index < len(thing[i]) and thing[i][starting_index].isdigit():
                        num.append(str(thing[i][starting_index]))
                        thing[i][starting_index] = "."
                        starting_index+= 1

                    temp_mult *= int("".join(num))

                if thing[i+1][j-1].isdigit():
                    num_count+=1
                    starting_index = j-1
                    while thing[i+1][starting_index].isdigit() and starting_index >=0:
                        starting_index -= 1
                    starting_index +=1
                    num = list(str(thing[i+1][starting_index]))
                    thing[i+1][starting_index] = "."
                    starting_index +=1
                    while thing[i+1][starting_index].isdigit() and  starting_index < len(thing[i+1]):
                        num.append(str(thing[i+1][starting_index]))
                        thing[i+1][starting_index] = "."
                        starting_index+= 1
                    temp_mult *= int("".join(num))
                if thing[i+1][j].isdigit():
                    num_count+=1
                    starting_index = j
                    while thing[i+1][starting_index].isdigit() and starting_index >=0:
                        starting_index -= 1
                    starting_index +=1
                    num = list(str(thing[i+1][starting_index]))
                    thing[i+1][starting_index] = "."
                    starting_index +=1
                    while thing[i+1][starting_index].isdigit() and starting_index < len(thing[i+1]):
                        num.append(str(thing[i+1][starting_index]))
                        thing[i+1][starting_index] = "."
                        starting_index+= 1
                    temp_mult *= int("".join(num))

                if thing[i+1][j+1].isdigit():
                    num_count+=1
                    starting_index = j+1
                    while thing[i+1][starting_index].isdigit() and starting_index >=0:
                        starting_index -= 1
                    starting_index +=1
                    num = list(str(thing[i+1][starting_index]))
                    thing[i+1][starting_index] = "."
                    starting_index +=1
                    while thing[i+1][starting_index].isdigit() and starting_index < len(thing[i+1]):
                        num.append(str(thing[i+1][starting_index]))
                        thing[i+1][starting_index] = "."
                        starting_index+= 1
                    temp_mult *= int("".join(num))
            if num_count ==2:
                sum += temp_mult
                
    print(sum)

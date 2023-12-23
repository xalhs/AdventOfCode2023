def add(list1, list2):
    list3 = []
    for i,el in enumerate(list1):
        list3.append(list1[i] + list2[i])

    return list3

def move(position , dir ):

    dire= {"D" : [1, 0] , "U":[-1,0] , "R": [0,1] , "L":[0,-1]}
    position = add(position, dire[dir] )
    return position

def process(position , prev_dir ,pattern):
    count = 0
    new_pos_list = []
    came_from = None
    if prev_dir== "D":
        came_from = "U"
    elif prev_dir == "U":
        came_from = "D"
    elif prev_dir == "L":
        came_from = "R"
    elif prev_dir == "R":
        came_from = "L"
    count_list = []
    new_pattern = pattern.copy()
    dire= {"D" : [1, 0] , "U":[-1,0] , "R": [0,1] , "L":[0,-1]}
    dir_list = []
    for dir in dire:
        if dir != came_from:
            new_pos = move(position , dir )
            if new_pos[0] >= len(pattern) or pattern[new_pos[0]][new_pos[1]] == "#":
                continue
            elif pattern[new_pos[0]][new_pos[1]] != ".":
                if  pattern[new_pos[0]][new_pos[1]] == '>' and dir == "L":
                    continue
                elif  pattern[new_pos[0]][new_pos[1]] == '<' and dir == "R":
                    continue
                elif  pattern[new_pos[0]][new_pos[1]] == '^' and dir == "D":
                    continue
                elif  pattern[new_pos[0]][new_pos[1]] == 'v' and dir == "U":
                    continue
            if new_pos[0] == len(pattern)-1:
                return 1
            dir_list.append(dir)
            new_pattern[position[0]] = pattern[position[0]][:position[1]] + "#" +  pattern[position[0]][position[1]+ 1:]
            new_pos_list.append(new_pos)
    max_count = 0
    while len(new_pos_list) == 1:
        new_pos =  new_pos_list[0]
        new_pos_list = []
        position = new_pos
        count += 1
        prev_dir = dir_list[0]
        if prev_dir== "D":
            came_from = "U"
        elif prev_dir == "U":
            came_from = "D"
        elif prev_dir == "L":
            came_from = "R"
        elif prev_dir == "R":
            came_from = "L"
        new_pos_list = []
        count_list = []
        dir_list = []
        for dir in dire:
            if dir != came_from:
                new_pos = move(position , dir )
                if new_pos[0] >= len(pattern) or new_pos[0] < 0 or new_pattern[new_pos[0]][new_pos[1]] == "#":
                    continue
                elif new_pattern[new_pos[0]][new_pos[1]] != ".":
                    if  new_pattern[new_pos[0]][new_pos[1]] == '>' and dir == "L":
                        continue
                    elif  new_pattern[new_pos[0]][new_pos[1]] == '<' and dir == "R":
                        continue
                    elif  new_pattern[new_pos[0]][new_pos[1]] == '^' and dir == "D":
                        continue
                    elif  new_pattern[new_pos[0]][new_pos[1]] == 'v' and dir == "U":
                        continue
                if new_pos[0] == len(new_pattern)-1:
                    return count+1

                dir_list.append(dir)
                new_pattern[position[0]] = new_pattern[position[0]][:position[1]] + "#" +  new_pattern[position[0]][position[1]+ 1:]
                new_pos_list.append(new_pos)
    count_list = []
    for i,new_pos in enumerate(new_pos_list):
        count_list.append( process(new_pos , dir_list[i] , new_pattern ))
    max_pos = 0
    for i,new_count in enumerate(count_list):
        if new_count > max_count:
            max_pos = new_pos_list[i]
            max_count = new_count

    return count+max_count+1

with open("input23.txt")  as fin:
    pattern = []
    starting_point = []
    for i,line in enumerate(fin):
            pattern.append(line.strip("\n"))

    starting_point = [0 , pattern[0].find(".")]

print(process(starting_point , None , pattern))

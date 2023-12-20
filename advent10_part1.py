def add_lists (list1 , list2):
    list3 = []
    for i,el in enumerate(list1):
        list3.append(list1[i] + list2[i])
    return list3

def moving(current_pos , big_map, came_from):
    if big_map[current_pos[0]][current_pos[1]] == "|":
        current_pos = add_lists(current_pos , dire[I[came_from]])
        came_from = I[came_from]
    elif big_map[current_pos[0]][current_pos[1]] == "F":
        current_pos = add_lists(current_pos , dire[F[came_from]])
        came_from = F[came_from]
    elif big_map[current_pos[0]][current_pos[1]] == "7":
        current_pos = add_lists(current_pos , dire[seven[came_from]])
        came_from = seven[came_from]
    elif big_map[current_pos[0]][current_pos[1]] == "-":
        current_pos = add_lists(current_pos , dire[dash[came_from]])
        came_from = dash[came_from]
    elif big_map[current_pos[0]][current_pos[1]] == "L":
        current_pos = add_lists(current_pos , dire[L[came_from]])
        came_from = L[came_from]
    elif big_map[current_pos[0]][current_pos[1]] == "J":
        current_pos = add_lists(current_pos , dire[J[came_from]])
        came_from = J[came_from]
    if big_map[current_pos[0]][current_pos[1]] == ".":
        current_pos = add_lists(current_pos , dire[dot[came_from]])
        came_from = dot[came_from]
    return current_pos , came_from





with open('input10.txt') as fin:
    big_map =[[]]
    starting_pos = 0
    I = {"down" : "down" , "up": "up" }
    dash = {"left": "left" , "right": "right"}
    L = {"up":"left" , "right":"down"}
    J = {"up":"right" , "left":"down"}
    seven = {"left":"up" , "down":"right"}
    F = {"right": "up", "down": "left" }
    dot = {}
    dire= {"down" : [-1, 0] , "up":[1,0] , "right": [0,-1] , "left":[0,1]}

    for i,line in enumerate(fin):
        if "S" in line:
            starting_pos = [i , line.find("S")]
        big_map[-1] += line.rstrip("\n")
        big_map.append([])

    current_pos = [i for i in starting_pos]
    steps = 0
    try:
        current_pos[0] -=1
        came_from = "down"
        while current_pos != starting_pos:
            current_pos , came_from = moving(current_pos , big_map, came_from)
            steps +=1
        print(int((steps+1)/2))
    except:
        current_pos = [i for i in starting_pos]
        pass
    print("another direction")
    steps = 0
    try:
        current_pos[1] -=1
        came_from = "right"
        while current_pos != starting_pos:
        #    print(came_from)
        #    print(big_map[current_pos[0]][current_pos[1]])
            current_pos , came_from = moving(current_pos , big_map, came_from)
            steps +=1
        print(int((steps+1)/2))
    except:
        current_pos = [i for i in starting_pos]
        pass
    print("another dir")
    steps = 0
    try:
        current_pos[0] +=1
        came_from = "up"
        while current_pos != starting_pos:
            current_pos , came_from = moving(current_pos , big_map, came_from)
            steps +=1
        print(int((steps+1)/2))
    except:
        current_pos = [i for i in starting_pos]
        pass
    print("another dir")
    steps = 0
    try:
        current_pos[1] +=1
        came_from = "left"
        while current_pos != starting_pos:
            current_pos , came_from = moving(current_pos , big_map, came_from)
            steps +=1
        print(int((steps+1)/2))
    except:
        current_pos = [i for i in starting_pos]
        pass



#    print(big_map)

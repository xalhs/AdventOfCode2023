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
    return current_pos , came_from

with open('input10.txt') as fin:
    big_map =[]
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
        big_map.append([])
        if "S" in line:
            starting_pos = [i , line.find("S")]
        big_map[-1] += line.rstrip("\n")


    current_pos = [i for i in starting_pos]
    steps = 0
    loop = {}
    current_pos[1] -=1
    came_from = "right"
    loop[tuple(current_pos)] = came_from
    #loop.append(current_pos)
    right = 0
    left = len(big_map[0])-1
    top  = len(big_map)-1
    bottom  = 0
    first_came_from = came_from
    while current_pos != starting_pos:
        prev_came_from = came_from
        prev_pos = [i for i in current_pos]
        current_pos , came_from = moving(current_pos , big_map, came_from)
        if current_pos[0] < top:
            top = current_pos[0]
        if current_pos[1] > right:
            right = current_pos[1]
        if current_pos[0] > bottom:
            bottom = current_pos[0]
        if  current_pos[1] < left:
            left = current_pos[1]
        steps +=1
        if came_from == "up" or came_from == "down":
            loop[tuple(prev_pos)] = "half-"+ prev_came_from
        else:
            if prev_came_from == "up" or prev_came_from == "down":
                loop[tuple(prev_pos)] = "half-" + came_from
            else:
                loop[tuple(prev_pos)] = came_from
    if first_came_from == "up" or first_came_from == "down":
        loop[tuple(starting_pos)] = "half-"+ came_from
    else:
        if came_from == "up" or came_from == "down":
            loop[tuple(starting_pos)] = "half-" + first_came_from
        else:
            loop[tuple(starting_pos)] = first_came_from

    enclosed = 0
    for i in range(top , bottom+1):
        for j in range(left , right+1):
            if not tuple([i,j]) in loop:
            #    print("checking pos " + str(tuple([i,j])))
                leftness = 0
                pos = i
                while pos >= top-1:
                    if tuple([pos , j]) in loop:
                        if loop[tuple([pos , j])] == "left":
                            leftness += 1
                        elif loop[tuple([pos , j])] == "right":
                            leftness -=1
                        elif  loop[tuple([pos , j])] == "half-right":
                            leftness -=0.5
                        elif  loop[tuple([pos , j])] == "half-left":
                            leftness +=0.5
                    pos -=1
                leftness = int(leftness)
                if leftness != 0:
                #    print("position " + str(tuple([i,j])) + " is enclosed")
                    enclosed +=1
    print(enclosed)


        #loop.append(current_pos)

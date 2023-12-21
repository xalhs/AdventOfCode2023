def add_lists(list1, list2):
    list3 = []
    for i,el in enumerate(list1):
        list3.append(list1[i] + list2[i])
    return list3

with open("input21.txt") as fin:
    pattern  = []
    starting_point = []
    for i,line in enumerate(fin):
        pattern.append(line.strip("\n"))
        if "S" in line:
            starting_point = [i , line.find("S")]

    direct = [[1,0]  , [0,1] , [-1,0] , [0,-1]]
    points_visited = [[starting_point] , []]
    new_points = [starting_point]

    for i in range(64):
        current_points = [x.copy() for x in new_points]
        new_points = []
        for dir in direct:
            for point in current_points:
                new_loc = add_lists(dir, point)
                if (not new_loc in points_visited[(i+1)%2]) and  pattern[new_loc[0]][new_loc[1]] != "#":
                    if i%2 != 0:
                        pattern[new_loc[0]] = pattern[new_loc[0]][:new_loc[1]] + "O" + pattern[new_loc[0]][new_loc[1]+1:]
                    points_visited[(i+1)%2].append(new_loc)
                    new_points.append(new_loc)

    print(len(points_visited[0]))

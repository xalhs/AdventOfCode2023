def add(list1, list2):
    list3 = []
    for i,el in enumerate(list1):
        list3.append(list1[i] + list2[i])

    return list3

def move(position , dir ):
    dire= {"D" : [1, 0] , "U":[-1,0] , "R": [0,1] , "L":[0,-1]}
    position = add(position, dire[dir] )
    return position

def mappen(position , prev_intersect, prev_dir,  pattern , steps = 0):
    global final_point
    starting_intersect = prev_intersect
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
    dire= {"D" : [1, 0] , "U":[-1,0] , "R": [0,1] , "L":[0,-1]}
    dir_list = []
    for dir in dire:
        if dir != came_from:
            new_pos = move(position , dir )
            if new_pos[0] >= len(pattern) or pattern[new_pos[0]][new_pos[1]] == "#":
                continue
            if new_pos[0] == len(pattern)-1:
                final_point = new_pos
                paths[ (min( intersections_inverse[tuple(starting_intersect)]  , intersections_inverse[tuple(new_pos)]) , max( intersections_inverse[tuple(starting_intersect)]  , intersections_inverse[tuple(new_pos)]) ) ] = steps+1
                return
            dir_list.append(dir)
            new_pos_list.append(new_pos)


    max_count = 0
    if len(new_pos_list) == 0:
        return
    while len(new_pos_list) == 1:
        new_pos =  new_pos_list[0]
        new_pos_list = []
        steps += 1
        position = new_pos
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
                if new_pos[0] >= len(pattern) or new_pos[0] < 0 or pattern[new_pos[0]][new_pos[1]] == "#":
                    continue
                if new_pos[0] == len(pattern)-1:
                    final_point = new_pos
                    intersections_inverse[tuple(new_pos)] = list(intersections)[-1] +1
                    intersections[list(intersections)[-1] +1]  = new_pos
                    paths[ (min( intersections_inverse[tuple(starting_intersect)]  , intersections_inverse[tuple(new_pos)]) , max( intersections_inverse[tuple(starting_intersect)]  , intersections_inverse[tuple(new_pos)]) ) ] = steps +1
                    return

                dir_list.append(dir)
                new_pos_list.append(new_pos)

    if len(new_pos_list) > 1 and not tuple(position) in intersections_inverse:
        intersections_inverse[tuple(position)] = list(intersections)[-1] +1
        intersections[list(intersections)[-1] +1]  = position
        start = min( intersections_inverse[tuple(starting_intersect)]  , intersections_inverse[tuple(position)])
        end = max( intersections_inverse[tuple(starting_intersect)]  , intersections_inverse[tuple(position)])
        if (start,end) in paths:
            paths[(start,end)]  = max(steps , paths[(start,end)] )
        else:
            paths[(start,end)]  = steps
    elif len(new_pos_list) > 1 and tuple(position) in intersections_inverse:
        start = min( intersections_inverse[tuple(starting_intersect)]  , intersections_inverse[tuple(position)])
        end = max( intersections_inverse[tuple(starting_intersect)]  , intersections_inverse[tuple(position)])
        if (start,end) in paths:
            paths[(start,end)]  = max(steps , paths[(start,end)] )
        else:
            paths[(start,end)]  = steps
        return
    if len(new_pos_list) == 0:
        return -len(pattern)*len(pattern[0])
    for i,new_pos in enumerate(new_pos_list):
        mappen(new_pos, position , dir_list[i]  , pattern  , steps = 1)
    return

def max_path(current_int , already_visited  ):
    if current_int == second_to_last_int:
        return paths[(second_to_last_int ,final_int )]
    current_max = 0
    for new_int in intersection_connections[current_int]:
        if not new_int in already_visited:
            new_already_visited = already_visited.copy()
            new_already_visited.append(new_int)
            path_to_end =  max_path(new_int , new_already_visited  )
            start = min(new_int , current_int)
            end = max(new_int , current_int)
            path_to_end += paths[(start , end)]
            if path_to_end > current_max:
                current_max = path_to_end

    return current_max


global intersections
global intersections_inverse
global paths
global list_of_intersections
global final_point
final_point = [-1,-1]
intersections = {}
intersections_inverse = {}
paths = {}
list_of_intersections = []
with open("input23.txt")  as fin:
    pattern = []
    starting_point = []
    for i,line in enumerate(fin):
            pattern.append(line.strip("\n").replace(">" , ".").replace("v" , "."))
    starting_point = [0 , pattern[0].find(".")]
    intersections[0] = starting_point
    intersections_inverse[tuple(starting_point)] = 0


    mappen(starting_point ,starting_point,  None , pattern)

global intersection_connections
intersection_connections = {}
for i, inter1 in enumerate(intersections):
    for j in range( i + 1, len(intersections)):
        if (i,j) in paths:
            if not i in intersection_connections:
                intersection_connections[i]  = [j]
            else:
                intersection_connections[i].append(j)
            if not j in intersection_connections:
                intersection_connections[j]  = [i]
            else:
                intersection_connections[j].append(i)
already_visited = [0]
current_int = 0
global final_int
final_int = intersections_inverse[tuple(final_point)]
global second_to_last_int
second_to_last_int = intersection_connections[final_int][0]
steps = 0
print(max_path(current_int , already_visited  ))

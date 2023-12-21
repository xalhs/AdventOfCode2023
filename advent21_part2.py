def add_lists(list1, list2):
    list3 = []
    for i,el in enumerate(list1):
        list3.append(list1[i] + list2[i])
    return list3

def do_the_process(n , pattern , starting_point , confined = False):
    direct = [[1,0]  , [0,1] , [-1,0] , [0,-1]]
    points_visited = [[starting_point] , []]
    new_points = [starting_point]
    for i in range(n):
        current_points = [x.copy() for x in new_points]
        new_points = []
        for dir in direct:
            for point in current_points:
                new_loc = add_lists(dir, point)
                if confined and (new_loc[0]%len(pattern)!=new_loc[0] or new_loc[1]%len(pattern[0])!=new_loc[1])  :
                    continue
                if (not new_loc in points_visited[(i+1)%2]) and  pattern[new_loc[0]%len(pattern)][new_loc[1]%len(pattern[0])] != "#":
                    points_visited[(i+1)%2].append(new_loc)
                    new_points.append(new_loc)
    return len(points_visited[n%2])


with open("input21.txt") as fin:
    pattern  = []
    starting_point = []
    count =0
    for i,line in enumerate(fin):
        pattern.append(line.strip("\n"))
        if "S" in line:
            starting_point = [i , line.find("S")]

    direct = [[1,0]  , [0,1] , [-1,0] , [0,-1]]
    points_visited = [[starting_point] , []]
    new_points = [starting_point]
    even_diamond = do_the_process(64 , pattern , starting_point)
    odd_diamond = do_the_process(65 , pattern , starting_point)
    even_count = do_the_process(150 , pattern , starting_point , True)
    odd_count = do_the_process(151 , pattern , starting_point , True)

    ratio = int(26501365/131) #=202300
    if ratio%2 ==0:
        print(even_count*ratio**2+odd_count*(ratio -1)**2 + 2*odd_count +2*odd_diamond+(ratio)*(even_count - even_diamond) + (ratio - 1)*(3*odd_count + odd_diamond))
    else:
        print(odd_count*ratio**2+even_count*(ratio -1)**2 + 2*even_count +2*even_diamond+ratio*(odd_count - odd_diamond) + (ratio - 1)*(3*even_count + even_diamond))

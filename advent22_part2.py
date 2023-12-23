def what_will_fall(z_level , brick_stability , brick_stability2 , what_has_fallen , bricks_from_bottom_to_top):
    if not z_level in bricks_from_bottom_to_top or z[z_level] == []:
        return what_has_fallen
    for brick in bricks_from_bottom_to_top[z_level]:
        if(all(x in what_has_fallen for x in brick_stability[brick])):
            what_has_fallen.append(brick)
    what_has_fallen = what_will_fall(z_level+1 , brick_stability , brick_stability2 , what_has_fallen , bricks_from_bottom_to_top)
    return what_has_fallen

with open("input22.txt") as fin:
    z = {}
    bricks = {}
    coords = {}
    brick_z = {}
    count =0
    brick_count = -1
    for line in fin:
        brick_count += 1
        line = line.strip("\n")
        [start , end] = line.split("~")
        start = start.split(",")
        start = [int(i) for i in start]
        end = end.split(",")
        end = [int(i) for i in end]
        bricks[brick_count] = []
        brick_z[brick_count] = {}
        for i in range(start[0] , end[0] + 1):
            for j in range(start[1] , end[1] + 1):
                for k in range(start[2] , end[2] + 1):
                    if not k in z:
                        z[k] = []
                    if not k in brick_z[brick_count]:
                        brick_z[brick_count][k] = []
                    z[k].append([brick_count , i , j])
                    bricks[brick_count].append((i,j,k))
                    coords[(i,j,k)] = brick_count
                    brick_z[brick_count][k].append([i,j])

z_list = [zee for zee in z]
brick_stability = {} #key stabilized by item
brick_stability2 = {} # key stabilizes item
z_list.sort()
for k in z_list:

    if k == 1:
        continue
    bricks_to_fall =[]
    bricks_in_zk = []
    for things in z[k]:
        if not things[0] in bricks_in_zk:
            bricks_in_zk.append(things[0])
    for brick in bricks_in_zk:
        brick = [brick]
        goes_down = 0
        for l in range(1,k):
            can_go_down = True
            for base in brick_z[brick[0]][k]:
                if (base[0] , base[1] , k-l) in coords:
                    can_go_down = False
                    if coords[(base[0] , base[1] , k-l) ] != brick[0]:
                        if not brick[0] in brick_stability:
                            brick_stability[brick[0]] = [coords[(base[0] , base[1] , k-l) ] ]
                        elif coords[(base[0] , base[1] , k-l) ]  in  brick_stability[brick[0]]:
                            pass
                        else:
                            brick_stability[brick[0]].append(coords[(base[0] , base[1] , k-l) ] )
                        if not coords[(base[0] , base[1] , k-l) ]  in brick_stability2:
                            brick_stability2[coords[(base[0] , base[1] , k-l) ] ] = [brick[0]]
                        elif brick[0]  in  brick_stability2[coords[(base[0] , base[1] , k-l) ] ]:
                            pass
                        else:
                            brick_stability2[coords[(base[0] , base[1] , k-l) ] ].append(brick[0])
            if can_go_down == False:
                l -=1
                break
        if l != 0:
            bricks_to_fall.append([brick[0] , l])
    for brick in bricks_to_fall:
        brick_z_list = []
        for zet in brick_z[brick[0]]:
            if not zet-brick[1] in z:
                z[zet-brick[1]] = []
            loc_list = []
            for loc in z[zet]:

                if loc[0] == brick[0]:
                    loc_list.append(loc)
            for loc in loc_list:
                z[zet - brick[1]].append(loc)
                z[zet].remove(loc)
            brick_z_list.append(zet)

        for item in brick_z_list:
            brick_z[brick[0]][item - brick[1]] = brick_z[brick[0]][item]
            del brick_z[brick[0]][item]
        new_brick_loc = []
        for i,loc in enumerate(bricks[brick[0]]):
            del coords[loc]
            coords[(list(loc)[0] ,list(loc)[1] , list(loc)[2] - brick[1])] = brick[0]
            new_brick_loc.append(tuple([list(loc)[0] ,list(loc)[1] , list(loc)[2] - brick[1]]))
        bricks[brick[0]] = new_brick_loc

bricks_from_bottom_to_top = {}
sorting_dict = []
for brick in brick_z:
    if not min(brick_z[brick]) in bricks_from_bottom_to_top:
         bricks_from_bottom_to_top[min(brick_z[brick])] = [brick]
    else:
            bricks_from_bottom_to_top[min(brick_z[brick])].append(brick)
    sorting_dict.append(min(brick_z[brick]))
sorting_dict.sort()
sorting_dict = list(dict.fromkeys(sorting_dict))
for i in range(1 , max(bricks_from_bottom_to_top)):  #very important part, took me hours to figure out what was wrong
    if not i in bricks_from_bottom_to_top:           #if not done then the algorithm will skip some bricks that would fall   
        bricks_from_bottom_to_top[i] = []

total = 0
for height in sorting_dict:
    for brick in bricks_from_bottom_to_top[height]:
        if brick in brick_stability2 or True:
            fall = 0
            what_has_fallen = [brick]
            height1 = min(brick_z[brick])
            what_has_fallen  = what_will_fall(height1 +1, brick_stability , brick_stability2  , what_has_fallen , bricks_from_bottom_to_top)
            fall = len(what_has_fallen)-1
            total += fall
print(total)

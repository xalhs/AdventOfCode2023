with open("input22.txt") as fin:
    x = {}
    y = {}
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
            if not i in x:
                x[i] = []
            for j in range(start[1] , end[1] + 1):
                if not j in y:
                    y[j] = []
                for k in range(start[2] , end[2] + 1):
                    if not k in z:
                        z[k] = []
                    if not k in brick_z[brick_count]:
                        brick_z[brick_count][k] = []
                    z[k].append([brick_count , i , j])
                    y[j].append([brick_count , i , k])
                    x[i].append([brick_count , j , k])
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
        if list(bricks[1432][0])[2]  == 241:
            pass
        bricks[brick[0]] = new_brick_loc

total = 0
for brick in bricks:
    if not brick in brick_stability2:
        total +=1
    else:
        can_be_int = True
        for other_brick in brick_stability2[brick]:
            if brick_stability[other_brick] == [brick]:

                can_be_int = False
                break
        if can_be_int:
            total+=1
print(total)

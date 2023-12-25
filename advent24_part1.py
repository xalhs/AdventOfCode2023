with open("input24.txt") as fin:
    pos = {}
    vel = {}
    count = 0
    for i,line in enumerate(fin):
        [posi , velo] = line.strip("\n").split(" @ ")
        pos[i] = [int(j) for j in posi.split(", ")]
        vel[i] = [int(j) for j in velo.split(", ")]

    for i in pos:
        for j in range(i):
            dif_pos = [pos[i][0] - pos[j][0] , pos[i][1] - pos[j][1]  ]
            dif_vel = [vel[i][0] - vel[j][0] , vel[i][1] - vel[j][1]  ]
            D = -vel[i][0]*vel[j][1]+vel[j][0]*vel[i][1]
            if D == 0:
                continue
            D_x = -vel[i][1]*(pos[j][1]*vel[j][0]- pos[j][0]*vel[j][1]) + vel[j][1]*(pos[i][1]*vel[i][0]- pos[i][0]*vel[i][1])
            D_y = vel[i][0]*(pos[j][1]*vel[j][0]- pos[j][0]*vel[j][1]) - vel[j][0]*(pos[i][1]*vel[i][0]- pos[i][0]*vel[i][1])
            col_x = D_y/D
            col_y = -D_x/D
            if (col_x- pos[i][0])*vel[i][0] < 0 or  (col_x- pos[j][0])*vel[j][0] < 0:
                continue
            if 200000000000000 <= col_x and   col_x <= 400000000000000 and 200000000000000 <= col_y and   col_y <= 400000000000000:
                count +=1

    print(count)

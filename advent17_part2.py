def path_conv(points_list):
    new_points = []
    for point in points_list:
        new_points.append([ point[1] , length - point[0] ])

    return new_points

def path_inv_conv(points_list):
    new_points = []
    for point in points_list:
        new_points.append([length - point[1] , point[0]])

    return new_points

def add_lists (list1 , list2):
    list3 = []
    for i,el in enumerate(list1):
        list3.append(list1[i] + list2[i])
    return list3

def subtract_lists(list1 , list2):
    list3 = []
    for i,el in enumerate(list1):
        list3.append(list1[i] - list2[i])
    return list3

def multiply_list(list1 , number):
    list2 = []
    for i,el in enumerate(list1):
        list2.append(list1[i]*number)
    return list2

def negative_list(list1):
    list2 = []
    for el in list1:
        list2.append(-el)
    return list2

global current_pos
dire= {"D" : [1, 0] , "U":[-1,0] , "R": [0,1] , "L":[0,-1]}
opposite_dir ={"D" : "U" , "U":"D" , "R":  "L" , "L":"R"}

def is_coord_in(coord):
    if coord[0] < len(pattern) and coord[1] < len(pattern) and coord[0] >=0 and coord[1] >= 0:
        return True
    else:
        return False

def map_altering(pattern1 , condition = False):
    basis = {"L" : [10000 , 10000, 10000, 10000, 10000, 10000 , 10000, 10000, 10000, 10000] , "R" : [10000 , 10000, 10000, 10000, 10000, 10000 , 10000, 10000, 10000, 10000], "U" : [10000 , 10000, 10000, 10000, 10000, 10000 , 10000, 10000, 10000, 10000] , "D" : [10000 , 10000, 10000, 10000, 10000, 10000 , 10000, 10000, 10000, 10000] }
    if condition:
        tracker =[[pattern1[i][j].copy() for j in range(len(pattern1))] for i in range(len(pattern1)) ]
    else:
        tracker = [ [  copy.deepcopy(basis)  for i in range(len(pattern1))] for j in range(len(pattern1)) ]

    for i in range(2*len(pattern1) -1):
        for j in range(max(i+1-len(pattern1) , 0) , min(i+1 , len(pattern1))):
            #if i-j<140, i-j>=0
            koeak = tracker[j][i-j]["L"][0]
            if i ==0 and j ==0:
                zero_val = int(pattern[0][0])
                zero_val = 0
                tracker[j][i-j] = {"L" : [zero_val , zero_val, zero_val, zero_val, zero_val,zero_val , zero_val, zero_val, zero_val, zero_val] , "R" : [zero_val , zero_val, zero_val, zero_val, zero_val,zero_val , zero_val, zero_val, zero_val, zero_val], "U" : [zero_val , zero_val, zero_val, zero_val, zero_val,zero_val , zero_val, zero_val, zero_val, zero_val] , "D" : [zero_val , zero_val, zero_val, zero_val, zero_val,zero_val , zero_val, zero_val, zero_val, zero_val]}
                continue
            for direc in basis: #direction to take the value from
                for k , val in enumerate(basis[direc]):
                    if tracker[0][1]["U"][0] != 10000:
                        sys.exit()
                    if k ==0:
                        mini =10000
                        for direct in basis:
                            if direc == direct or direct == opposite_dir[direc]:
                                continue
                            else:
                                other_dir = add_lists( [j , i-j] , dire[direc])
                                if is_coord_in(other_dir):
                                    for neu_val in  tracker[other_dir[0]][other_dir[1]][direct][3:]:
                                        if neu_val < mini:
                                            mini = neu_val
                        #print(k)
                        if mini + int(pattern[j][i-j]) < tracker[j][i-j][direc][k]:
                            tracker[j][i-j][direc][k] = mini + int(pattern[j][i-j])
		  	
                    else:
                        other_dir = add_lists( [j , i-j] , dire[direc])
                        if is_coord_in(other_dir):
                            if tracker[other_dir[0]][other_dir[1]][direc][k-1] + int(pattern[j][i-j]) < tracker[j][i-j][direc][k]:
                                tracker[j][i-j][direc][k] = tracker[other_dir[0]][other_dir[1]][direc][k-1] + int(pattern[j][i-j])

    return tracker

def find_path(tracker):
    length = len(pattern)-1
    path_points =[ [length , length]]
    cards = ["X" , 0]
    dire= {"D" : [1, 0] , "U":[-1,0] , "R": [0,1] , "L":[0,-1]}
    perp_dir = {"D" : ["L" ,"R"] , "U":["L" ,"R"]  , "R":["U" , "D"] , "L":["U" , "D"]}
    cur_cor = [length , length]
    aval_dir = ["R" ,"L" , "D" , "U"]
    while cur_cor != [0,0]:
        mini = 10000
        for thing in aval_dir:
            for k in range(3 , len(tracker[cur_cor[0]][cur_cor[1]][thing])):
                value =  tracker[cur_cor[0]][cur_cor[1]][thing][k]                                        
                if value < mini:
                    mini = value
                    cards = [thing , k+1]
        cur_cor = add_lists(multiply_list(dire[cards[0]] , cards[1] ), cur_cor )
        aval_dir = perp_dir[cards[0]].copy()
        path_points.append(cur_cor)
        
    path_points.reverse()
    return path_points

import copy
with open("input17.txt") as fin:
    pattern = []
    for line in fin:
        pattern.append(line.strip("\n"))
        
length = len(pattern)-1
tracker = map_altering(pattern)
prev_final_pos = []

while prev_final_pos != tracker[length][length]:
    prev_final_pos = copy.deepcopy(tracker[length][length])
    tracker = map_altering(tracker , True)
    
for i in range(40):
    tracker = map_altering(tracker , True)	

while prev_final_pos != tracker[length][length]:
    prev_final_pos = copy.deepcopy(tracker[length][length])
    tracker = map_altering(tracker , True)

dir_list = ["U" , "L"]
minimum = 10000
for direction in dir_list:
    for k in range(3,len(tracker[length][length][direction])):
        if tracker[length][length][direction][k] < minimum:   
            minimum = tracker[length][length][direction][k]	
            
print(minimum)
path = find_path(tracker)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
def init():
#    ax.set_xticks(range(-10,10))
#    ax.set_yticks(range(-10,10))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
#    ax.set_xlim([-1*width, width])
#    ax.set_ylim([-1*height, height])
    ax.set_aspect('equal')
    plt.tick_params(length=0)
    return ln,

fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(111)

xdata, ydata = [], []


def update(points):
    xdata.append(points[0])
    ydata.append(points[1])
    ln.set_data(xdata, ydata)
    ax.set_xlim([-0.3, length+1])
    ax.set_ylim([-0.3, length+1])
    #ax.grid(b=True, which='both', linewidth=10, c='b', linestyle='-')
    return ln,
    
plt.rcParams['lines.linewidth']= 2
ax.set_xlim([-0.3, length+1])
ax.set_ylim([-0.3, length+1])
data = np.array(path_conv(path))
plt.plot(data[:, 0], data[:, 1] , linewidth = 2) #comment this line to hide the final path from the plot (in case you are viewing the animation)
ln, = plt.plot([], [])
#ani = animation.FuncAnimation(fig, update, frames=path_conv(path),  init_func=init, blit=True, repeat=False, interval=1) #uncomment this line to get the animation of the path
plt.show()

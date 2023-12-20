def is_list_zero(list):
    for element in list:
        if element != 0:
            return False
    return True

def zero_the_list(list):
    level = 0
    tracker = [list[0]]
    while not is_list_zero(list):
        list1 = []
        for i,el in enumerate(list):
            if i ==0:
                pass
            else:
                list1.append(el- list[i-1])
        list = list1
        level += 1
        tracker.append(list[0])
    return list , tracker, level

def unzero_the_list(list ,tracker, level):
    #list.append(0)
    new_tracker =[0]
    while level >=0:
        new_tracker.append(tracker[level] - new_tracker[-1])
        level -=1
    return new_tracker[-1]

with open('input9.txt') as fin:    ####”
    sum = 0
    for line in fin:
        list = [int(i) for i in line.strip("\n").split(" ")]
        sum+= unzero_the_list(*zero_the_list(list))
    print(sum)

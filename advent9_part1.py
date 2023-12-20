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
    while level >=0:
        list1 = [tracker[level]]
        for el in list:
            list1.append(list1[-1] + el)
        level -=1
        list = list1
    return list

with open('input9.txt') as fin:    ####”
    sum = 0
    for line in fin:
        list = [int(i) for i in line.strip("\n").split(" ")]
        new_list = unzero_the_list(*zero_the_list(list))
        sum += new_list[-1]
    print(sum)

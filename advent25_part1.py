def circle_finder(dict , a = []):
    for i in dict:
        if not i in a:
            dict[i]
            break
    circle  = False
    already_circle = [i]
    prev_found = i
    while  circle == False:
        prev_on_loop = prev_found
        for j,thing in enumerate(dict[prev_found]):
            if not thing in already_circle[-1000:]+a and thing in already_circle :
                print(i)
                print(thing)
                print(prev_found)
                print(already_circle)
                circle = True
                break
            prev_on_loop = thing
        if not circle:
            if thing != prev_on_loop:
                prev_found = thing
            else:
                found = False
                for thing in dict[prev_found]:
                    if not thing in already_circle + a:
                        found = True
                        prev_found = thing
                        break
                if found == False:
                    return  already_circle
            already_circle.append(prev_found)
    return already_circle

with open("input25.txt") as fin:
    dict = {}
    count = 0
    for i,line in enumerate(fin):
        line = line.strip("\n")
        comp1 = line.split(": ")[0]
        comps2 = line.split(": ")[1].split(" ")
        for comp in comps2:
            if not comp1 in dict:
                dict[comp1] = []
            if not comp in dict:
                dict[comp] = []
            if not comp1 in dict[comp]:
                dict[comp].append(comp1)
            if not comp in dict[comp1]:
                dict[comp1].append(comp)

a = circle_finder(dict)
a = a[min([a.index(i) for i in dict[a[-1]]]  ):]

c = []
b = []
for item in a:
    count3 = 0
    for item2 in dict[item]:
        if item2 in a:
            count3 +=1
    if count3 >= 3:
        b.append(item)
a = b.copy()
while len(c) + len(a) != len(dict):

    b = []
    while b != a:
        b = a.copy()
        for i in dict:
            if not i in a:
                count2 = 0
                for item in dict[i]:
                    if item in a:
                        count2 +=1
                if count2 >= 2:
                    a.append(i)
                    try:
                        c.remove(i)
                    except:
                        pass
    c = []
    for item in dict:
        if not item in a:
            c.append(item)

    d = []
    while d != c:
        d = c.copy()
        for i in dict:
            if not i in c:
                count2 = 0
                for item in dict[i]:
                    if item in c:
                        count2 +=1
                if count2 >= 2:
                    c.append(i)
                    a.remove(i)

print(len(c)*len(a))

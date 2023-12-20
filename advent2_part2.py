with open('input2.txt') as fin:    ####”
    sum = 0
    for line in fin:
        rounds = (line.split(':')[1]).split(";")
        id = (line.split(':')[0]).split("Game ")[1]
        round_valid = True
        max_green = 0
        max_red = 0
        max_blue = 0
        for round in rounds:
            parts = round.split(",")
            green = 0
            red = 0
            blue = 0
            try:
                green = int(round.split(" green")[0].split(" ")[-1])
            except:
                pass
            try:
                red = int(round.split(" red")[0].split(" ")[-1])
            except:
                pass
            try:
                blue = int(round.split(" blue")[0].split(" ")[-1])
            except:
                pass
            if blue > max_blue:
                max_blue = blue
            if red > max_red:
                max_red = red
            if green > max_green:
                max_green = green
        power = max_red*max_green*max_blue
        #    sum += int(id)
        sum += power
    print(sum)

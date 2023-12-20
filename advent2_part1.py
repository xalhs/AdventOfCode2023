with open('input2.txt') as fin:    ####”
    sum = 0
    for line in fin:
        rounds = (line.split(':')[1]).split(";")
        id = (line.split(':')[0]).split("Game ")[1]
        round_valid = True
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
            if (red > 12 or green > 13) or blue > 14:
                round_valid = False
        if round_valid == True:
            sum += int(id)
    print(sum)

# Part A
fo = open("02.txt", "r")

depth = 0
dist = 0

for line in fo:
    splits = line.split(" ")
    dir = splits[0]
    val = int(splits[1])
    if dir == "forward":
        dist += val
    elif dir == "down":
        depth += val
    elif dir == "up":
        depth -= val
    else:
        "Unkown value"
        exit

fo.close()

print ("part a:", depth * dist)


# Part B
fo = open("02.txt", "r")

aim = 0
depth = 0
dist = 0

for line in fo:
    splits = line.split(" ")
    dir = splits[0]
    val = int(splits[1])
    if dir == "forward":
        dist += val
        depth += aim*val
    elif dir == "down":
        aim += val
    elif dir == "up":
        aim -= val
    else:
        "Unkown value"
        exit

fo.close()

print ("part b:", depth * dist)
# Part A
fo = open("01.txt", "r")

prev_val = 0
increments = 0

for line in fo:
    if int(line) > prev_val:
        increments += 1
    prev_val = int(line)

fo.close()

print("part a:", increments - 1)


# Part B
fo = open("01.txt", "r")

window = []
prev_val = 0
increments = 0

for line in fo:
    val = int(line)
    if len(window) == 3:
        window.pop()
    window.insert(0, val)
    if len(window) == 3:
        if prev_val != 0:
            if sum(window) > prev_val: 
                increments += 1
        prev_val = sum(window)


fo.close()
print("part 2:", increments)
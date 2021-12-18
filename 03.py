# Part A
fo = open("03.txt", "r")

count = {}
num_lines = 0

for line in fo:
    for i in range(len(line)):
        if line[i] == "1":
            if count.get(i) == None:
                count[i] = 1
            else:
                count[i] += 1
    num_lines += 1

fo.seek(0)
bin_len = len(fo.readline())
fo.close()

gamma = ""
epsilon = ""

for i in range(bin_len-1):
    if count[i] > num_lines/2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print ("part a:", int(gamma, 2) * int(epsilon, 2))

# Part B

def splitOxyAndCo2(input, index):
    dic = {}
    for line in input:
        if len(line) > index:
            front_char = line[index]
            dic.setdefault(front_char, []).append(line)
        else:
            break
    if dic.has_key('0') == False:
        return dic['1'], dic['1']
    if dic.has_key('1') == False:
        return dic['0'], dic['0']
    if len(dic['0']) > len(dic['1']):
        return dic['0'], dic['1']
    return dic['1'], dic['0']

fo = open("03.txt", "r")
oxy, co2 = splitOxyAndCo2(fo, 0)

oxy_ans = ""
index = 1
while oxy_ans == "":
    oxy, _ = splitOxyAndCo2(oxy, index)
    if len(oxy) == 1:
        oxy_ans = oxy[0]
    index+= 1

co2_ans = ""
index = 1
while co2_ans == "":
    _, co2 = splitOxyAndCo2(co2, index)
    if len(co2) == 1:
        co2_ans = co2[0]
    index+= 1

fo.close()
print ("part b:", int(oxy_ans, 2) * int(co2_ans, 2))
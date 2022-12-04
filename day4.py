f = open('day4-input.txt','r')
lines = f.readlines()
lines = [line.rstrip() for line in lines]


total = 0
totaltwo = 0
for line in lines:
    line = line.split("-")
    middle = line[1]
    middle = middle.split(",")

    onestart = int(line[0])
    oneend = int(middle[0])
    twostart = int(middle[1])
    twoend = int(line[2])

    if onestart <= twostart and oneend >= twoend:
        total += 1
    elif twostart <= onestart and twoend >= oneend:
        total += 1
    
    arrayone = [onestart]
    arraytwo = [twostart]

    for x in range(onestart, oneend + 1):
        arrayone.append(x)
    for x in range(twostart, twoend + 1):
        arraytwo.append(x)
    for x in arrayone:
        if(x in arraytwo):
            totaltwo += 1
            break


print(total)
print(totaltwo)
f.close()
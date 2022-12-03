f = open('day1-input.txt','r')
lines = f.readlines()

currentHigh = [-1000, -1000, -1000]
current = 0
for line in lines:
    if line.strip():
        current += int(line)
    else:
        if current > currentHigh[2]:
            currentHigh[2] = current
            if currentHigh[2] > currentHigh[1]:
                currentHigh[1], currentHigh[2] = currentHigh[2], currentHigh[1]
                if currentHigh[1] > currentHigh[0]:
                    currentHigh[1], currentHigh[0] = currentHigh[0], currentHigh[1]
        current = 0

print(currentHigh[0] + currentHigh[1] + currentHigh[2])


f.close()
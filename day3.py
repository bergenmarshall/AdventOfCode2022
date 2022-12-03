f = open('day3-input.txt','r')
lines = f.readlines()
lines = [line.rstrip() for line in lines]

sum = 0
badgesum = 0
i = 0
for i, line in enumerate(lines):
    half = len(line)//2
    firstHalf, secondHalf = line[:half], line[half:]
    for element in firstHalf:
        if element in secondHalf:
            if ord(element) > 96:
                sum += ord(element) - 96
                break
            else:
                sum += ord(element) - 38
                break
    if i % 3 == 0:
        for element in line:
            if element in lines[i + 1] and element in lines[i + 2]:
                if ord(element) > 96:
                    badgesum += ord(element) - 96
                    break
                else:
                    badgesum += ord(element) - 38
                    break
    

print(sum)
print(badgesum)
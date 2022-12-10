f = open('day8-input.txt','r')
lines = f.readlines()
lines = [line.rstrip() for line in lines]

total = 0

highestScenicScore = 0

linePostion = 0
for line in lines:
    charPosition = 0
    for char in line:
        charPosition += 1
        left = line[:charPosition-1]
        right = line[charPosition:]
        above = [lines[x][charPosition-1] for x in range(0,linePostion)]
        below = [lines[x][charPosition-1] for x in range(linePostion+1, len(lines)-1)]
        if(all(i < char for i in left)):
            total += 1
        elif(all(i < char for i in right)):
            total += 1
        elif(all(i < char for i in above)):
            total += 1
        elif(all(i < char for i in below)):
            total += 1

        leftScore = 0
        rightScore = 0
        upScore = 0
        downScore = 0

        left = left[::-1]
        above = above[::-1]

        for i in left:
            leftScore += 1
            if i >= char:
                break
        for i in right:
            rightScore += 1
            if i >= char:
                break
        for i in above:
            upScore += 1
            if i >= char:
                break
        for i in below:
            downScore += 1
            if i >= char:
                break
        scenicScore = leftScore * rightScore * upScore * downScore
        if(scenicScore >highestScenicScore):
            highestScenicScore = scenicScore
    linePostion += 1

print(total)
print(highestScenicScore)
f.close()
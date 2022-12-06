f = open('day5-input.txt','r')
lines = f.readlines()
lines = [line.rstrip() for line in lines]
lines = [line.ljust(34) for line in lines]

Array = ["" for i in range(9)]
SizeArray = [-1 for i in range(9)]

for i in range(0, 8):
    if(lines[i][1] != " "):
        Array[0] += lines[i][1]
        SizeArray[0] += 1
    if(lines[i][5] != " "):
        Array[1] += lines[i][5]
        SizeArray[1] += 1
    if(lines[i][9] != " "):
        Array[2] += lines[i][9]
        SizeArray[2] += 1
    if(lines[i][13] != " "):
        Array[3] += lines[i][13]
        SizeArray[3] += 1
    if(lines[i][17] != " "):
        Array[4] += lines[i][17]
        SizeArray[4] += 1
    if(lines[i][21] != " "):
        Array[5] += lines[i][21]
        SizeArray[5] += 1
    if(lines[i][25] != " "):
        Array[6] += lines[i][25]
        SizeArray[6] += 1
    if(lines[i][29] != " "):
        Array[7] += lines[i][29]
        SizeArray[7] += 1
    if(lines[i][33] != " "):
        Array[8] += lines[i][33]
        SizeArray[8] += 1

for i in range(9):
    DaString = Array[i]
    Array[i] = DaString[::-1] 

print(Array)

for line in lines:
    if(line[0] == "m"):
        line = line.split(' ')
        NumMoves = int(line[1])
        To = int(line[5]) - 1
        From = int(line[3]) - 1
        Moving = Array[From][-NumMoves:]
        Array[From] = Array[From][:-NumMoves]
        Array[To] += Moving

print(Array)
f = open('day2-input.txt','r')
lines = f.readlines()
lines = [line.rstrip() for line in lines]

sum = 0
for line in lines:
    line = list(line.split(' '))
    if(line[1] == 'Y'): 
        sum += 3
        if(line[0] == 'A'): #Rock
            sum += 1
        elif(line[0] == 'B'): #Paper
            sum += 2
        else:               #scissors
            sum += 3
    elif(line[1] == 'X'): 
        sum += 0
        if(line[0] == 'A'): #Rock
           sum += 3
        elif(line[0] == 'B'): #Paper
            sum += 1
        else:               #scissors
            sum += 2
    else:                  
        sum += 6
        if(line[0] == 'A'): #Rock
            sum += 2
        elif(line[0] == 'B'): #Paper
            sum += 3
        else:               #scissors
            sum += 1

print(sum)

f.close()
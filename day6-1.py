f = open('day6-input.txt','r')
line = f.readline()
line = line.rstrip()

list = ['X','X','X','X']

spot = 0

for char in line:
    spot += 1
    if len(set(list)) == len(list) and list[3] != 'X':
        print(list)
        print(spot)
        break
    else:
        list = [char] + list[:-1]

f.close()
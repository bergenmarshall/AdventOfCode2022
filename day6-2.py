f = open('day6-input.txt','r')
line = f.readline()
line = line.rstrip()
list = ['X','X','X','X','X','X','X','X','X','X','X','X','X']
spot = 0
for char in line:
    spot += 1
    if len(set(list)) == len(list) and list[0] != 'X':
        print(spot)
        break
    else:
        list = [char] + list[:-1]
<<<<<<< HEAD:day6.py
=======

>>>>>>> 9f945eb3925aafc878a7ec37439a66a157ffc73a:day6-2.py
f.close()
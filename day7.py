f = open('day7-input.txt','r')
lines = f.readlines()
lines = [line.rstrip() for line in lines]


path = []
Directories = {"/":0}

path.append("/")

for line in lines:
    if '$ cd' in line:
        if line.split()[-1] == '..':
            path.pop()
        else:
            path.append(line.split()[-1])
    elif line.split()[0].isdigit():
        size = int(line.split()[0])
        pathname = '/'
        for dir in path:
            pathname += (dir + '/') if dir != '/' else ''
            if pathname not in Directories:
                Directories[pathname] = 0
            Directories[pathname] += size

sum = sum([directory for directory in Directories.values() if directory <= 100000])
min = min([directory for directory in Directories.values() if directory >= (30000000 - (70000000 - Directories['/']))])
    
print(sum)
print(min)

f.close()
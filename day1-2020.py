with open("day1data.txt","r") as file:
    data = [int(line.strip()) for line in file.readlines()]

for x in data:
    for y in data:
        for z in data:
            if x != y and y!= z and z != x:
                if x + y + z == 2020:
                    print(x*y*z)


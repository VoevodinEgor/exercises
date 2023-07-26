#part1
with open ('exercise04data.txt', 'r') as file:
    count = 0
    for line in file:
        line = line.replace('\n','').split(',')
        pair1 = list(map(int,line[0].split('-')))
        pair2 = list(map(int,line[1].split('-')))
        if pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
            count += 1
        elif pair2[0] <= pair1[0] and pair2[1] >= pair1[1]:
            count += 1
print(count)

#part2
with open ('exercise04data.txt', 'r') as file:
    count = 0
    for line in file:
        line = line.replace('\n','').split(',')
        pair1 = list(map(int,line[0].split('-')))
        pair2 = list(map(int,line[1].split('-')))
        if pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
            count += 1
        elif pair2[0] <= pair1[0] and pair2[1] >= pair1[1]:
            count += 1
        elif pair2[0] <= pair1[1] and pair2[0] >= pair1[0]:
            count += 1
        elif pair1[0] <= pair2[1] and pair1[0] >= pair2[0]:
            count += 1
print(count)



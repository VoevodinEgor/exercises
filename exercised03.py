import string

alphabet = string.ascii_letters
#part1
with open('exercise03data.txt', 'r') as file:
    items = []
    for line in file:
        line = line.replace('\n','')
        len_part_line = int(len(line)/2)
        for item in line[:len_part_line]:
            if item in line[len_part_line:]:
                items.append(item)
                break
score = 0
for item in items:
    score += alphabet.index(item) + 1
print(score)

#part2
with open('exercise03data.txt', 'r') as file:
    items = []
    item = []
    result_items = []
    for line in file:
        line = line.replace('\n','')
        if len(item) < 3:
            item.append(line)
        if len(item) == 3:
            items.append(item)
            item = []
    for item in items:
        for i in item[0]:
            if i in item[1] and i in item[2]:
                result_items.append(i)
                break
score = 0
for item in result_items:
    score += alphabet.index(item) + 1
print(score)     

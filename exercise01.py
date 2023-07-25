elfs_food = []
with open('exercise01data.txt', 'r') as file:
    data_chunks = file.read().split('\n\n')
    for data_block in data_chunks:
        data_lines = data_block.strip().split('\n')
        elfs_food.append(list(map(int, data_lines)))
#part 1
max_callories = max(list(map(sum, elfs_food)))
for i, food in enumerate(elfs_food):
    sum_callories = sum(food)
    if sum_callories == max_callories:
        print(f"У эльфа под номером {i+1} наибольшее количество калорий {sum_callories}")
#part 2
max_callories = sorted(list(map(sum, elfs_food)))[-3:]
print(f"Суммарное количество калорий у 3 эльфов с самым большим их количеством:{sum(max_callories)}")
elfs_list = []
for i, food in enumerate(elfs_food):
    sum_callories = sum(food)
    if sum_callories in max_callories:
        elfs_list.append(i)
print(f"Это эльфы {elfs_list}")
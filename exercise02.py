#Part 1
#A for Rock, B for Paper, and C for Scissors - opponent
#X for Rock, Y for Paper, and Z for Scissors - me
my_scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
opponent_scores = {
    "A": 1,
    "B": 2,
    "C": 3
}
results = {
    "loose": 0,
    "draw": 3,
    "win": 6
}
score = 0
with open('exercise02data.txt','r') as file:
    for line in file:
        if line[2] == "Z" and line[0] == "A":
            #значение не увеличивается
            score += results['loose']
        elif line[2] == "X" and line[0] == "C":
            score += results['win']
        elif my_scores[line[2]] > opponent_scores[line[0]]:
            score += results['win']
        elif my_scores[line[2]] == opponent_scores[line[0]]:
            score += results['draw']
        score += my_scores[line[2]]
print(score)

#Part 2
#A for Rock, B for Paper, and C for Scissors - opponent
#X for loose, Y for draw, and Z for win - me
win_patters = {
'A': 'B',
'B': 'C',
'C': 'A'
}
loose_patterns = {
'A': 'C',
'B': 'A',
'C': 'B'
}
with open('exercise02data.txt','r') as file:
    score = 0
    for line in file:
        if line[2] == 'X':
            my_choice = loose_patterns[line[0]]
            score += opponent_scores[my_choice]
        elif line[2] == 'Y':
            score += results['draw']
            score += opponent_scores[line[0]]
        else:
            my_choice = win_patters[line[0]]
            score += results['win']
            score += opponent_scores[my_choice]
print(score)
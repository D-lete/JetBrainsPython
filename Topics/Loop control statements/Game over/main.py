scores = input().split()
scores_string = ''.join(scores)
third = [i for i in range(len(scores)) if scores_string.startswith('I', i)]
if scores.count('I') >= 3:
    print(f"Game over\n{scores[0:third[2]].count('C')}")
else:
    print(f"You won\n{scores.count('C')}")

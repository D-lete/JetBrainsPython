lines = int(input())
win_loss = []
winners = []
for i in range(lines):
    scores = input()
    win_loss.append(tuple([name for name in scores.split()[0] if scores.split()[1] == 'win']))
    win_loss = [t for t in win_loss if t]
    winners = [''.join(i) for i in win_loss]
print(winners)
print(len(win_loss))

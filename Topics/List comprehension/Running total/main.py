seed = list(input())
stage = [int(x) for x in seed]
running_total = []
for x in seed:
    max_loops = len(seed)
    current_loop = 1
    while current_loop < max_loops + 1:
        total = (sum(stage[0:current_loop:1]))
        current_loop += 1
        running_total.append(total)
print(running_total[0:max_loops])

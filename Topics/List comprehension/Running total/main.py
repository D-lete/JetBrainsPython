seed = list(input())
stage = [int(x) for x in seed]
running_total = []
for x in seed:
    max_loops = len(seed)
    current_loop = 1
    while current_loop < max_loops + 1:
        total = (sum(stage[0:current_loop]))
        current_loop += 1
        running_total.append(total)
print(list(set(running_total))) #<-- Here

# TODO: issue is that the loop calcs correctly but the set function is eliminating a value where it is added to 0
#  thus creating a duplicate in the set... need to fix 3x loop issue

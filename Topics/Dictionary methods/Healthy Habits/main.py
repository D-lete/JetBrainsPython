# the list "walks" is already defined
# your code here
import statistics

key = 'distance'
print(round(statistics.mean([a_dict[key] for a_dict in walks])))

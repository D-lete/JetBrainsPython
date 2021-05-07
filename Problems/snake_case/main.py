import re

variable = input()
words = [re.sub(r'([A-Z])', r'_\1', variable)].pop(0)
if words[0] == '_':
    print(words[1:].lower())
else:
    print(words[0:].lower())

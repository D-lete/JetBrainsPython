word = input()

for i in range(len(word)):
    if not word[i].islower() and i > 0:
        word_start = word[:i]
        word_end = word[i:]
        print(word_start.lower() + '_' + word_end.lower())

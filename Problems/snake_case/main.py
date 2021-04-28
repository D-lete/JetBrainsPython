
word = input()

for i in range(len(word)):
    if not word[i].islower() and i > 0:
        word = word[:i] + "_" + word[i:]
        uppers = word.count(word[i].isupper())
        if word.count("_", 0) > uppers:
            word.replace("_", "", uppers - 1)

print(word.lower())

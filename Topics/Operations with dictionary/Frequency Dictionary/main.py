words = str(input()).lower().split()
word_set = set(words)
result = {word: words.count(word) for word in words}
for key, value in result.items():
    print(key, ' ', value)

text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
length = int(input())
result = []
for words in text:
        for word in words:
                if len(word) <= length:
                        result.append(word)
print(result)

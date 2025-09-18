'''
    Count frequency of words in data.text

'''
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()   # read entire file as one string

words = text.split()   # split text into words (by spaces/newlines)

word_counts = {}       # dictionary to store frequencies

for w in words:
    w = w.strip(".,!?;:\"'()[]{}").lower()  # clean punctuation, lowercase
    if w not in word_counts:
        word_counts[w] = 1
    else:
        word_counts[w] += 1

print(word_counts)


with open("my_book.txt","r") as f:
    text = f.read()

keys_by_words = {}
for i in text.split():
    if i not in keys_by_words:
        keys_by_words[i] = 1
    else:
        keys_by_words[i] += 1
print(keys_by_words)

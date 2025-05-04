with open("my_book.txt","r") as f:
    text = f.read()

keys_by_words = {}
for word in text.split():
    word = word.replace(",","").replace(".","").lower()
    if word not in keys_by_words:
        keys_by_words[word] = 1
    else:
        keys_by_words[word] += 1

def sum_of_the_different_words():
    return len(keys_by_words)



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


def selecting_words_by_their_length(length):
    result = []
    for k, v in keys_by_words.items():
        if v == length:
            result.append(k)
    return result
enter_len_of_word = int(input("please enter len of word! "))
print(selecting_words_by_their_length(enter_len_of_word))


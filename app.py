class Books:

    def __init__(self, name_file):
        """
        Opens the text file, reads its content, and splits it into words.
        It also creates a dictionary (word_counts) that counts how many times each word appears,
        after removing commas and periods and converting words to lowercase.
        """

        with open(f"{name_file}.txt", "r") as f:
            self.raw_text = f.read()
        self.text = self.raw_text.split()

        self.word_counts = {}
        for word in self.text:
            word = word.replace(",", "").replace(".", "").lower()
            self.word_counts[word] = self.word_counts.get(word, 0) + 1

    def most_frequent_word(self):
        """
        Finds and returns the word that appears most frequently in the text,
        along with how many times it appears.
        """

        most_common_word, max_count = "", 0
        for word, count in self.word_counts.items():
            if count > max_count:
                most_common_word, max_count = word, count
        return f"The word '{most_common_word}' found in book {max_count} times"

    def count_unique_words(self):
        """
        Returns the number of unique words in the text.
        """
        return len(self.word_counts)

    def count_sentences(self):
        """
        Returns the number of sentences in the text,
        based on counting the number of periods ('.').
        """

        return self.raw_text.count(".")

    def words_with_given_frequency(self):
        """
        Asks the user to input a number and returns a list of words
        that appear exactly that many times in the text.
        """

        length = int(input("Please enter number of appearances: "))
        result = []
        for word, count in self.word_counts.items():
            if count == length:
                result.append(word)
        return result

    def longest_words(self):
        """
        Finds and returns a list of the longest word(s) in the text.
        If there are multiple words with the same maximum length, all are returned.  
        """

        longest = [""]
        for word in self.text:
            if len(longest[0]) < len(word):
                longest = [word]
            elif len(longest[0]) == len(word):
                longest.append(word)
        return longest

    def equal_length_word_chains(self):
        """
        Returns all chains of consecutive words that have the same length.
        Only chains with at least two words are included. 
        """

        chains = []
        chain = [self.text[0]]

        for word in self.text[1:] + [""]:
            if len(word) == len(chain[-1]):
                chain.append(word)
            elif len(chain) > 1:
                chains.append(' '.join(chain))
                chain = [word]
            else:
                chain = [word]
        return chains


response = int(input("Please choose an option to display:\n\n"
                     "1. Display the number of sentences in the text.\n"
                     "2. Display the most frequent word in the text and how many times it appears.\n"
                     "3. Display the longest word(s) in the text. If there are multiple words with the same length, display all of them.\n"
                     "4. Display the number of unique words in the text.\n"
                     "5. Display all words that appear a specified number of times in the text. Please enter the number of occurrences:\n"
                     "6. Display all chains of words (at least two words) where the total number of characters in the chain is the same.\n"
                     "7. Exit.\n"))

a = Books("my_book")

if response == 1:
    print(a.count_sentences())
elif response == 2:
    print(a.most_frequent_word())
elif response == 3:
    print(a.longest_words())
elif response == 4:
    print(a.count_unique_words())
elif response == 5:
    print(a.words_with_given_frequency())
elif response == 6:
    print(a.equal_length_word_chains())

word_list = ["apple", "banana", "orange", "grape", "kiwi", "pear"]

odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Words with odd length:")
print(odd_length_words)
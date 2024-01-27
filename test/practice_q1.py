import nltk
import string
from collections import Counter

def count_words_from_file(file):
    with open(file, "r") as f:
        text = f.read()

    words = extract_words_from_text(text)

    counter = Counter(words)
    word_count = dict(counter)
    return word_count

def extract_words_from_text(text):
    # make all letters lowercase
    text = text.lower()

    # remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # get list of words from text
    words = nltk.word_tokenize(text)
    return words

if __name__ == "__main__":
    word_count = count_words_from_file("story.txt")

    # print word_count, sorted by value
    sorted_word_count = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)
    print(sorted_word_count)
    
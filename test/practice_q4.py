import nltk
import string
from collections import Counter
from nltk.book import text1 as text


def count_words_from_text():

    words = extract_words_from_text(text)

    porter_stemmer = nltk.stem.PorterStemmer()
    stemmed_words = [porter_stemmer.stem(word) for word in words]

    counter = Counter(words)
    word_count = dict(counter)
    sorted_word_count = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)

    stem_counter = Counter(stemmed_words)
    stem_word_count = dict(stem_counter)
    sorted_stem_word_count = sorted(stem_word_count.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_word_count, sorted_stem_word_count

def extract_words_from_text(text):
    tokens = text.tokens

    # make all letters lowercase and remove punctuation tokens
    tokens = [word.lower() for word in tokens if word not in string.punctuation]

    return tokens

if __name__ == "__main__":

    wc, swc = count_words_from_text()

    print(wc[:5])
    print(swc[:5])

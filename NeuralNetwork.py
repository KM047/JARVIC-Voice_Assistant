import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()
try:

    def tokenize(sentence):
        if not sentence:
            # print('The text to be tokenized is a None type. Defaulting to blank string.')
            sentence = ''
        

        return nltk.word_tokenize(sentence)


    def stem(word):

        return Stemmer.stem(word.lower())


    def bag_of_words(tokenized_sentence, words):
        
        if not words:
            # print('The text to be tokenized is a None type. Defaulting to blank string.')
            words = ''
        sentence_word = [stem(word) for word in tokenized_sentence]
        bag = np.zeros(len(words), dtype=np.float32)

        for idx, w in enumerate(words):
            if w in sentence_word:
                bag[idx] = 1

        return bag

except:
    pass
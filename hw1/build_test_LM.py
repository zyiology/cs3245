#!/usr/bin/python3

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
import nltk
import sys
import getopt
import four_gram_language_model as fglm


def build_LM(in_file):
    """
    build language models for each label
    each line in in_file contains a label and a string separated by a space
    """
    print("building language models...")
    # This is an empty method
    # Pls implement your code below

    lm = fglm.FourGramLanguageModel()

    with open(in_file, "r") as f:
        labels = []
        strings = []
        for line in f:
            label, string = line.split(" ", 1)
            labels.append(label)
            strings.append(string)
        
    lm.train(strings, labels)
    return lm
            




def test_LM(in_file, out_file, LM):
    # type: (str, str, fglm.FourGramLanguageModel) -> None
    """
    test the language models on new strings
    each line of in_file contains a string
    you should print the most probable label for each string into out_file
    """
    print("testing language models...")
    # This is an empty method
    # Pls implement your code below

    with open(in_file, "r") as f:
        with open(out_file, "w") as o:
            for line in f:
                predicted_label = LM.predict(line)
                o.write(predicted_label + " " + line)
    


def usage():
    print(
        "usage: "
        + sys.argv[0]
        + " -b input-file-for-building-LM -t input-file-for-testing-LM -o output-file"
    )


input_file_b = input_file_t = output_file = None
try:
    opts, args = getopt.getopt(sys.argv[1:], "b:t:o:")
except getopt.GetoptError:
    usage()
    sys.exit(2)
for o, a in opts:
    if o == "-b": # a file given to you that contains a list of strings with their labels for you to build your ngram language models
        input_file_b = a
    elif o == "-t": # file containing a list of strings for you to test your language models
        input_file_t = a
    elif o == "-o": # file where you store your predictions
        output_file = a
    else:
        assert False, "unhandled option"

if input_file_b == None or input_file_t == None or output_file == None:
    usage()
    sys.exit(2)

LM = build_LM(input_file_b)
test_LM(input_file_t, output_file, LM)

# python3 build_test_LM.py -b 'input.train.txt' -t 'input.test.txt' -o 'output_predictions.txt'
# python3 eval.py output_predictions.txt input.correct.txt
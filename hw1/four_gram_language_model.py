from typing import Any
import numpy as np

class FourGramLanguageModel():
    def __init__(self):
        self.four_grams_counts = {} # type: dict[str, dict[str, int]]
        self.four_grams_mastercount = {} # type: dict[str, int]
        self.four_grams_probabilities = {} # type: dict[str, dict[str, np.float128]]
        return

    def train(self, inputs, targets):
        # type: (list[str], list[str]) -> None

        if len(inputs) != len(targets):
            raise ValueError("inputs and targets must be the same length")
        
        for t in set(targets):
            self.four_grams_counts[t] = {}
            self.four_grams_mastercount[t] = 0
        
        # collect 4-grams from each input string
        for input, target in zip(inputs, targets):
            for four_gram in generate_four_grams(input):
                # for a given 4-gram, check if it exists in all the languages
                for key in self.four_grams_counts.keys():
                    if four_gram not in self.four_grams_counts[key].keys():
                        self.four_grams_counts[key][four_gram] = 0

                # increment the count for the target language
                self.four_grams_counts[target][four_gram] += 1
            
        # increase the count of all 4-grams by 1 and document the mastercount
        for key in self.four_grams_counts.keys():
            for four_gram in self.four_grams_counts[key].keys():
                self.four_grams_counts[key][four_gram] += 1
                self.four_grams_mastercount[key] += self.four_grams_counts[key][four_gram]

        # calculate the probabilities
        for key in self.four_grams_counts.keys():
            self.four_grams_probabilities[key] = {}
            for four_gram in self.four_grams_counts[key].keys():
                self.four_grams_probabilities[key][four_gram] = np.float128(self.four_grams_counts[key][four_gram]) / np.float128(self.four_grams_mastercount[key])

        return
    
    def predict(self, input):
        # type: (str) -> str
        """
        Predict the language of the input string
        """
        if len(self.four_grams_probabilities) == 0:
            raise ValueError("language model must be trained first")

        # calculate the probability of each language
        probabilities = {} # type: dict[str, np.float128]
        for key in self.four_grams_probabilities.keys():
            probabilities[key] = np.float128(1)
            missing_four_grams = 0
            total_four_grams = 0
            for four_gram in generate_four_grams(input):
                if four_gram in self.four_grams_probabilities[key].keys():
                    probabilities[key] *= self.four_grams_probabilities[key][four_gram]
                
                #if 4-gram wasn't encountered in training, ignore it
                else:
                    # probabilities[key] *= 1 / self.four_grams_mastercount[key]
                    missing_four_grams += 1
                
                total_four_grams += 1

            # if too many 4-grams were missing, set probability to 0
            if missing_four_grams / total_four_grams > 0.5:
                probabilities[key] = 0
        
        # check if all probabilities are 0, return "other" instead
        if all(prob == 0 for prob in probabilities.values()):
            return "other"

        # return the language with the highest probability
        return max(probabilities, key=probabilities.get)
    

def generate_four_grams(input_string):
    # type: (str) -> list[str]
    """
    Generate a list of four-grams from the input string
    """
    if len(input_string) < 4:
        return

    for i in range(len(input_string) - 3):
        four_gram = input_string[i:i+4]
        yield four_gram

if __name__ == "__main__":
    test_input = ["this is a test", "this is another test", "watashi wa anata ga suki desu"]
    test_target = ["english", "english", "japanese"]

    lm = FourGramLanguageModel()
    lm.train(test_input, test_target)
    print(lm.four_grams_probabilities)
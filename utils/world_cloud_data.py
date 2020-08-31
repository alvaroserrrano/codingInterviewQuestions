"""
You want to build a word cloud, an infographic where the size of a word
corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds
its word cloud data in a dictionary ↴ , where the keys are words and the values
are the number of times the words occurred.

Think about capitalized words. For example, look at these sentences:

  'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'
What do we want to do with "After", "Dana", and "add"? In this example, your
final dictionary should include one "Add" or "add" with a value of 22.
Make reasonable (not necessarily perfect) decisions about cases like
"After" and "Dana".

Assume the input will only contain words and standard punctuation.
"""
class WorldCloudData:
    def __init__(self, input_str):
        self.dict = {}
        self.populate_dict(input_str)
    def populate_dict(self, input_str):
        word_start_index, word_length = 0, 0
        for i, char in enumerate(input_str):
            #we reach the end of the string
            if i == len(input_str) -1:
                if char.isalpha():
                    word_length += 1
                if word_length > 0:
                    word = input_str[word_start_index: word_start_index + word_length]
                    self.add_to_dict(word)
                    word_length = 0
            #space or emdash => reach end of word
            elif char == ' ' or char == u'\u2014':
                if word_length > 0:
                    word = input_str[word_start_index: word_start_index + word_length]
                    self.add_to_dict(word)
                    word_length == 0
            #check for elipses
            elif char == '.':
                if i < len(input_str) -1 and input_str[i+1]=='.':
                    if word_length > 0:
                        word = input_str[word_start_index: word_start_index + word_length]
                        self.add_to_dict(word)
                        word_length = 0
            #not to skip apostrophe
            elif char == '\'' or char.isalpha():
                if word_length == 0:
                    word_start_index = i
                word_length += 1
            #hyphen surrounded by chars
            elif char == '-':
                if i > 0 and input_str[i-1].isalpha() and input_str[i+1].isalpha():
                    if word_length == 0:
                        word_start_index = i
                    word_length += 1
                else:
                    if word_length > 0:
                        word =input_str[word_start_index: word_start_index + word_length]
                        self.add_to_dict(word)
                        word_length = 0
    def add_word_to_dict(self, word):
        if word in self.dict:
            self.dict[word] += 1
        #add to count if an uppercase version is found
        elif word.lower() in self.dict:
            self.dict[word.lower()] += 1
        #exchange uppercase version for all lowercase
        elif word.capitalize() in self.dict:
            self.dict[word] = 1
            self.dict[word] += self.dict[word.capitalize()]
            del self.dict[word.capitalize()]
        else:
            self.dict[word] = 1


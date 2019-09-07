############################################################
# CIS 521: Homework 1
############################################################

student_name = "Jerrison Li"

############################################################
# Section 1: Python Concepts - Study Questions
############################################################

python_concepts_question_1 = """
Strongly typed means that 
"""

python_concepts_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
This question will not be graded.
"""

python_concepts_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
This question will not be graded.
"""


############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(l) for l in p(l)]


def concatenate(seqs):
    return [x for y in seqs for x in y]


def transpose(matrix):
    result = [[] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j].append(matrix[i][j])
    return result


############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]


def all_but_last(seq):
    return seq[:-1]


def every_other(seq):
    return seq[::2]


############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    for i in range(len(seq) + 1):
        yield seq[:i]


def suffixes(seq):
    for i in range(len(seq) + 1):
        yield seq[i:]


def slices(seq):
    for i in range(len(seq)):
        for j in range(1, len(seq) + 1):
            if i < j:
                yield seq[i:j]


############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    return " ".join(text.lower().split())


def no_vowels(text):
    vowels = "aeiouAEIOU"
    for i in vowels:
        text = text.replace(i, "")
    return text


def digits_to_words(text):
    result = ""
    num_dict = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
                "5": "five", "6": "six", "7": "seven", "8": "eight",
                "9": "nine"}

    for letter in text:
        if letter.isdigit():
            result += num_dict.get(letter) + " "

    return result.strip()


def to_mixed_case(name):
    text = name.replace("_", " ").title().split()
    if len(text) > 0:
        text = text[0].lower() + "".join(text[1:])
        return text
    # text = text.lower()

    return "".join(text)




############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        pass

    def get_polynomial(self):
        pass

    def __neg__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __call__(self, x):
        pass

    def simplify(self):
        pass

    def __str__(self):
        pass


############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
This question will not be graded.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
This question will not be graded.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
This question will not be graded.
"""

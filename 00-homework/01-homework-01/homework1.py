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
    return [f(x) for x in l if p(x)]


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
    num_dict = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }

    for letter in text:
        if letter.isdigit():
            result += num_dict.get(letter) + " "

    return result.strip()


def to_mixed_case(name):
    text = name.replace("_", " ").split()
    if len(text) > 1:
        text = text[0].lower() + "".join(x.capitalize() for x in text[1:])
        return text
    elif len(text) == 1:
        text = text.lower()
    else:
        text = ""

    return text


############################################################
# Section 6: Polynomials
############################################################


class Polynomial(object):
    def __init__(self, polynomial):
        self.polynomial = tuple(polynomial)

    def get_polynomial(self):
        return self.polynomial

    def __neg__(self):
        return Polynomial(tuple([(-x, y) for x, y in self.polynomial]))

    def __add__(self, other):
        return Polynomial(self.get_polynomial() + other.get_polynomial())

    def __sub__(self, other):
        negated_other = -other
        return Polynomial(self.get_polynomial() + negated_other.get_polynomial())

    def __mul__(self, other):
        return Polynomial(
            tuple(
                [
                    (x[0] * y[0], x[1] + y[1])
                    for x in self.get_polynomial()
                    for y in other.get_polynomial()
                ]
            )
        )

    def __call__(self, x):
        return sum([y[0] * x ** y[1] for y in self.get_polynomial()])

    def simplify(self):
        unique_powers = list(set([y for x, y in self.get_polynomial()]))
        coefficient_dict = dict.fromkeys(unique_powers, 0)
        for coefficient, power in self.get_polynomial():
            coefficient_dict[power] += coefficient

        coefficient_dict = {v: k for k, v in coefficient_dict.items() if v != 0}

        if not bool(coefficient_dict):
            self.polynomial = ((0, 0),)
            return

        self.polynomial = tuple(
            sorted(
                [(k, v) for k, v in coefficient_dict.items()],
                key=lambda x: x[1],
                reverse=True,
            )
        )

    def __str__(self):
        if len(self.get_polynomial()) == 0:
            return ""

        result = ""
        for coefficient, power in self.get_polynomial():
            # sign part
            if coefficient < 0:
                result += "-"
            else:
                result += "+"

            result += " "

            # coefficient part
            if abs(coefficient) == 1:
                if power == 0:
                    result += str(abs(coefficient))
                else:
                    pass
            else:
                result += str(abs(coefficient))

            # power part
            if power == 0:
                pass
            elif power == 1:
                result += "x"
            else:
                result += "x^" + str(power)

            result += " "

        result = (result[0] + result[2:]).strip()

        if result[0] == "+":
            result = result[1:]

        return result


############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
11 hours
"""

feedback_question_2 = """
The syntax was the most challenging part of the assignment. Familiarity with
built-in functions was the biggest stumbling block.
"""

feedback_question_3 = """
More problems regarding matrix multiplication would be more useful.
"""

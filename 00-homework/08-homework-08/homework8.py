############################################################
# CIS 521: Homework 8
############################################################

student_name = "Jerrison Li"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import sys, re, math, random, os, string


############################################################
# Section 1: Markov Models
############################################################


def tokenize(text):
    return re.findall(r"[\w]+|[" + string.punctuation + "]", text)


def ngrams(n, tokens):
    for i in range(n):
        tokens.insert(0, "<START>")
    tokens.append("<END>")
    ngrams = []
    for i in range(n, len(tokens)):
        ngrams.append((tuple(tokens[i - n + 1 : i]), tokens[i]))
    return ngrams


class NgramModel(object):
    def __init__(self, n):
        self.n = n
        self.grams = []

    def update(self, sentence):
        tokens = tokenize(sentence)
        self.grams += ngrams(self.n, tokens)

    def prob(self, context, token):
        ctx_count = 0
        match_count = 0
        for i, v in enumerate(self.grams):
            if v[0] == context:
                ctx_count = ctx_count + 1
                if v[1] == str(token):
                    match_count = match_count + 1
        # protect against divide by 0 case
        if ctx_count == 0:
            return 0
        return float(match_count) / float(ctx_count)

    def random_token(self, context):
        T = [
            self.grams[i][1]
            for i in range(len(self.grams))
            if self.grams[i][0] == context
        ]
        T.sort()
        r = random.random()
        # index = int(math.ceil(r*(len(T)-1)))
        if len(T) != 0:
            index = int(r * len(T))
            if index > len(T) - 1:
                index = len(T) - 1
            return T[index]
        else:
            return " "

    def random_text(self, token_count):
        context = []
        for i in range(self.n - 1):
            context.append("<START>")
        tokens = []
        for i in range(token_count):
            toke = self.random_token(tuple(context))
            tokens.append(toke)
            if self.n > 1:
                if toke != "<END>":
                    context.append(toke)
                    context = context[1:]
                else:
                    context = []
                    for x in range(self.n - 1):
                        context.append("<START>")
        sentence = " ".join(word for word in tokens)
        return sentence

    def perplexity(self, sentence):
        perplexity = 0.0
        tokens = tokenize(sentence)
        test_ngrams = ngrams(self.n, tokens)
        for i in range(len(test_ngrams)):
            perplexity += math.log(
                1.0 / self.prob(test_ngrams[i][0], test_ngrams[i][1])
            )
        perplexity = math.exp(perplexity)
        return perplexity ** (1.0 / len(test_ngrams))


def create_ngram_model(n, path):
    f = open(path, "r")
    doc = NgramModel(n)
    for line in f:
        doc.update(line)
    return doc


############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = 9

feedback_question_2 = """
Learning the concepts
"""

feedback_question_3 = """
The second part.
"""

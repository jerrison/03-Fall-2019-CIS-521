############################################################
# CIS 521: Homework 7
############################################################

student_name = "Jerrison Li"

############################################################
# Imports
############################################################

import homework7_data as data

# Include your imports here, if any are used.
import time

############################################################
# Section 1: Perceptrons
############################################################


class BinaryPerceptron(object):
    def __init__(self, examples, iterations):
        self.labelDict = {}
        for i in range(iterations):
            for d, sign in examples:
                prediction = 0.0
                for key in d:
                    prediction += d[key] * self.labelDict.get(key, 0)
                if (sign and prediction <= 0) or (not sign and prediction > 0):
                    for key in d:
                        if sign > 0:
                            self.labelDict[key] = self.labelDict.get(key, 0) + d[key]
                        else:
                            self.labelDict[key] = self.labelDict.get(key, 0) - d[key]

    def predict(self, x):
        res = 0
        for key in x:
            res += self.labelDict.get(key, 0) * x[key]
        return res > 0


class MulticlassPerceptron(object):
    def __init__(self, examples, iterations):
        self.d = {label: {} for dict, label in examples}
        first = examples[0][1]
        for i in range(iterations):
            for dict, l in examples:
                bestLabel, bestVal = first, None
                for l_key in self.d:
                    prediction = 0
                    d_l = self.d[l_key]
                    for key in dict:
                        prediction += d_l.get(key, 0) * dict[key]
                    if bestVal == None or prediction > bestVal:
                        bestVal, bestLabel = prediction, l_key
                if bestLabel != l:
                    for key in dict:
                        x = dict[key]
                        self.d[l][key] = self.d[l].get(key, 0) + x
                        self.d[bestLabel][key] = self.d[bestLabel].get(key, 0) - x

    def predict(self, x):
        bestLabel = None
        bestVal = 0
        for l_key in self.d:
            prediction = 0
            for data in x:
                prediction += self.d[l_key].get(data, 0) * x[data]
            if prediction > bestVal:
                bestVal = prediction
                bestLabel = l_key
        return bestLabel


############################################################
# Section 2: Applications
############################################################


class IrisClassifier(object):
    def __init__(self, data):
        iterations = 30
        data_list = []
        for (x, y) in data:
            d = {}
            for i in range(4):
                d["p%s" % i] = x[i]
            data_list.append((d, y))
        self.p = MulticlassPerceptron(data_list, iterations)

    def classify(self, instance):
        d = {}
        for i in range(4):
            d["p%s" % i] = instance[i]
        return self.p.predict(d)


class DigitClassifier(object):
    def __init__(self, data):
        train = [
            ({i + 1: tup[i] for i in range(64)}, category) for tup, category in data
        ]
        self.p = MulticlassPerceptron(train, 9)

    def classify(self, instance):
        d = {i + 1: instance[i] for i in range(64)}
        return self.p.predict(d)


class BiasClassifier(object):
    def __init__(self, data):
        self.feature_id = ("x1", "x2")
        train = []
        for data_point in data:
            if data_point[0] > 1:
                bias = (data_point[0], 1)
            else:
                bias = (data_point[0], -1)
            data_point = list(data_point)
            data_point[0] = dict(zip(self.feature_id, bias))
            data_point = tuple(data_point)
            train.append(data_point)

        # init and train classifier on data
        self.classifier = BinaryPerceptron(train, 5)

    def classify(self, instance):
        if instance > 1:
            bias = (instance, 1)
        else:
            bias = (instance, -1)
        test_data = dict(zip(self.feature_id, bias))
        return self.classifier.predict(test_data)


class MysteryClassifier1(object):
    def __init__(self, data):
        iterations = 1
        examples = self.format_data(data)
        self.classifier = BinaryPerceptron(examples, iterations)

    def classify(self, instance):
        ins = {"x1": instance[0] ** 2 + instance[1] ** 2, "x2": 1}
        return self.classifier.predict(ins)

    def format_data(self, data):
        examples = [
            ({"x1": exp[0][0] ** 2 + exp[0][1] ** 2, "x2": 1}, exp[1]) for exp in data
        ]
        return examples


class MysteryClassifier2(object):
    def __init__(self, data):
        train = list()
        for (x, y, z), bool in data:
            d = {"x": x, "y": y, "z": z}
            if self.mystery_verifier(x, y, z):
                d["in"] = 1
            else:
                d["out"] = 1
            train.append((d, bool))
        self.p = BinaryPerceptron(train, 4)

    def classify(self, instance):
        x, y, z = instance
        d = {"x": x, "y": y, "z": z}
        if self.mystery_verifier(x, y, z):
            d["in"] = 1
        else:
            d["out"] = 1
        return self.p.predict(d)

    def mystery_verifier(self, x, y, z):
        if 0 <= x and 0 >= y and 0 >= z:
            return True
        elif 0 >= x and 0 >= y and 0 <= z:
            return True
        elif 0 <= x and 0 <= y and 0 <= z:
            return True
        elif 0 >= x and 0 <= y and 0 >= z:
            return True
        else:
            return False


############################################################
# Section 3: Feedback
############################################################

feedback_question_1 = 15

feedback_question_2 = """
The Mystery Classifiers were the most significant stumbling blocks.
"""

feedback_question_3 = """
The fact that it is touching machine learning.
"""

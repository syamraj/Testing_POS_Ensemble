import nltk

__author__ = 'devil'

from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier



import random

from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
    [(name, 'female') for name in names.words('female.txt')])

random.shuffle(labeled_names)

def gender_features(word):
    # return {'last_letter': word[-1]}
    return {"keys" : word[-1]}

featuresets = [[gender_features(n), gender] for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]

# print featuresets

classifier = nltk.NaiveBayesClassifier.train(train_set)

print train_set
print classifier.classify(gender_features('Syam'))

# for i in train_set:
#     print (i[0])

# trying with adaboost

# temp = []
# for i in train_set:
#     temp.append(i[0])

# X = train_set
# y = temp
#
# # print y[:10]
# # print X[1]
# # # print X[2]
# # print len(y)
#
# n_split = 200
#
# X_train, X_test = X[:n_split], X[n_split:]
# y_train, y_test = y[:n_split], y[n_split:]
#
#
#
# bdt_real = AdaBoostClassifier(
#     DecisionTreeClassifier(max_depth=2),
#     n_estimators=600,
#     learning_rate=1)
#
# bdt_discrete = AdaBoostClassifier(
#     DecisionTreeClassifier(max_depth=2),
#     n_estimators=600,
#     learning_rate=1.5,
#     algorithm="SAMME")
#
# bdt_real.fit(X_train, y_train)
# bdt_discrete.fit(X_train, y_train)
#
# print bdt_real.predict("syam")
# print bdt_discrete.predict("syam")

import seqlearn as seqlearn
from seqlearn.hmm import MultinomialHMM
from sklearn.feature_extraction import DictVectorizer

__author__ = 'devil'

# clf = MultinomialHMM(decode='viterbi', alpha=0.01)
#
# trainingFeatures = [{'suffix(3)': 'llo', 'prev-word': '<START>', 'suffix(2)': 'lo', 'prev-tag': '<START>', 'suffix(1)': 'o'}]
# trainingFeatures1 = [{'suffix(3)': 'his', 'prev-word': 'Hello', 'suffix(2)': 'is', 'prev-tag': 'UH', 'suffix(1)': 's'}]
#
# trainingTag = ['UH', 'DT']
#
#
# vec = DictVectorizer()
#
# trainingFeatureToVec = vec.fit_transform(trainingFeatures)
# trainingfeatureList = []
# trainingfeatureList.append(trainingFeatureToVec)
# trainingFeatureToVec = vec.fit_transform(trainingFeatures1)
# trainingfeatureList.append(trainingFeatureToVec)
#
# print len(trainingfeatureList)
# print type(trainingfeatureList[0])
# print trainingfeatureList[0].shape
# print trainingfeatureList[1].shape
# l = [trainingfeatureList[0].shape[0], trainingfeatureList[1].shape]
#
# clf.fit(trainingfeatureList, trainingTag, l)


# --------------------------------- fetching data from a file ------------------------------------------

def features(sequence, i):
     yield "word=" + sequence[i].lower()
     if sequence[i].isupper():
         yield "Uppercase"

from seqlearn.datasets import load_conll
X_train, y_train, lengths_train = load_conll("train.txt", features)

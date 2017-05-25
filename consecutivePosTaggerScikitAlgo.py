import nltk
from scipy.sparse import coo_matrix, hstack
from scipy.sparse.construct import vstack
from sklearn.ensemble import AdaBoostClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

__author__ = 'devil'

bdt_real = AdaBoostClassifier(
            DecisionTreeClassifier(max_depth=2),
            n_estimators=600,
            learning_rate=1)

bdt_discrete = AdaBoostClassifier(
            DecisionTreeClassifier(max_depth=2),
            n_estimators=600,
            learning_rate=1.5,
            algorithm="SAMME")


def pos_features(sentence, i, history):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-tag"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
        features["prev-tag"] = history[i-1]
    return features

class ConsecutivePosTagger(nltk.TaggerI):

    count = 0
    count1 = 0

    def __init__(self, train_sents):
        train_set_featureset = []
        train_set_tags = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = pos_features(untagged_sent, i, history)
                train_set_featureset.append(featureset)
                train_set_tags.append(tag)
                history.append(tag)

        print train_set_featureset
        print train_set_tags

        #  bring in the model from scikit

        vec = DictVectorizer()
        X_tfidf = vec.fit_transform(train_set_featureset)
        print X_tfidf.shape
        # y_tfidf = vec.fit_transform(train_set_tags)

        # count_vect = CountVectorizer()
        # X_train_counts = count_vect.fit_transform(train_set_featureset)
        # y_train_counts = count_vect.fit_transform(train_set_tags)
        # tfidf_transformer = TfidfTransformer()
        # X_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        # y_tfidf = tfidf_transformer.fit_transform(y_train_counts)
        # print type(y_tfidf)

        bdt_real.fit(X_tfidf, train_set_tags)
        # bdt_discrete.fit(X_tfidf, train_set_tags)

        global count
        global count1
        count = X_tfidf.shape[0]
        count1 = X_tfidf.shape[1]

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = pos_features(sentence, i, history)
            fraturesetList = []
            fraturesetList.append(featureset)
            vec = DictVectorizer()
            X_tfidf = vec.fit_transform(fraturesetList)
            print "somthing ", X_tfidf.shape
            print fraturesetList
            print len(fraturesetList)
            print count
            print count1
            temp =[]
            for k in range(X_tfidf.shape[0]):
                temp1 = []
                temp1.append(0)
                temp.append(temp1)
            x = coo_matrix(temp)
            listForRow = []
            for k in range(count1):
                listForRow.insert(k, 0)
            y = coo_matrix(listForRow)
            print 'printing dimention of y', y.shape
            for k in range(count1 - X_tfidf.shape[1]):
                X_tfidf = hstack([X_tfidf, x]).toarray()
            print 'print dimention of X_tfidf', X_tfidf.shape
            for k in range(count - X_tfidf.shape[0]):
                X_tfidf = vstack([X_tfidf, y]).toarray()
            print 'checking if it works', X_tfidf.shape
            tag = bdt_real.predict(X_tfidf)
            history.append(tag)
        return zip(sentence, history)

test_input = []

with open('/home/devil/Projects/Thesis/OpenNLP/apache-opennlp-1.7.2/bin/testout.txt') as fp:
    for line in fp:
        temp = []
        for words in line.split():
            temp.append((words.split('_')[0], words.split('_')[1]))
        test_input.append(temp)

tagger = ConsecutivePosTagger(test_input)

print tagger.tag(['something'])
# print tagger.tag([('what'),('is'),('this')])
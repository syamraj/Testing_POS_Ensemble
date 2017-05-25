# import nltk
# from scipy.sparse import csr_matrix
# from scipy.sparse import coo_matrix, hstack
# from scipy.sparse.construct import vstack
# from sklearn.feature_extraction import DictVectorizer
# import numpy as np
#
# __author__ = 'devil'
#
# from nltk.corpus import brown
#
# # tagged_words = brown.tagged_words(categories='news')
# # tagged_sents = brown.tagged_sents(categories='news')
# # print tagged_sents[0]
# # print tagged_words[:5]
#
# test_input = []
#
# # Read from a file and make it in the format for passing to the consecutive functions
# with open('/home/devil/Projects/Thesis/OpenNLP/apache-opennlp-1.7.2/bin/testout.txt','rU') as fp:
#     for line in fp:
#         temp = []
#         for words in line.split():
#             temp.append((words.split('_')[0], words.split('_')[1]))
#         test_input.append(temp)
#
# print test_input[1]
#
# # testing dict to Scikit conversion
#
# pos_window = [{'suffix(3)': 'llo', 'prev-word': '<START>', 'suffix(2)': 'lo', 'prev-tag': '<START>', 'suffix(1)': 'o'}, {'suffix(3)': 'his', 'prev-word': 'Hello', 'suffix(2)': 'is', 'prev-tag': 'UH', 'suffix(1)': 's'}, {'suffix(3)': 'is', 'prev-word': 'this', 'suffix(2)': 'is', 'prev-tag': 'DT', 'suffix(1)': 's'}, {'suffix(3)': 'a', 'prev-word': 'is', 'suffix(2)': 'a', 'prev-tag': 'VBZ', 'suffix(1)': 'a'}, {'suffix(3)': 'est', 'prev-word': 'a', 'suffix(2)': 'st', 'prev-tag': 'DT', 'suffix(1)': 't'}, {'suffix(3)': 'I', 'prev-word': '<START>', 'suffix(2)': 'I', 'prev-tag': '<START>', 'suffix(1)': 'I'}, {'suffix(3)': 'am', 'prev-word': 'I', 'suffix(2)': 'am', 'prev-tag': 'PRP', 'suffix(1)': 'm'}, {'suffix(3)': 'ood', 'prev-word': 'am', 'suffix(2)': 'od', 'prev-tag': 'VBP', 'suffix(1)': 'd'}, {'suffix(3)': 'ion', 'prev-word': '<START>', 'suffix(2)': 'on', 'prev-tag': '<START>', 'suffix(1)': 'n'}, {'suffix(3)': 'of', 'prev-word': 'Inhibition', 'suffix(2)': 'of', 'prev-tag': 'NN', 'suffix(1)': 'f'}, {'suffix(3)': 'paB', 'prev-word': 'of', 'suffix(2)': 'aB', 'prev-tag': 'IN', 'suffix(1)': 'B'}, {'suffix(3)': 'ion', 'prev-word': 'NF-kappaB', 'suffix(2)': 'on', 'prev-tag': 'NNP', 'suffix(1)': 'n'}, {'suffix(3)': 'sed', 'prev-word': 'activation', 'suffix(2)': 'ed', 'prev-tag': 'NN', 'suffix(1)': 'd'}, {'suffix(3)': 'the', 'prev-word': 'reversed', 'suffix(2)': 'he', 'prev-tag': 'VBD', 'suffix(1)': 'e'}, {'suffix(3)': 'tic', 'prev-word': 'the', 'suffix(2)': 'ic', 'prev-tag': 'DT', 'suffix(1)': 'c'}, {'suffix(3)': 'ect', 'prev-word': 'anti-apoptotic', 'suffix(2)': 'ct', 'prev-tag': 'JJ', 'suffix(1)': 't'}, {'suffix(3)': 'of', 'prev-word': 'effect', 'suffix(2)': 'of', 'prev-tag': 'NN', 'suffix(1)': 'f'}, {'suffix(3)': 'min', 'prev-word': 'of', 'suffix(2)': 'in', 'prev-tag': 'IN', 'suffix(1)': 'n'}, {'suffix(3)': 'L-2', 'prev-word': '<START>', 'suffix(2)': '-2', 'prev-tag': '<START>', 'suffix(1)': '2'}, {'suffix(3)': 'ene', 'prev-word': 'IL-2', 'suffix(2)': 'ne', 'prev-tag': 'DT', 'suffix(1)': 'e'}, {'suffix(3)': 'ion', 'prev-word': 'gene', 'suffix(2)': 'on', 'prev-tag': 'NN', 'suffix(1)': 'n'}, {'suffix(3)': 'and', 'prev-word': 'expression', 'suffix(2)': 'nd', 'prev-tag': 'NN', 'suffix(1)': 'd'}, {'suffix(3)': 'ppa', 'prev-word': 'and', 'suffix(2)': 'pa', 'prev-tag': 'CC', 'suffix(1)': 'a'}, {'suffix(3)': 'ion', 'prev-word': 'NF-kappa', 'suffix(2)': 'on', 'prev-tag': 'NNP', 'suffix(1)': 'n'}, {'suffix(3)': 'ugh', 'prev-word': 'Bactivation', 'suffix(2)': 'gh', 'prev-tag': 'NNP', 'suffix(1)': 'h'}, {'suffix(3)': 'D28', 'prev-word': 'through', 'suffix(2)': '28', 'prev-tag': 'IN', 'suffix(1)': '8'}, {'suffix(3)': 'res', 'prev-word': 'CD28', 'suffix(2)': 'es', 'prev-tag': 'DT', 'suffix(1)': 's'}, {'suffix(3)': 'ive', 'prev-word': 'requires', 'suffix(2)': 've', 'prev-tag': 'VBZ', 'suffix(1)': 'e'}, {'suffix(3)': 'gen', 'prev-word': 'reactive', 'suffix(2)': 'en', 'prev-tag': 'JJ', 'suffix(1)': 'n'}, {'suffix(3)': 'ion', 'prev-word': 'oxygen', 'suffix(2)': 'on', 'prev-tag': 'NN', 'suffix(1)': 'n'}, {'suffix(3)': 'by', 'prev-word': 'production', 'suffix(2)': 'by', 'prev-tag': 'NN', 'suffix(1)': 'y'}, {'suffix(3)': 'ase', 'prev-word': 'by', 'suffix(2)': 'se', 'prev-tag': 'IN', 'suffix(1)': 'e'}, {'suffix(3)': 'ion', 'prev-word': '<START>', 'suffix(2)': 'on', 'prev-tag': '<START>', 'suffix(1)': 'n'}, {'suffix(3)': 'of', 'prev-word': 'Activation', 'suffix(2)': 'of', 'prev-tag': 'NN', 'suffix(1)': 'f'}, {'suffix(3)': 'the', 'prev-word': 'of', 'suffix(2)': 'he', 'prev-tag': 'IN', 'suffix(1)': 'e'}, {'suffix(3)': 'D28', 'prev-word': 'the', 'suffix(2)': '28', 'prev-tag': 'DT', 'suffix(1)': '8'}, {'suffix(3)': 'ace', 'prev-word': 'CD28', 'suffix(2)': 'ce', 'prev-tag': 'NNS', 'suffix(1)': 'e'}, {'suffix(3)': 'tor', 'prev-word': 'surface', 'suffix(2)': 'or', 'prev-tag': 'NN', 'suffix(1)': 'r'}, {'suffix(3)': 'des', 'prev-word': 'receptor', 'suffix(2)': 'es', 'prev-tag': 'NN', 'suffix(1)': 's'}, {'suffix(3)': 'a', 'prev-word': 'provides', 'suffix(2)': 'a', 'prev-tag': 'VBZ', 'suffix(1)': 'a'}, {'suffix(3)': 'jor', 'prev-word': 'a', 'suffix(2)': 'or', 'prev-tag': 'DT', 'suffix(1)': 'r'}, {'suffix(3)': 'ory', 'prev-word': 'major', 'suffix(2)': 'ry', 'prev-tag': 'JJ', 'suffix(1)': 'y'}, {'suffix(3)': 'nal', 'prev-word': 'costimulatory', 'suffix(2)': 'al', 'prev-tag': 'NN', 'suffix(1)': 'l'}, {'suffix(3)': 'for', 'prev-word': 'signal', 'suffix(2)': 'or', 'prev-tag': 'NN', 'suffix(1)': 'r'}, {'suffix(3)': 'T', 'prev-word': 'for', 'suffix(2)': 'T', 'prev-tag': 'IN', 'suffix(1)': 'T'}, {'suffix(3)': 'ell', 'prev-word': 'T', 'suffix(2)': 'll', 'prev-tag': 'NNP', 'suffix(1)': 'l'}, {'suffix(3)': 'ion', 'prev-word': 'cell', 'suffix(2)': 'on', 'prev-tag': 'NN', 'suffix(1)': 'n'}, {'suffix(3)': 'ing', 'prev-word': 'activation', 'suffix(2)': 'ng', 'prev-tag': 'NN', 'suffix(1)': 'g'}, {'suffix(3)': 'in', 'prev-word': 'resulting', 'suffix(2)': 'in', 'prev-tag': 'VBG', 'suffix(1)': 'n'}, {'suffix(3)': 'ced', 'prev-word': 'in', 'suffix(2)': 'ed', 'prev-tag': 'IN', 'suffix(1)': 'd'}, {'suffix(3)': 'ion', 'prev-word': 'enhanced', 'suffix(2)': 'on', 'prev-tag': 'JJ', 'suffix(1)': 'n'}, {'suffix(3)': 'of', 'prev-word': 'production', 'suffix(2)': 'of', 'prev-tag': 'NN', 'suffix(1)': 'f'}, {'suffix(3)': 'n-2', 'prev-word': 'of', 'suffix(2)': '-2', 'prev-tag': 'IN', 'suffix(1)': '2'}, {'suffix(3)': '-2)', 'prev-word': 'interleukin-2', 'suffix(2)': '2)', 'prev-tag': 'JJ', 'suffix(1)': ')'}, {'suffix(3)': 'and', 'prev-word': '(IL-2)', 'suffix(2)': 'nd', 'prev-tag': 'JJ', 'suffix(1)': 'd'}, {'suffix(3)': 'ell', 'prev-word': 'and', 'suffix(2)': 'll', 'prev-tag': 'CC', 'suffix(1)': 'l'}, {'suffix(3)': 'ion', 'prev-word': 'cell', 'suffix(2)': 'on', 'prev-tag': 'NN', 'suffix(1)': 'n'}, {'suffix(3)': 'In', 'prev-word': '<START>', 'suffix(2)': 'In', 'prev-tag': '<START>', 'suffix(1)': 'n'}, {'suffix(3)': 'ary', 'prev-word': 'In', 'suffix(2)': 'ry', 'prev-tag': 'IN', 'suffix(1)': 'y'}, {'suffix(3)': 'T', 'prev-word': 'primary', 'suffix(2)': 'T', 'prev-tag': 'JJ', 'suffix(1)': 'T'}, {'suffix(3)': 'tes', 'prev-word': 'T', 'suffix(2)': 'es', 'prev-tag': 'NNP', 'suffix(1)': 's'}, {'suffix(3)': 'we', 'prev-word': 'lymphocytes', 'suffix(2)': 'we', 'prev-tag': 'NNS', 'suffix(1)': 'e'}, {'suffix(3)': 'how', 'prev-word': 'we', 'suffix(2)': 'ow', 'prev-tag': 'PRP', 'suffix(1)': 'w'}, {'suffix(3)': 'hat', 'prev-word': 'show', 'suffix(2)': 'at', 'prev-tag': 'VBP', 'suffix(1)': 't'}, {'suffix(3)': 'D28', 'prev-word': 'that', 'suffix(2)': '28', 'prev-tag': 'IN', 'suffix(1)': '8'}, {'suffix(3)': 'ion', 'prev-word': 'CD28', 'suffix(2)': 'on', 'prev-tag': 'DT', 'suffix(1)': 'n'}, {'suffix(3)': 'ads', 'prev-word': 'ligation', 'suffix(2)': 'ds', 'prev-tag': 'NN', 'suffix(1)': 's'}, {'suffix(3)': 'to', 'prev-word': 'leads', 'suffix(2)': 'to', 'prev-tag': 'VBZ', 'suffix(1)': 'o'}, {'suffix(3)': 'the', 'prev-word': 'to', 'suffix(2)': 'he', 'prev-tag': 'TO', 'suffix(1)': 'e'}, {'suffix(3)': 'pid', 'prev-word': 'the', 'suffix(2)': 'id', 'prev-tag': 'DT', 'suffix(1)': 'd'}, {'suffix(3)': 'lar', 'prev-word': 'rapid', 'suffix(2)': 'ar', 'prev-tag': 'JJ', 'suffix(1)': 'r'}, {'suffix(3)': 'ion', 'prev-word': 'intracellular', 'suffix(2)': 'on', 'prev-tag': 'JJ', 'suffix(1)': 'n'}, {'suffix(3)': 'of', 'prev-word': 'formation', 'suffix(2)': 'of', 'prev-tag': 'NN', 'suffix(1)': 'f'}, {'suffix(3)': 'ive', 'prev-word': 'of', 'suffix(2)': 've', 'prev-tag': 'IN', 'suffix(1)': 'e'}, {'suffix(3)': 'gen', 'prev-word': 'reactive', 'suffix(2)': 'en', 'prev-tag': 'NN', 'suffix(1)': 'n'}, {'suffix(3)': 'tes', 'prev-word': 'oxygen', 'suffix(2)': 'es', 'prev-tag': 'NN', 'suffix(1)': 's'}, {'suffix(3)': '(', 'prev-word': 'intermediates', 'suffix(2)': '(', 'prev-tag': 'NNS', 'suffix(1)': '('}, {'suffix(3)': 'OIs', 'prev-word': '(', 'suffix(2)': 'Is', 'prev-tag': '-LRB-', 'suffix(1)': 's'}, {'suffix(3)': ')', 'prev-word': 'ROIs', 'suffix(2)': ')', 'prev-tag': 'NNS', 'suffix(1)': ')'}, {'suffix(3)': 'ich', 'prev-word': ')', 'suffix(2)': 'ch', 'prev-tag': '-RRB-', 'suffix(1)': 'h'}, {'suffix(3)': 'are', 'prev-word': 'which', 'suffix(2)': 're', 'prev-tag': 'WDT', 'suffix(1)': 'e'}, {'suffix(3)': 'red', 'prev-word': 'are', 'suffix(2)': 'ed', 'prev-tag': 'VBP', 'suffix(1)': 'd'}, {'suffix(3)': 'for', 'prev-word': 'required', 'suffix(2)': 'or', 'prev-tag': 'VBN', 'suffix(1)': 'r'}, {'suffix(3)': 'ted', 'prev-word': 'for', 'suffix(2)': 'ed', 'prev-tag': 'IN', 'suffix(1)': 'd'}, {'suffix(3)': 'ion', 'prev-word': 'CD28-mediated', 'suffix(2)': 'on', 'prev-tag': 'JJ', 'suffix(1)': 'n'}, {'suffix(3)': 'of', 'prev-word': 'activation', 'suffix(2)': 'of', 'prev-tag': 'NN', 'suffix(1)': 'f'}, {'suffix(3)': 'the', 'prev-word': 'of', 'suffix(2)': 'he', 'prev-tag': 'IN', 'suffix(1)': 'e'}, {'suffix(3)': 'ppa', 'prev-word': 'the', 'suffix(2)': 'pa', 'prev-tag': 'DT', 'suffix(1)': 'a'}, {'suffix(3)': 'ive', 'prev-word': 'NF-kappa', 'suffix(2)': 've', 'prev-tag': 'NNP', 'suffix(1)': 'e'}, {'suffix(3)': 'lex', 'prev-word': 'B/CD28-responsive', 'suffix(2)': 'ex', 'prev-tag': 'NNP', 'suffix(1)': 'x'}, {'suffix(3)': 'and', 'prev-word': 'complex', 'suffix(2)': 'nd', 'prev-tag': 'NN', 'suffix(1)': 'd'}, {'suffix(3)': 'L-2', 'prev-word': 'and', 'suffix(2)': '-2', 'prev-tag': 'CC', 'suffix(1)': '2'}, {'suffix(3)': 'ion', 'prev-word': 'IL-2', 'suffix(2)': 'on', 'prev-tag': 'JJ', 'suffix(1)': 'n'}]
# vec = DictVectorizer()
# pos_vectorized = vec.fit_transform(pos_window)
# print pos_vectorized.shape
# a = pos_vectorized
# b = [{'suffix(3)': 'hat', 'prev-word': '<START>', 'suffix(2)': 'at', 'prev-tag': '<START>', 'suffix(1)': 't'}]
# pos_vectorized1 = vec.fit_transform(b)
# print pos_vectorized1.shape
# temp = []
# for k in range(pos_vectorized1.shape[0]):
#     temp1 = []
#     temp1.append(0)
#     temp.append(temp1)
# x = coo_matrix(temp)
# listForRow = []
# for i in range(a.shape[1]):
#     listForRow.insert(i, 0)
# y = coo_matrix(listForRow)
# print x.shape
# print a.shape[1]
# for i in range(a.shape[1] - pos_vectorized1.shape[1]):
#     pos_vectorized1 = hstack([pos_vectorized1,x]).toarray()
#
# for i in range(a.shape[0] - pos_vectorized1.shape[0]):
#     pos_vectorized1 = vstack([pos_vectorized1, y]).toarray()
# print pos_vectorized1
# # print pos_vectorized1.shape
#
# # #  testing to change the shape of spare matrix
# # x = np.ones((3,5))
# # x = csr_matrix(x)
# # print x.toarray()
# # #
# # print 'last day breakthrough'
# # A = coo_matrix([[1, 2], [3, 4], [7,8]])
# # print A.shape[0]
# # temp = []
# # for k in range(A.shape[0]):
# #     temp1 = []
# #     temp1.append(0)
# #     temp.append(temp1)
# # print temp
# # x = coo_matrix(temp)
# # print x.shape
# # # B = coo_matrix([[0], [0]])
# # for i in range(5):
# #     A = hstack([A,x]).toarray()
# #
# # print hstack([A,x]).toarray()
# # print hstack([A,x]).toarray().shape
# #
# #
# # print 'testing today'
# #
# # A = coo_matrix([[1, 2], [3, 4]])
# # list_row = []
# # for i in range(15):
# #     list_row.insert(i,0)
# #
# # print list_row
#
# def features(sequence, i):
#      yield "word=" + sequence[i].lower()
#      if sequence[i].isupper():
#          yield "Uppercase"
#
# something = features('Syam', 2)
# print something

listOverAll = []

#
# with open('output.txt', 'rU') as fp:
#     for line in fp:
#         str = line.split(' ')
#         listEachLine = []
#         for i in str[:-1]:
#             if i.__contains__('_'):
#                 listEachLine.insert(len(listEachLine),(i.split('_')[0], i.split('_')[1]))
#         listOverAll.append(listEachLine)
#
# print listOverAll[0]


str = ""
str = str +"somethifnd"
str += "fuck"
print str
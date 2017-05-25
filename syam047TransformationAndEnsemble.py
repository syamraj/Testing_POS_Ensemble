from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier



# str = "Hello_UH this_DT is_VBZ a_DT test_NN"
str = "Inhibition_NN of_IN NF-kappaB_NNP activation_NN reversed_VBD the_DT anti-apoptotic_JJ effect_NN of_IN " \
      "isochamaejasmin_NN"

str = str.split(' ')
str1 = []
strWord = []
strWordToString = []
strTag = []
flag = 0
pos = 0
# keep 0 for padding.

for i in str:
    strWord.append(i.split('_')[0])
    strTag.append(i.split('_')[1])

for i in strWord:
    for j in strWord:
        if i == j:
            flag = 1
            pos = strWord.index(j)+1
    if flag == 0:
        strWordToString.append(strWord.index(i)+1)
    else:
        strWordToString.append(pos)

countOuterTag = 1


listOverall = []
newTagList = []

print strWord
print strTag
print strWordToString

for i in strTag:
    flag1 = 0
    count = 1
    listInside = [strWordToString.__getitem__(countOuterTag-1)]
    print i
    for j in strTag[countOuterTag:]:
        if i == j:
            print i,j
            print countOuterTag, count
            listInside.append(strWordToString.__getitem__((count + countOuterTag)-1))
        count += 1
    if not newTagList.__contains__(i):
        newTagList.append(i)
        flag1 = 1
    if flag1 == 1:
        listOverall.append(listInside)
    countOuterTag += 1


print strWord
print strTag
print strWordToString

mx = 0

for i in listOverall:
    if len(i) > mx:
        mx = len(i)

for i in listOverall:
    if len(i) < mx:
        for k in range(mx-len(i)):
            i.append(0)


print listOverall
print newTagList


X = listOverall
y = newTagList

# print y[:10]
# print X[1]
# # print X[2]
# print len(y)

n_split = 12

X_train, X_test = X[:n_split], X[n_split:]
y_train, y_test = y[:n_split], y[n_split:]



bdt_real = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=600,
    learning_rate=1)

bdt_discrete = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=600,
    learning_rate=1.5,
    algorithm="SAMME")

bdt_real.fit(X_train, y_train)
bdt_discrete.fit(X_train, y_train)

print bdt_real.predict([1, 4, 8, 10])
print bdt_discrete.predict([1, 0, 0, 0])



from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm

clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],
	[190,90,47],[175,64,39],
	[177,70,40],[159,55,37],[171,75,42],[181,85,43]]

Y = ['male','male','female','female','male','male','female','female',
	'female','male','male']

clf = clf.fit(X,Y)

prediction = clf.predict([[190,70,43]])

print(prediction)

neigh = KNeighborsClassifier()

neigh = neigh.fit(X,Y)
prediction = neigh.predict([[190,70,43]])

print(prediction)

gnb = GaussianNB()
gnb = gnb.fit(X,Y)
prediction = gnb.predict([[190,70,43]])

print(prediction)

SVM = svm.SVC()
SVM = SVM.fit(X,Y)
prediction = SVM.predict([[190,70,43]])

print(prediction)
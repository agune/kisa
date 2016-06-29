import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import neighbors

count_vect = CountVectorizer()

words = []
label = []
f = open('/Users/agun/Downloads/kbo2.csv', 'r')

csvReader = csv.reader(f)

for row in csvReader:
    words.append(row[2])
    label.append(row[1])
f.close()

X_train_counts = count_vect.fit_transform(words)
count_word = X_train_counts.toarray()

train_data = count_word[:10]
print(len(train_data))

test_data = count_word[10:]
train_label = label[:10]
test_label = label[10:]

clf = neighbors.KNeighborsClassifier(3, weights='distance')
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
fail = 0
for i in range(len(pre)) :
    if pre[i] != test_label[i] :
        fail = fail + 1

count = len(pre)

err = fail / count * 100

print("err: ", err, count)




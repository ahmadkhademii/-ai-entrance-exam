import pandas as pd 
import matplotlib.pyplot as plt 
import re 
from hazm import *


# read dataset 
df = pd.read_csv('data.csv')
# print(df.head())


# gain insight from data 
data = {'label':[1, -1], 
        'question': [len(df.loc[df.label == 1]), len(df.loc[df.label == -1])]}

df_count = pd.DataFrame(data, columns=['label', 'question'])
# print(df_count)


df_count.plot(x = 'label', y='question', kind='bar')
plt.show()


# cleaning dataset 
# stemmer = PorterStemmer()
normalizer = Normalizer()
stemmer = Stemmer()

corpus = [] 

for w in range(len(df['question'])):
    qst = df['question'][w]
    qst = re.sub('[^ا-ی]', ' ', qst)
    qst = normalizer.normalize(qst)
    qst = qst.split()
    qst = ' '.join(qst)
    corpus.append(qst)


# create word vector 
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer()
tf.fit(corpus)
# print(tf.vocabulary_)
X = tf.transform(corpus).toarray()

Y = df['label']


# train test split 
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=42)

# train model  decision tree
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)


# metrics 
from sklearn.metrics import confusion_matrix
confusion_m = confusion_matrix(y_test, y_pred)
print(confusion_m, '\n')

from sklearn.metrics import accuracy_score, precision_score, recall_score

acc = accuracy_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)

print('acc', acc, '\n')
print('prec', prec, '\n')
print('rec', rec, '\n')
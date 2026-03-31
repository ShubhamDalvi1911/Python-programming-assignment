'''
Part 3: Model Training
    1. Train individual models:
        Logistic Regression
        Decision Tree Classifier
    2. Combine them using:
        Hard Voting (majority rule)
        Soft Voting (average predicted probabilities)
'''
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


# Load the dataset using Pandas
fake_df = pd.read_csv("Fake.csv")
true_df = pd.read_csv("True.csv")

print("Some records of data : \n",fake_df.head())
print("Some records of data : \n",true_df.head())

fake_df['label'] = 0   # Fake 
true_df['label'] = 1   # True

df = pd.concat([fake_df, true_df], axis=0)

print("Combined Data:\n", df.head())

# Drop null values and select useful columns
print("Null Values are : \n", df.isnull().sum())

# Convert to lowercase 
df['title'] = df['title'].astype(str).str.lower()
df['text'] = df['text'].astype(str).str.lower()


# Feature & Target
df['content'] = df['title'] + " " + df['text']

X = df['content']
Y = df['label']

# Feature Extraction
vectorization = TfidfVectorizer()
X_trans = vectorization.fit_transform(X)

print("Some records after transformation : \n", X_trans[:5])

# Train individual models
X_train, X_test, Y_train, Y_test = train_test_split(X_trans,Y,test_size=0.2,random_state=42)

model_LR = LogisticRegression(max_iter=5000)
model_DT = DecisionTreeClassifier(random_state=42)

model_LR.fit(X_train,Y_train)
model_DT.fit(X_train,Y_train)

hard_model = VotingClassifier(
    estimators=[
        ('lr',model_LR),
        ('dt',model_DT),
    ],
    voting='hard'
)

soft_model = VotingClassifier(
    estimators=[
        ('lr',model_LR),
        ('dt',model_DT),
    ],
    voting='soft'
)

hard_model.fit(X_train,Y_train)
soft_model.fit(X_train,Y_train)

pred_hard = hard_model.predict(X_test)
pred_soft = soft_model.predict(X_test)

acc_hard = accuracy_score(pred_hard,Y_test)
acc_soft = accuracy_score(pred_soft,Y_test)

print("Hard Voting Accuracy ", acc_hard*100)
print("Soft Voting Accuracy ", acc_soft*100)


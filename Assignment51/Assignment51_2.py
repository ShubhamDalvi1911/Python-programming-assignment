'''
Part 2: Feature Extraction
    1. Use TF-IDF Vectorization to convert text into numerical features
'''
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

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
X = df[['title','text','subject','date']]

# Convert to lowercase 
df['title'] = df['title'].astype(str).str.lower()
df['text'] = df['text'].astype(str).str.lower()


# Feature & Target
X = df[['title' , 'text']]
Y = df['label']

# Feature Extraction
vectorization = TfidfVectorizer()

X_trans = vectorization.fit_transform(X)

print("Some records after transformation : \n", X_trans[:5])


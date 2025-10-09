import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import re
import string

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake["class"] = 0
true["class"] = 1

data = pd.concat([fake, true], axis=0)
data = data.drop(["title", "subject", "date"], axis=1)
data.reset_index(inplace=True)
data.drop(["index"], axis=1, inplace=True)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r"\W", " ", text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

data["text"] = data["text"].apply(clean_text)

x = data["text"]
y = data["class"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

vectorizer = TfidfVectorizer()
xv_train = vectorizer.fit_transform(x_train)
xv_test = vectorizer.transform(x_test)

lr = LogisticRegression()
lr.fit(xv_train, y_train)

pred_lr = lr.predict(xv_test)
print(classification_report(y_test, pred_lr))

joblib.dump(vectorizer, "vectorizer.jb")
joblib.dump(lr, "lr_model.jb")

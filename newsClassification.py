__author__ = 'devil'

# import statements

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer

# Categories of the files that should be loaded.
categories = ['alt.atheism', 'soc.religion.christian',
               'comp.graphics', 'sci.med']

# Fetching the files mentioned in the categories
twenty_train = fetch_20newsgroups(subset='train',
        categories=categories, shuffle=True, random_state=42)

print twenty_train.target_names

print("\n".join(twenty_train.data[2256].split("\n")[:3]))

# scikit need text data to be transformed to the numeric format.
count_vect = CountVectorizer()
print twenty_train.data
X_train_counts = count_vect.fit_transform(twenty_train.data)
print X_train_counts.shape
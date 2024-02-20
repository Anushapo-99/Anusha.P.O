import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Download the movie_reviews dataset
nltk.download('movie_reviews')
nltk.download('stopwords')
nltk.download('punkt')


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return ' '.join([word.lower() for word in words if word.isalpha() and word.lower() not in stop_words])

# Load positive and negative movie reviews
positive_reviews = [preprocess_text(movie_reviews.raw(fileid)) for fileid in movie_reviews.fileids('pos')]
negative_reviews = [preprocess_text(movie_reviews.raw(fileid)) for fileid in movie_reviews.fileids('neg')]


positive_labels = ['Positive'] * len(positive_reviews)
negative_labels = ['Negative'] * len(negative_reviews)

# Combining positive and negative reviews
reviews = positive_reviews + negative_reviews
labels = positive_labels + negative_labels

# Spliting datas into training and testing sets
train_reviews, test_reviews, train_labels, test_labels = train_test_split(reviews, labels, test_size=0.2, random_state=42)

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
train_features = vectorizer.fit_transform(train_reviews)
test_features = vectorizer.transform(test_reviews)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(train_features, train_labels)

# Evaluate the model on the test set
test_predictions = classifier.predict(test_features)
accuracy = accuracy_score(test_labels, test_predictions)
print(f"Accuracy: {accuracy:.2%}")

# Test the model with custom text
custom_text = "I really enjoyed this movie. The acting was great!"
custom_text_processed = preprocess_text(custom_text)
custom_feature = vectorizer.transform([custom_text_processed])
sentiment = classifier.predict(custom_feature)[0]
print(f"Predicted sentiment: {sentiment}")

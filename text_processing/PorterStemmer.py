from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
print(stemmer.stem('believes'))

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("believes"))

print(stemmer.stem(lemmatizer.lemmatize('buses')))
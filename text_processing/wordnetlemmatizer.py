from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cooking", pos="v"))
print(lemmatizer.lemmatize("cookbooks"))
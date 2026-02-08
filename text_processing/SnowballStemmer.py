from nltk.stem import SnowballStemmer

# Access the 'languages' tuple to see available languages
print("Available languages:")
print(SnowballStemmer.languages)

# Create a stemmer for Spanish
spanish_stemmer = SnowballStemmer('spanish')
stemmed_word = spanish_stemmer.stem('hola')
print(f"\nStem of 'hola': {stemmed_word}") # Output will be 'hol'

# Create a stemmer for English
english_stemmer = SnowballStemmer('english')
stemmed_word = english_stemmer.stem('hello')
print(f"Stem of 'hello': {stemmed_word}") # Output will be 'hello'

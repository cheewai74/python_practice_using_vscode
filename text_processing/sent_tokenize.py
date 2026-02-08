from nltk.tokenize import sent_tokenize
import nltk

nltk.download('punkt_tab')

para = "Hello World. It's good to see you. \
    Thanks for buying this book."

print(sent_tokenize(para))
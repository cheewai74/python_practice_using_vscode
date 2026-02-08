import nltk.data

para = "Hello World. It's good to see you. \
    Thanks for buying this book."

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
spanish_tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
print(tokenizer.tokenize(para))
print(spanish_tokenizer.tokenize('Hola amigo. Estoy bien.'))
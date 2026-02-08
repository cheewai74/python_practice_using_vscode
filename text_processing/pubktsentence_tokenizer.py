import nltk
nltk.download('webtext')

from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext

text = webtext.raw('C:\\python_sandbox\\resources\\overheard.txt')
sent_tokenizer = PunktSentenceTokenizer(text)
sents1 = sent_tokenizer.tokenize(text)
print(sents1[0])
sents2 = sent_tokenizer.tokenize(text)
print(sents2[0])
print(sents2[2])
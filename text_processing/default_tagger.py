from nltk.tag import DefaultTagger
from nltk.tag import untag

tagger = DefaultTagger('NN')
print(tagger.tag(["Hello", "World"]))
print(untag(tagger.tag(["Hello", "World"])))
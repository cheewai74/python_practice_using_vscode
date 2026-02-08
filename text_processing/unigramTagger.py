from nltk.tag import UnigramTagger
from nltk.corpus import treebank


train_sents = treebank.tagged_sents()[:3000]
tagger = UnigramTagger(train_sents)
print(treebank.sents()[0])
print("=========================================")
print(treebank.tag()[0])
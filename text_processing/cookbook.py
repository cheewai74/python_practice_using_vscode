from nltk.corpus import wordnet

syn = wordnet.synsets('cookbook')[0]
print(syn.name())
print(syn.definition())
print(wordnet.synset('cookbook.n.01'))
print(wordnet.synsets('cooking')[0].examples())

print(syn.hypernyms())
print(syn.hypernyms()[0].hyponyms())
print(syn.root_hypernyms())
print(syn.hypernym_paths())
print(syn.pos())
print(len(wordnet.synsets('great')))
print(len(wordnet.synsets('great', pos='n')))
print(len(wordnet.synsets('great', pos='a')))
from nltk.corpus.reader import WordListCorpusReader
reader = WordListCorpusReader(',', ['wordlist'])
print(reader.words())
print(reader.fileids())
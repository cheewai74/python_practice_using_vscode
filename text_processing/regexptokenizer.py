from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\s+', gaps=True)
print(tokenizer.tokenize("Can't is a contraction."))
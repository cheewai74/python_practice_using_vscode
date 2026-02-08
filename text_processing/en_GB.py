import enchant

# The corrected line:
dUS = enchant.Dict('en_US')
print(dUS.check('nltk'))

print(dUS.check('theater'))
dUS = enchant.Dict('en_GB')
print(dUS.check('nltk'))

print(dUS.check('theater'))
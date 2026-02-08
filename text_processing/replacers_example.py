from replacers import SpellingReplacer # type: ignore
us_replacer = SpellingReplacer('en_US')
print(us_replacer.replace('theater'))

gb_replacer = SpellingReplacer('en_GB')
print(gb_replacer.replace('theater'))

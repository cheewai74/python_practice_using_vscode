import re

# ^ Matches the expression to its right, at the start of a string before it experiences a line break
print(re.search(r"^x","xenon"))

# $ Matches the expression to its left, at the end of a string before it experiences a line break
print(re.search(r"s$","geeks"))

# + Matches the expression to its left 1 or more times.
print(re.search(r"9+","289908"))
#  {p} Matches the expression to its left p times, and not less.
print(re.search(r"\d{3}","hello1234"))

# \s Matches whitespace characters, which also include the \t, \n, \r, and space characters.
print(re.search(r"\s","xenon is a gas"))
# \D Matches any non-digits.
# \d Matches digits, from 0-9.
print(re.search(r"\D+\d*","123geeks123"))

# [^ab5] Adding ^ excludes any character in the set. Here, it matches characters that are not a, b, or 5.
print(re.search(r"[^abc]","abcde"))
# [a-z] Matches any alphabet from a to z.
print(re.search(r"[a-p]","xenon"))

# (?:A) Matches the expression as represented by A, but cannot be retrieved afterwards.
example = (re.search(r"(?:AB)","ACABC"))
print(example)
print(example.groups())

result = re.search(r"(\w*), (\w*)","geeks, best")
print(result.groups())

#A(?=B)  This matches the expression A only if it is followed by B. (Positive look ahead assertion)
print(re.search(r"z(?=a)", "pizza"))

# A(?!B) This matches the expression A only if it is not followed by B. (Negative look ahead assertion)
print(re.search(r"z(?!a)", "pizza"))

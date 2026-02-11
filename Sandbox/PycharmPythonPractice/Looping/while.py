secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt: break
    if count == 3: continue
    pw = input("What's the secret word? ")
else: # will only execute when the condition nolonger true and the loops exits normally.
    auth = True

print("Authorized" if auth else "calling the Singapore Police")
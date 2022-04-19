s = input()
pattern = input()

s_ = ''
for letter in s:
    if letter.isalpha():
        s_ += letter

if s_.count(pattern):
    print(1)
else:
    print(0)

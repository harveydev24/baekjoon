l, r = input().split()
s = input()

t = 0

left = {
    'q': (0, 0),
    'w': (0, 1),
    'e': (0, 2),
    'r': (0, 3),
    't': (0, 4),
    'a': (1, 0),
    's': (1, 1),
    'd': (1, 2),
    'f': (1, 3),
    'g': (1, 4),
    'z': (2, 0),
    'x': (2, 1),
    'c': (2, 2),
    'v': (2, 3),
}

right = {
    'y': (0, 0),
    'u': (0, 1),
    'i': (0, 2),
    'o': (0, 3),
    'p': (0, 4),
    'h': (1, 0),
    'j': (1, 1),
    'k': (1, 2),
    'l': (1, 3),
    'b': (2, -1),
    'n': (2, 0),
    'm': (2, 1),
}


for letter in s:
    t += 1
    if left.get(letter):
        t += abs(left[l][0]-left[letter][0])+abs(left[l][1]-left[letter][1])
        l = letter
    else:
        t += abs(right[r][0]-right[letter][0]) + \
            abs(right[r][1]-right[letter][1])
        r = letter

print(t)

# class Node:
#     def __init__(self, key, data=False):
#         self.key = key
#         self.data = data
#         self.children = {}


# class Trie:
#     def __init__(self):
#         self.head = Node(None)

#     def insert(self, word: str) -> None:
#         curr = self.head
#         for letter in word:
#             if curr.children.get(letter) == None:
#                 curr.children[letter] = Node(letter)
#             curr = curr.children[letter]
#         curr.data = True

#     def search(self, word: str) -> bool:
#         curr = self.head
#         for letter in word:
#             if curr.children.get(letter):
#                 curr = curr.children[letter]
#             else:
#                 return False
#         if curr.data:
#             return True
#         else:
#             return False

#     def startsWith(self, prefix: str) -> bool:
#         curr = self.head
#         for letter in prefix:
#             if curr.children.get(letter):
#                 curr = curr.children[letter]
#             else:
#                 return False
#         return True

#         # Your Trie object will be instantiated and called as such:
#         # obj = Trie()
#         # obj.insert(word)
#         # param_2 = obj.search(word)
#         # param_3 = obj.startsWith(prefix)


t = int(input())


def insert(trie, word):
    curr = trie
    for letter in word:
        if letter not in curr:
            curr[letter] = {}
        curr = curr[letter]
    curr['data'] = True


def startsWith(trie, word):
    curr = trie
    for i in range(len(word)):
        if word[i] in curr:
            curr = curr[word[i]]
            if i != len(word)-1 and curr.get('data'):
                return True
    return False


for _ in range(t):
    n = int(input())
    phone_numbers = [input() for _ in range(n)]

    trie = {}
    for number in phone_numbers:
        insert(trie, number)

    check = True

    for number in phone_numbers:
        if startsWith(trie, number):
            check = False
            break

    if check:
        print('YES')
    else:
        print("NO")

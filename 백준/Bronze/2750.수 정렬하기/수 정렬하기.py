N = int(input())
numbers=list()
for i in range(N):
  numbers.append(int(input()))

numbers.sort()

while numbers:
  print(numbers.pop(0))
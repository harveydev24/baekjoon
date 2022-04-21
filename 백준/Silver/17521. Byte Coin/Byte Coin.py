n, w = map(int, input().split())
data = []
for _ in range(n) :
  data.append(int(input()))

coin = 0
for i in range(n-1) :
  if data[i] < data[i+1] :
    if w // data[i] > 0 :
      coin = w // data[i]
      w -= data[i] * coin
  elif data[i] > data[i-1] :
    w += data[i] * coin
    coin = 0

if coin > 0 :
  w += coin * data[-1]

print(w)
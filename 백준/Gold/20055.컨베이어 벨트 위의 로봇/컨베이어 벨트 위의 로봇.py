N, K = map(int, input().split())
array = list(map(int, input().split()))
robots = [0]*(N)

def rotate(lst):
    last = lst[-1]
    for i in range(len(lst)-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = last
    return lst

def move_robot():
    robots[N-1] = 0
    for i in range(N-2, -1, -1):
        if robots[i] == 1 and robots[i+1] == 0 and array[i+1] >= 1:
            robots[i+1] = 1
            robots[i] = 0
            array[i+1] -= 1
    robots[N-1] = 0
                

def put_robot():
    if array[0] >= 1:
        robots[0] = 1
        array[0] -= 1

cnt = 0
while True:
    robots = rotate(robots)
    array = rotate(array)
    move_robot()
    put_robot()
    cnt += 1
    if array.count(0) >= K:
        print(cnt)
        exit(0)
N = int(input())
array = [-1] + list(map(int, input().split()))
student_num = int(input())

for _ in range(student_num):
    gender, number = map(int, input().split())

    if gender == 1: #boy
        i = number
        array[i] = abs(array[i]-1)
        i += number
        while i <= N:
            array[i] = abs(array[i]-1)
            i += number
    else: # girl
        i = 1
        array[number] = abs(array[number]-1)
        while number+i <= N and number-i >= 1:
            if array[number+i] == array[number-i]:
                array[number+i] = abs(array[number+i]-1)
                array[number-i] = abs(array[number-i]-1)
                i += 1
            else:
                break


for i in range(1, N+1):
    print(array[i], end = ' ')
    if i%20 == 0:
        print()

    
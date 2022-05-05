import sys

# 반복해서 출력되는 예제는 미리 배열에 담아준다.
arr = [
        '"재귀함수가 뭔가요?"',
        '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
        '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
        '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
    ]

count = 0
def lecturer_says(a, count): 
    # 카운트 수가 증가할 때마다 '_' 를 4개씩 추가
    under_bar = '_' * (4 * count)
    # count 수와 input 값이 동일해진다면 재귀 함수를 종료 시키고 아래 값을 반환한다.
    if a == count:
        print(under_bar + '"재귀함수가 뭔가요?"')
        print(under_bar + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(under_bar+ "라고 답변하였지.")
        return

    for i in arr:       
        print(under_bar + i)
    count += 1
   
    lecturer_says(a, count)
    # 재귀함수 리턴 후 순차적으로 출력되는 값
    print(under_bar+ "라고 답변하였지.")

a = int(sys.stdin.readline().rstrip())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
lecturer_says(a, count)
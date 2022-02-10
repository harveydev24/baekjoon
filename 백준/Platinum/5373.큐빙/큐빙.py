T = int(input())

def clockwise(d):
    cube[d][0][0],cube[d][1][0],cube[d][2][0],cube[d][2][1],cube[d][2][2],cube[d][1][2],cube[d][0][2],cube[d][0][1]=cube[d][2][0],cube[d][2][1],cube[d][2][2],cube[d][1][2],cube[d][0][2],cube[d][0][1],cube[d][0][0],cube[d][1][0]

def counter_clockwose(d):
    cube[d][0][0],cube[d][0][1],cube[d][0][2],cube[d][1][2],cube[d][2][2],cube[d][2][1],cube[d][2][0],cube[d][1][0]=cube[d][0][2],cube[d][1][2],cube[d][2][2],cube[d][2][1],cube[d][2][0],cube[d][1][0],cube[d][0][0],cube[d][0][1]

def U(sign):
    if sign=='+':
        cube['front'][0],cube['right'][0],cube['back'][0],cube['left'][0]=cube['right'][0],cube['back'][0],cube['left'][0],cube['front'][0]
        clockwise('up')
    else:
        cube['front'][0],cube['left'][0],cube['back'][0],cube['right'][0]=cube['left'][0],cube['back'][0],cube['right'][0],cube['front'][0]
        counter_clockwose('up')

def D(sign):
    if sign=='+':
        cube['front'][2],cube['left'][2],cube['back'][2],cube['right'][2]=cube['left'][2],cube['back'][2],cube['right'][2],cube['front'][2]
        clockwise('down')
    else:
        cube['front'][2],cube['right'][2],cube['back'][2],cube['left'][2]=cube['right'][2],cube['back'][2],cube['left'][2],cube['front'][2]
        counter_clockwose('down')

def F(sign):
    if sign=='+':
        cube['up'][2],cube['left'][2][2],cube['left'][1][2],cube['left'][0][2],cube['down'][0],cube['right'][2][0],cube['right'][1][0],cube['right'][0][0]=[cube['left'][2][2],cube['left'][1][2],cube['left'][0][2]],cube['down'][0][2],cube['down'][0][1],cube['down'][0][0],[cube['right'][2][0],cube['right'][1][0],cube['right'][0][0]],cube['up'][2][2],cube['up'][2][1],cube['up'][2][0]
        clockwise('front')
    else: 
        cube['up'][2],cube['right'][0][0],cube['right'][1][0],cube['right'][2][0],cube['down'][0][2],cube['down'][0][1],cube['down'][0][0],cube['left'][2][2],cube['left'][1][2],cube['left'][0][2]=[cube['right'][0][0],cube['right'][1][0],cube['right'][2][0]],cube['down'][0][2],cube['down'][0][1],cube['down'][0][0],cube['left'][2][2],cube['left'][1][2],cube['left'][0][2],cube['up'][2][0],cube['up'][2][1],cube['up'][2][2]
        counter_clockwose('front')
def B(sign):
    if sign=='+': 
        cube['up'][0][0],cube['up'][0][1],cube['up'][0][2],cube['right'][0][2],cube['right'][1][2],cube['right'][2][2],cube['down'][2][2],cube['down'][2][1],cube['down'][2][0],cube['left'][2][0],cube['left'][1][0],cube['left'][0][0]=cube['right'][0][2],cube['right'][1][2],cube['right'][2][2],cube['down'][2][2],cube['down'][2][1],cube['down'][2][0],cube['left'][2][0],cube['left'][1][0],cube['left'][0][0],cube['up'][0][0],cube['up'][0][1],cube['up'][0][2]
        clockwise('back')
    else:
        cube['up'][0][0],cube['up'][0][1],cube['up'][0][2],cube['left'][2][0],cube['left'][1][0],cube['left'][0][0],cube['down'][2][2],cube['down'][2][1],cube['down'][2][0],cube['right'][0][2],cube['right'][1][2],cube['right'][2][2]=cube['left'][2][0],cube['left'][1][0],cube['left'][0][0],cube['down'][2][2],cube['down'][2][1],cube['down'][2][0],cube['right'][0][2],cube['right'][1][2],cube['right'][2][2],cube['up'][0][0],cube['up'][0][1],cube['up'][0][2]
        counter_clockwose('back')
def L(sign):
    if sign=='+':
        cube['up'][0][0],cube['up'][1][0],cube['up'][2][0],cube['back'][2][2],cube['back'][1][2],cube['back'][0][2],cube['down'][0][0],cube['down'][1][0],cube['down'][2][0],cube['front'][0][0],cube['front'][1][0],cube['front'][2][0]=cube['back'][2][2],cube['back'][1][2],cube['back'][0][2],cube['down'][0][0],cube['down'][1][0],cube['down'][2][0],cube['front'][0][0],cube['front'][1][0],cube['front'][2][0],cube['up'][0][0],cube['up'][1][0],cube['up'][2][0]
        clockwise('left')
    else:
        cube['up'][0][0],cube['up'][1][0],cube['up'][2][0],cube['front'][0][0],cube['front'][1][0],cube['front'][2][0],cube['down'][0][0],cube['down'][1][0],cube['down'][2][0],cube['back'][2][2],cube['back'][1][2],cube['back'][0][2]=cube['front'][0][0],cube['front'][1][0],cube['front'][2][0],cube['down'][0][0],cube['down'][1][0],cube['down'][2][0],cube['back'][2][2],cube['back'][1][2],cube['back'][0][2],cube['up'][0][0],cube['up'][1][0],cube['up'][2][0]
        counter_clockwose('left')
def R(sign):
    if sign=='+':
        cube['up'][2][2],cube['up'][1][2],cube['up'][0][2],cube['front'][2][2],cube['front'][1][2],cube['front'][0][2],cube['down'][2][2],cube['down'][1][2],cube['down'][0][2],cube['back'][0][0],cube['back'][1][0],cube['back'][2][0]=cube['front'][2][2],cube['front'][1][2],cube['front'][0][2],cube['down'][2][2],cube['down'][1][2],cube['down'][0][2],cube['back'][0][0],cube['back'][1][0],cube['back'][2][0],cube['up'][2][2],cube['up'][1][2],cube['up'][0][2]
        clockwise('right')
    else:
        cube['up'][2][2],cube['up'][1][2],cube['up'][0][2],cube['back'][0][0],cube['back'][1][0],cube['back'][2][0],cube['down'][2][2],cube['down'][1][2],cube['down'][0][2],cube['front'][2][2],cube['front'][1][2],cube['front'][0][2]=cube['back'][0][0],cube['back'][1][0],cube['back'][2][0],cube['down'][2][2],cube['down'][1][2],cube['down'][0][2],cube['front'][2][2],cube['front'][1][2],cube['front'][0][2],cube['up'][2][2],cube['up'][1][2],cube['up'][0][2]
        counter_clockwose('right')

def rotate(order):
    if order[0]=='U':
        U(order[1])
    elif order[0]=='D':
        D(order[1])
    elif order[0]=='F':
        F(order[1])
    elif order[0]=='B':
        B(order[1])
    elif order[0]=='L':
        L(order[1])
    else:
        R(order[1])
for test_case in range(T):
    cube = {
        'up': [['w','w','w'],['w','w','w'],['w','w','w']],
        'down': [['y','y','y'],['y','y','y'],['y','y','y']],
        'front': [['r','r','r'],['r','r','r'],['r','r','r']],
        'back': [['o','o','o'],['o','o','o'],['o','o','o']],
        'left': [['g','g','g'],['g','g','g'],['g','g','g']],
        'right': [['b','b','b'],['b','b','b'],['b','b','b']]
    }

    n = int(input())
    orders = list(input().split())
    for order in orders:
        rotate(order)

    for item in cube['up']:
        print(''.join(item))
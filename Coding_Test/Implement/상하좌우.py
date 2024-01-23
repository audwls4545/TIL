## Q. 계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하시오.
## 입력조건
## 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1<=N<=100)
## 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다.(1<=이동횟수<=100)
## 출력조건
## 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백으로 구분하여 출력한다.
# L: 0,-1
# R: 0,1
# U: -1,0
# D: 1,0

def move():
    n = int(input())
    move_plan = list(map(str, input().split()))
    x, y = 1, 1

    for move in move_plan:
        if move == "L" and y != 1:
            y -= 1
        elif move == "R" and y != n:
            y += 1
        elif move == "U" and x != 1:
            x -= 1
        elif move == "D" and x != n:
            x += 1
        else:
            continue

    print(x,y)


move()

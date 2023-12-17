## Q. 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다. 동빈이는 최대 몇개의 모험가 그룹을 만들수 있는가?
## 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.
## 입력조건
## 첫째 줄에 모험가의 수 N이 주어집니다.(1<=N<=100,000)
## 둘째 줄에 각 모험가의 동포도의 값을 N 이하의 자연수로 주어지며, 각 지연수는 공백으로 구분합니다.
## 출력조건
## 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.

def count():
    N = int(input())
    group = list(map(int, input().split()))

    group.sort()

    team = 0
    count = 0
    for panic in group:
        count += 1
        if count >= panic:
            team += 1
            count = 0

    return team 

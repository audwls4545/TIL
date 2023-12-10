## Q. 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임
## 규칙은 N * M 행렬 각 행중에서 가장 높은 숫자를 뽑기
## 입력조건
## 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.(1 <= N, M <= 100)
## 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수이다.
## 출력조건
## 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

def game():
    num = 0
    num_list = []
    N, M = map(int, input().split())

    for _ in range(N):
        num_list.append(list(map(int, input().split())))
    
    print(num_list)

    for i, check in enumerate(num_list):
        min_num = min(check)
        if i == 0:
            num = min_num
        else:
            if num < min_num:
                num = min_num

    return num
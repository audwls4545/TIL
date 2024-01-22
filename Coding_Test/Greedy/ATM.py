## Q. 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.
## 입력조건
## 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)
## 출력 조건
## 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

def test():
    n = int(input())
    p = list(map(int, input().split()))
    num = 0
    count = 0

    p.sort()

    while True:
        if count == n:
            break
        else:
            for temp in range(count+1):
                num += p[temp]
            count += 1
            
    print(num)


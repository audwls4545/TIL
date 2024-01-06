## Q. 두 수 A와 B가 주어졌을 때, 상근이는 이 두수를 더하려고 한다. 구할 수 있는 두수의 합 중, 최솟값과 최댓값을 구해라.
## 입력조건
## 첫째 줄에 두 정수 A와 B가 주어진다.(1<=A,B<=1,000,000)
## 출력조건
## 첫째 줄에 상근이가 구할 수 있는 두 수의 합 중 최솟값과 최댓값을 출력한다.

def hub():

    A, B = map(str, input().split())

    min_hub = int(A.replace('6','5')) + int(B.replace('6','5'))

    max_hub = int(A.replace('5','6')) + int(B.replace('5','6'))

    print(min_hub, max_hub)

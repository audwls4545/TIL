## Q. 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K(최대 K번까지만 반복 사용 가능)가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력
## 입력조건
## 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분
## 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어짐
## 입력으로 주어지는 K는 항상 M보다 작거나 같음
## 출력 조건
## 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력

def large_num_plus():

    sum = 0

    N, M, K = map(int, input().split())

    num_list = list(map(int, input().split()))

    num_list.sort(reverse=True) # 내림차순 정렬

    first = num_list[0] #가장 큰수
    second = num_list[1] # 두번째로 큰수

    for i in range(1, M+1):
        if i%K == 0:
            sum += second
        else:
            sum += first
    
    return sum

result = 0
result = large_num_plus()

print(result)
    
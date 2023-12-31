## Q. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수 구하기.(N은 항상 10의 배수, 500원, 100원, 50원, 10원)

## 그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘이므로
## '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 제시
## 대부분의 그리디 알고리즘 문제에서는 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정단하지 검토할 수 있어야 답을 도출할 수 있음

def change_money(N):
    num = 0 #동전의 최소 개수
    
    while N != 0:
        if N >= 500:
            num += N // 500
            N = N % 500
        elif N >= 100:
            num += N // 100
            N = N % 100
        elif N >= 50:
            num += N // 50
            N = N % 50
        else:
            num += N // 10
            N = N % 10
    
    return num


def other_change_money(N):
    num = 0 #동전의 최소 개수
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        num += N // coin
        N %= coin
    
    return num


## 가장 큰 화폐 단위부터 돈을 거슬러 주는 것
## 화폐의 종류만큼 반복을 수행해야 함
## 화폐의 종류가 K개라고 할때 시간 복잡도는 O(K)
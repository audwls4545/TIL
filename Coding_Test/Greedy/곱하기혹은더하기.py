## Q. 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때,
##    왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
##    'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오. 
## 일반적인 계산 방식과는 달리 모든 연산은 왼쪽에서부터 순서대로 이루어짐
## 입력조건
## 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다.(1<=S의길이<=20)
## 출력조건
## 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

def cal():
    S = input()

    S_list = list(S)
    max_num = 0
    check = 0

    for temp in S_list:
        print(temp)
        int_temp = int(temp)
        if int_temp == 0:
            max_num += int_temp
        else:
            if max_num == 0:
                max_num = 1
                max_num *= int_temp
            else:
                max_num *= int_temp
    
    return max_num

        
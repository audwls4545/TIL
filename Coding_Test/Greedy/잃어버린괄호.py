## Q. 괄호를 적절히 쳐서 이 식의 값을 최소로 만드느 프로그램을 작성하시오.
## 입력조건
## 첫째 줄에 식이 주어진다. 식은 '0'~'9', '+' 그리고 '-'만으로 이루어져 있고
## 가장 처음과 마지막 문자는 숫자이다.
## 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
## 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.
## 출력조건
## 첫째 줄에 정답을 출력한다.

def lost_bracket():
    bracket = []
    result_list = []
    left_wing, right_wing = 0, 0
    number = ''
    check = ''
    result = []

    temp = str(input())

    bracket = list(temp)

    for i, num in enumerate(bracket):
        if num == '-':
            if left_wing == 0:
                result_list.append('-')
                result_list.append('(')
                left_wing = 1
            elif left_wing == 1:
                result_list.append(')')
                result_list.append('-')
                result_list.append('(')
                left_wing = 2
            else:
                result_list.append(')')
                result_list.append('-')
                result_list.append('(')
                left_wing = 1
        else:
            result_list.append(num)

    if left_wing != 0:
        result_list.append(')')

    for j in result_list:
        if j.isdigit():
            check += str(j)
        else:
            if len(check) != 0:
                int_check = int(check)
                check = str(int_check)
                result.append(check)
                check = ''
            result.append(j)
    if len(check) != 0:
        int_check = int(check)
        check = str(int_check)
        result.append(check)

    number = ''.join(result)

    result_num = 0
    result_num = eval(number)
    print(result_num)

def lost_bracket2():
    num = input().split('-')

    sum = 0
    for temp in num[0].split('+'):
        sum += int(temp)

    for i in num[1:]:
        for j in i.split('+'):
            sum -= int(j)

    print(sum)

##잔디테스트
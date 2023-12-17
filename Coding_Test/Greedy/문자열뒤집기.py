## Q. 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 합니다. 최소 횟수를 출력하세요.
## 입력조건
## 첫째 줄에 0과 1로만 이루어진 문자열 S가 주어집니다. S의 길이는 100만보다 작습니다.
## 출력조건
## 첫째 줄에 다솜이가 해야 하는 행동의 최소 횟수를 출력합니다.

# def cal():
#     S = input()
#     S_list = list(S)
    
#     zero_count = S_list.count("0")
#     one_count = S_list.count("1")

#     num_list = []
#     count = 0
#     print(zero_count, one_count)

#     if zero_count >= one_count:
#         for i, temp in enumerate(S_list):
#             if temp == "0" and len(num_list) == 0:
#                 pass
#             elif temp == "0" and len(num_list) != 0:
#                 count += 1
#                 num_list = []
#             elif temp == "1":
#                 num_list.append(i)
#     else:
#         for i, temp in enumerate(S_list):
#             if temp == "1" and len(num_list) == 0:
#                 pass
#             elif temp == "1" and len(num_list) != 0:
#                 count += 1
#                 num_list = []
#             elif temp == "0":
#                 num_list.append(i)
    
#     if len(num_list) != 0:
#         count += 1

#     return count

def cal():
    S = input()
    zero_list = list(map(str, S.split("1")))
    one_list = list(map(str, S.split("0")))

    result = 0
    
    zero_list = ' '.join(zero_list).split()
    one_list = ' '.join(one_list).split()
    if len(zero_list) >= len(one_list):
        result = len(one_list)
    else:
        result = len(zero_list)

    return result

# 프로그래머스 코딩테스트 - 수식최대화(Lv2)

import re
from itertools import permutations

def calc(permutation, n, exp):
    if n == len(permutation):
        return str(exp)
    if permutation[n] == "*":
        split = exp.split("*")
        temp = []
        for s in split:
            temp.append(calc(permutation, n + 1, s))
            print(temp)
        return str(eval("*".join(temp)))

    if permutation[n] == "+":
        split = exp.split("+")
        temp = []
        for s in split:
            temp.append(calc(permutation, n + 1, s))
            print(temp)
        return str(eval("+".join(temp)))

    if permutation[n] == "-":
        split_data = exp.split("-")
        temp = []
        for s in split_data:
            temp.append(calc(permutation, n + 1, s))
            print(temp)
        return str(eval("-".join(temp)))

def solution(expression):
    sum_list = []
    operator = re.findall(r'\D', expression)
    search = list(set(operator))
    permutation = permutations(search, len(search))
    for p in permutation:
        print(p)
        cal = abs(int(calc(p, 0, expression)))
        print(cal)
        sum_list.append(cal)
        
    answer = max(sum_list)
    return answer
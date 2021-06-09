# 프로그래머스 코딩테스트 - 멀쩡한 사각형(Lv2)

from math import gcd

def solution(w,h):
    a = w / gcd(w,h)
    b = h / gcd(w,h)
    answer = (w*h) - ((a+b-1) * (w/a))
    return answer
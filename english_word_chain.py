# 프로그래머스 코딩테스트 - 영어 끝말잇기(Lv2)

from itertools import cycle

def solution(n, words):
    n_list = list(range(1,n+1))
    overlap_list = [words[0]]
    turn_list = []
    answer = []
    
    if words == []:
        answer = [0,0]
        return answer
    
    for i, j in zip(words, cycle(n_list)):
        print(i, j)
        if i == words[0]:
            turn_list.append(j)
            pass
        elif i in overlap_list:
            turn_list.append(j)
            answer.append(j)
            answer.append(turn_list.count(j))
            break
        elif i[0] != overlap_list[-1][-1]:
            turn_list.append(j)
            answer.append(j)
            answer.append(turn_list.count(j))
            break
        else:
            overlap_list.append(i)
            turn_list.append(j)
            if i == words[-1]:
                answer = [0,0]
    
    if answer == [] and words[-1] in overlap_list[:-1]:
        answer.append(turn_list[-1])
        answer.append(turn_list.count(turn_list[-1]))
        
    return answer
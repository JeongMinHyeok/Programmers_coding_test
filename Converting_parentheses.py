# 참고 블로그 : https://this-programmer.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Level2%ED%8C%8C%EC%9D%B4%EC%8D%AC3python3-%EA%B4%84%ED%98%B8-%EB%B3%80%ED%99%98

def solution(p):
    answer = ''
    counter = 0
    counter2 = 0
    u = ''
    v = ''
    if p == '':
        return answer
    
    for i in p:
        if i == '(':
            counter += 1
            u += i
        else :
            counter -= 1
            u += i
        if counter == 0:
            v = p[len(u):]
            correct = True
            for j in u:
                if j == '(':
                    counter2 += 1
                else :
                    counter2 -= 1
                if counter2 < 0:
                    correct = False
            if correct :
                return u + solution(v)
            else:
                new_u = ''
                for k in u[1:-1]:
                    if k == '(':
                        new_u += ')'
                    else:
                        new_u += '('
                answer = '(' + solution(v) + ')' + new_u
                return answer
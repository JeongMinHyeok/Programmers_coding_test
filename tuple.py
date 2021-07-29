def solution(s):
    answer = []
    s = s.replace('{', ' ')
    s = s.replace('}', ' ')
    s = s.split(' ')
    sentence = s
    for idx, i in enumerate(sentence):
        if i == '' or i == ',':
            del s[idx]
    del s[0]
    del s[-1]
    tuple_list = []
    for j in s:
        tuple_list.append(list((j.split(','))))
    tuple_list = sorted(tuple_list, key=len)
    answer.append(int(tuple_list[0][0]))
    
    for t in range(len(tuple_list)-1):
        a = list(set(tuple_list[t+1]) - set(tuple_list[t]))
        answer.append(int(a[0]))
    return answer
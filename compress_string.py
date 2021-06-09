# 프로그래머스 코딩테스트 - 문자열 압축(Lv2)

def solution(s):
    
    length = len(s)
    s_zip = ''
    zip_list =[]

    if length == 1:
        return 1
    
    for i in range(1, length):
        sentence = s[:i]
        count = 1
        for j in range(i, length, i):
            if s[j:j+i] == sentence:
                count += 1
            else :
                if count == 1:
                    s_zip += sentence
                    sentence = s[j:j+i]
                else:
                    s_zip += str(count) + sentence
                    sentence = s[j:j+i]
                    count = 1
                
        if count == 1:
            s_zip += str(count) + sentence
            sentence = s[j:j+i]
            
        zip_list.append(len(s_zip))
        s_zip = ''
        
    return min(zip_list)
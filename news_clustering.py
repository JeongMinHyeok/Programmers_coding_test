import re
import collections as cols

def solution(str1, str2):
    
    str1_sec = []
    str2_sec = []
    for i in range(len(str1)-1):
        if (str1[i].isalpha()) & (str1[i+1].isalpha()):
            str1_sec.append(str(str1[i]+str1[i+1]).upper())
        
    for i in range(len(str2)-1):
        if (str2[i].isalpha()) & (str2[i+1].isalpha()):
            str2_sec.append(str(str2[i]+str2[i+1]).upper())
                
        
    str1_sec = cols.Counter(str1_sec)
    str2_sec = cols.Counter(str2_sec)
    
    union = sum((str1_sec | str2_sec).values())
    intersec = sum((str1_sec & str2_sec).values())
    
    if union == 0:
        answer = 65536
    else:
        answer = int(65536 * (intersec / union))
    
    return answer
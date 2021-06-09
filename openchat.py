# 프로그래머스 코딩테스트 연습 - 오픈채팅방(Lv2)

def solution(record):
    answer = []
    record_dict = {}
    for i, rec in enumerate(record):
        rec = rec.split(" ")
        if rec[1] not in record_dict.keys():
            record_dict[rec[1]] = [rec[2],(i,'님이 들어왔습니다.')]
        else:
            if rec[0] == 'Enter':
                value = record_dict[rec[1]]
                value.append((i,'님이 들어왔습니다.'))
                value[0] = rec[2]
                record_dict[rec[1]] = value
            if rec[0] == 'Leave':
                value = record_dict[rec[1]]
                value.append((i,'님이 나갔습니다.'))
                record_dict[rec[1]] = value
            if rec[0] == 'Change':
                value = record_dict[rec[1]]
                value[0] = rec[2]
                record_dict[rec[1]] = value
                
    print_list = []
    for v in record_dict.values():
        for j in range(len(v)):
            if j == 0:
                continue
            else:
                print_list.append((v[j],v[0]))
                
    print_list = sorted(print_list)
    for p in print_list:
        answer.append(str(p[1]+ p[0][1]))
    
    return answer

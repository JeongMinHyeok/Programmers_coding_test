# 프로그래머스 코딩테스트 연습 - 메뉴리뉴얼(Lv2)

def solution(orders, course):
    import itertools
    answer = []
    order_dict = {}
    
    for i in range(len(orders)):
        order_list = list(orders[i])
        for num in course:
            course_list = list(itertools.combinations(order_list, num))
            for j in course_list:
                j = sorted(j)
                j = ''.join(j)
                if j in order_dict.keys():
                    order_dict[j] += 1
                else:
                    order_dict[j] = 1
                    
    for num in course:
        compare_dict = {}
        for o in order_dict:
            if len(o) == num:
                compare_dict[o] = order_dict[o]
        if compare_dict == {}:
            max_order = 0
        elif max(compare_dict.values()) > 1:
            for c in compare_dict:
                if compare_dict[c] == max(compare_dict.values()):
                    answer.append(c)
    answer.sort()
    return answer
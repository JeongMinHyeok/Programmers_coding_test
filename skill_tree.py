def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        skill_list = list(skill)
        print(skill_list)
        count = 0
        for j in tree:
            if j in skill and j != skill_list.pop(0):
                    break
            count += 1
            if count == len(tree):
                answer += 1
    
    return answer
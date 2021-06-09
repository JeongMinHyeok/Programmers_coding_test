# 프로그래머스 코딩테스트 - 삼각달팽이(Lv2)

def solution(n):
    row = n-1
    column = 0
    count = n
    step = n
    direction = []
    triangle_snail = []
    answer = []

    for i in range(1, n+1):
        triangle_snail.append([i]*i)

    for i in range(n):
        direction.extend([0,1,2])
        if len(direction) == n-1 or len(direction) > n-1:
            direction = direction[:n]
            break

    for direct in direction:
        step -= 1
        for steps in range(0,step):
            if direct == 0: # 오른쪽
                column += 1
                count += 1
                triangle_snail[row][column] = count
            elif direct == 1: # 위쪽
                column -= 1
                row -= 1
                count += 1
                triangle_snail[row][column] = count
            else: # 아래쪽
                row += 1
                count += 1
                triangle_snail[row][column] = count

    for s in range(0, n):
        answer.extend(triangle_snail[s])
        
    return answer
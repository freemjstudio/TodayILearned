def solution(sides):
    answer = set()
    
    # 가장 긴변인 경우 
    m = max(sides)
    n = min(sides)
    # m < x + n 
    for i in range(m-n+1, m):
        answer.add(i)
    
    # 나머지 한변이 가장 긴 변인 경우 
    # x < m + n 
    for j in range(m, m+n):
        answer.add(j)
    return len(answer)
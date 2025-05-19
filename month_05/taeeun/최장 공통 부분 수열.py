# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBOHEx66kIDFAWr

T = int(input())

for tc in range(1, T+1):
    ans = 0
    word1, word2 = input().split()
    len1, len2 = len(word1), len(word2)
    
    matrix = [[0]*(len2+1) for _ in range(len1 +1)]
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if word1[i-1] != word2[j-1]:
                matrix[i][j] = max(matrix[i-1][j] , matrix[i][j-1])
            else:
                matrix[i][j] = matrix[i-1][j-1] + 1
            
            ans = max(ans, matrix[i][j])
    
    print(f'#{tc} {ans}')

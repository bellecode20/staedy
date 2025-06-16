# [PGR] 블록 이동하기 https://school.programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def solution(board):
    n = len(board)
    # 보드판 크게 만들기. -1로 감싸기.
    new_board = [[-1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    def is_vertical(a_row, a_col, b_row, b_col):
        return abs(a_row - b_row) == 1 and a_col == b_col
    
    def can_down(a_row, a_col, b_row, b_col):
        if new_board[a_row+1][a_col] == 0 and new_board[b_row+1][b_col] == 0:
            return True
        return False
    
    def can_right(a_row, a_col, b_row, b_col):
        if new_board[a_row][a_col+1] == 0 and new_board[b_row][b_col+1] == 0:
            return True
        return False
    
    def can_rotate(a_row, a_col, b_row, b_col):
        if is_vertical(a_row, a_col, b_row, b_col):
            return new_board[a_row][a_col+1] == 0 and new_board[b_row][b_col+1] == 0
        else:
            return new_board[a_row+1][a_col] == 0 and new_board[b_row+1][b_col] == 0
    
    queue = deque()
    visited = set()
    start = tuple(sorted(((1, 1), (1, 2))))
    queue.append((*start[0], *start[1], 0))
    visited.add(start)
    
    while queue:
        a_row, a_col, b_row, b_col, time = queue.popleft()
        if (n, n) in ((a_row, a_col), (b_row, b_col)):
            return time
        
        # 아래로 이동
        if can_down(a_row, a_col, b_row, b_col):
            new_pos = tuple(sorted(((a_row+1, a_col), (b_row+1, b_col))))
            if new_pos not in visited:
                queue.append((*new_pos[0], *new_pos[1], time + 1))
                visited.add(new_pos)
        
        # 오른쪽으로 이동
        if can_right(a_row, a_col, b_row, b_col):
            new_pos = tuple(sorted(((a_row, a_col+1), (b_row, b_col+1))))
            if new_pos not in visited:
                queue.append((*new_pos[0], *new_pos[1], time + 1))
                visited.add(new_pos)
        
        # 회전
        if can_rotate(a_row, a_col, b_row, b_col):
            if is_vertical(a_row, a_col, b_row, b_col):
                # 세로 -> 가로로 회전
                new_pos = tuple(sorted(((b_row, b_col), (b_row, b_col+1))))
                if new_pos not in visited:
                    queue.append((*new_pos[0], *new_pos[1], time + 1))
                    visited.add(new_pos)
            else:
                # 가로 -> 세로로 회전
                new_pos = tuple(sorted(((b_row, b_col), (b_row+1, b_col))))
                if new_pos not in visited:
                    queue.append((*new_pos[0], *new_pos[1], time + 1))
                    visited.add(new_pos)
    
    return 0

def read_matrix(size):    
    matrix = []
    for _ in range(size):
        row = [el for el in input()]
        matrix.append(row)
    return matrix

def check_in_range(row, col, size):
    return (0 <= row < size) and (0 <= col < size)


moves = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, 2), (2, -1), (2, 1), (1, -2)]

size = int(input())
matrix = read_matrix(size)

total_kills = 0
while True:
    most_kills = 0
    knight_r, knight_c = 0, 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "K" :
                dead_knights = 0
                for move in moves:
                    row = move[0] + r
                    col = move[1] + c
                    if check_in_range(row, col, size):
                        if matrix[row][col] == "K":                                                        
                            dead_knights += 1
                            if dead_knights > most_kills:
                                most_kills = dead_knights
                                knight_r, knight_c = r, c
    
    if most_kills == 0:         
        break
    total_kills += 1
    matrix[knight_r][knight_c] = "0"

print(total_kills)


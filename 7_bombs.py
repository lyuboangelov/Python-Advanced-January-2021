def read_matrix(r):    
    matrix = []
    for _ in range(r):
        row = [int(el) for el in input().split()]
        matrix.append(row)
    return matrix

def input_bombs():
    bombs = []
    bombs_input = input().split()
    for el in bombs_input:
        r, c = map(int, el.split(",")) 
        bombs.append((r, c)) 
    return bombs      

def check_in_range(row, col, size):
    return (0 <= row < size) and (0 <= col < size)


directions = [  (-1, 0), 
                (+1, 0), 
                (0, -1), 
                (0, +1), 
                (-1, -1),
                (-1, +1),
                (+1, -1),
                (+1, +1),
]

size = int(input())
matrix = read_matrix(size)
all_bombs = input_bombs()

dead_bombs = 0
total_sum = 0
alive_cells = 0

for bomb in all_bombs:
    if matrix[bomb[0]][bomb[1]] >= 0:
        bomb_power = matrix[bomb[0]][bomb[1]]
        matrix[bomb[0]][bomb[1]] = 0    
        for direction in directions:
            row = bomb[0] + direction[0]
            col = bomb[1] + direction[1]
            if check_in_range(row, col, size):
                matrix[row][col] -= bomb_power

for r in range(size):
    for c in range(size):
        if matrix[r][c] <= 0:
            dead_bombs += 1
        else:
            total_sum += matrix[r][c]
            alive_cells += 1
            




print("Alive cells:", alive_cells)
print("Sum:", total_sum)
for i in matrix:
    print(' '.join(map(str, i)))
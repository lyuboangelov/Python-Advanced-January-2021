def read_matrix(r):    
    matrix = []
    for _ in range(r):
        row = [el for el in list(input())]
        matrix.append(row)
    return matrix

def find_player(r, c, matrix):
    for row in range(r):
        for col in range(c):
            if matrix[row][col] == 'P':
                return row, col

def find_bunny(r, c, matrix):
    pos = []
    for row in range(r):
        for col in range(c):
            if matrix[row][col] == 'B':
                p = (row, col)
                pos.append(p)
    return pos

def check_out_of_range(row, col, r, c):
    return (0 <= row < r) and (0 <= col < c)

def bunny_spread(bun_cor, moves, matrix, r, c):
    for cor in bun_cor:
        row, col = cor[0], cor[1]
        up = row + moves[0][0]
        down = row + moves[1][0]
        left = col + moves[2][1]
        right = col + moves[3][1]
        matrix[row][col] = "B"
        if check_out_of_range(up, col, r, c):
            matrix[up][col] = "B"
        if check_out_of_range(down, col, r, c):
            matrix[down][col] = "B"
        if check_out_of_range(row, left, r, c):
            matrix[row][left] = "B"
        if check_out_of_range(row, right, r, c):
            matrix[row][right] = "B"
    return matrix

def check_for_bunny_hit(player_position, bun_pos):
    return player_position in bun_pos

def player_move(direction, movement, p_pos, matrix):    
    if direction == "U":    
        r_n = p_pos[0] + int(movement[0][0])
        c_n = p_pos[1] + int(movement[0][1])
    elif direction == "D":
        r_n = p_pos[0] + int(movement[1][0])
        c_n = p_pos[1] + int(movement[1][1])
    elif direction == "L":
        r_n = p_pos[0] + int(movement[2][0])
        c_n = p_pos[1] + int(movement[2][1])
    elif direction == "R":
        r_n = p_pos[0] + int(movement[3][0])
        c_n = p_pos[1] + int(movement[3][1])

    if check_out_of_range(r_n, c_n, len(matrix), len(matrix[0])) == False:
        matrix[p_pos[0]][p_pos[1]] = "."
        return matrix
    else:    
        matrix[p_pos[0]][p_pos[1]] = "."
        matrix[r_n][c_n] = "P"
        return matrix

def player_new_pos(direction, movement, p_pos, matrix):    
    if direction == "U":    
        r_n = p_pos[0] + int(movement[0][0])
        c_n = p_pos[1] + int(movement[0][1])
    elif direction == "D":
        r_n = p_pos[0] + int(movement[1][0])
        c_n = p_pos[1] + int(movement[1][1])
    elif direction == "L":
        r_n = p_pos[0] + int(movement[2][0])
        c_n = p_pos[1] + int(movement[2][1])
    elif direction == "R":
        r_n = p_pos[0] + int(movement[3][0])
        c_n = p_pos[1] + int(movement[3][1])
    return r_n, c_n

MOVEMENT = [(-1, 0), (1, 0), (0, -1), (0, 1),]
ROW_ST, COL_ST = map(int, input().split())
MATRIX = read_matrix(ROW_ST)
MOVES = [el for el in list(input())]
IS_DEAD = False
PLAYER_POS = find_player(ROW_ST, COL_ST, MATRIX)
bunny_pos = find_bunny(ROW_ST, COL_ST, MATRIX)

for move in MOVES:
    
    if move == "U":
        PLAYER_POS = find_player(ROW_ST, COL_ST, MATRIX)
        PLAYER_NEW_POS = player_new_pos(move, MOVEMENT, PLAYER_POS, MATRIX)
        if check_out_of_range(PLAYER_NEW_POS[0], PLAYER_NEW_POS[1], ROW_ST, COL_ST) == False:            
            IS_DEAD = False
            break        
        MATRIX = player_move(move, MOVEMENT, PLAYER_POS, MATRIX)        
        if check_for_bunny_hit(PLAYER_POS, bunny_pos):
            IS_DEAD = True
            break
    elif move == "D":
        PLAYER_POS = find_player(ROW_ST, COL_ST, MATRIX)
        PLAYER_NEW_POS = player_new_pos(move, MOVEMENT, PLAYER_POS, MATRIX)
        if check_out_of_range(PLAYER_NEW_POS[0], PLAYER_NEW_POS[1], ROW_ST, COL_ST) == False:
            IS_DEAD = False
            break        
        MATRIX = player_move(move, MOVEMENT, PLAYER_POS, MATRIX)        
        if check_for_bunny_hit(PLAYER_POS, bunny_pos):
            IS_DEAD = True
            break
    elif move == "L":
        PLAYER_POS = find_player(ROW_ST, COL_ST, MATRIX)
        PLAYER_NEW_POS = player_new_pos(move, MOVEMENT, PLAYER_POS, MATRIX)
        if check_out_of_range(PLAYER_NEW_POS[0], PLAYER_NEW_POS[1], ROW_ST, COL_ST) == False:
            IS_DEAD = False
            break        
        MATRIX = player_move(move, MOVEMENT, PLAYER_POS, MATRIX)        
        if check_for_bunny_hit(PLAYER_POS, bunny_pos):
            IS_DEAD = True
            break
    elif move == "R":
        PLAYER_POS = find_player(ROW_ST, COL_ST, MATRIX)
        PLAYER_NEW_POS = player_new_pos(move, MOVEMENT, PLAYER_POS, MATRIX)
        if check_out_of_range(PLAYER_NEW_POS[0], PLAYER_NEW_POS[1], ROW_ST, COL_ST) == False:
            IS_DEAD = False
            break        
        MATRIX = player_move(move, MOVEMENT, PLAYER_POS, MATRIX)        
        if check_for_bunny_hit(PLAYER_POS, bunny_pos):
            IS_DEAD = True
            break

    PLAYER_POS = find_player(ROW_ST, COL_ST, MATRIX)
    MATRIX = bunny_spread(bunny_pos, MOVEMENT, MATRIX, ROW_ST, COL_ST)
    bunny_pos = find_bunny(ROW_ST, COL_ST, MATRIX)
    if check_for_bunny_hit(PLAYER_POS, bunny_pos):
        IS_DEAD = True    
        break
    
if IS_DEAD:
        
    for el in MATRIX:
        print("".join(el))
    print(f"dead: {PLAYER_POS[0]} {(PLAYER_POS[1])}")
else:
    MATRIX[PLAYER_POS[0]][PLAYER_POS[1]] = "."
    MATRIX = bunny_spread(bunny_pos, MOVEMENT, MATRIX, ROW_ST, COL_ST)
    for el in MATRIX:
        print("".join(el))
    print(f"won: {PLAYER_POS[0]} {(PLAYER_POS[1])}")
    
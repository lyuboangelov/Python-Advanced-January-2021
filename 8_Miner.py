def read_matrix(r):    
    matrix = []
    for _ in range(r):
        row = [el for el in list(input().split())]
        matrix.append(row)
    return matrix

def check_out_of_range(row, col, r, c):
    return (0 <= row < r) and (0 <= col < c)

def player_move(direction, movement, p_pos, matrix):    
    if direction == "up":    
        r_n = p_pos[0] + int(movement[0][0])
        c_n = p_pos[1] + int(movement[0][1])
    elif direction == "down":
        r_n = p_pos[0] + int(movement[1][0])
        c_n = p_pos[1] + int(movement[1][1])
    elif direction == "left":
        r_n = p_pos[0] + int(movement[2][0])
        c_n = p_pos[1] + int(movement[2][1])
    elif direction == "right":
        r_n = p_pos[0] + int(movement[3][0])
        c_n = p_pos[1] + int(movement[3][1])

    if check_out_of_range(r_n, c_n, len(matrix), len(matrix[0])) == False:
        new_pos = matrix[p_pos[0]][p_pos[1]] = "s"
        return matrix, new_pos
    else:    
        matrix[p_pos[0]][p_pos[1]] = "*"
        matrix[r_n][c_n] = "s"
        new_pos = (r_n, c_n)
        return matrix, new_pos    

def check_coal_end(player_position, coal_pos, end_pos):
    return player_position in coal_pos, player_position in end_pos

def find_player(r, c, matrix):
    for row in range(r):
        for col in range(c):
            if matrix[row][col] == 's':
                return row, col

def find_coal_or_end(r, matrix):
    coal = []
    end = []
    for row in range(r):
        for col in range(r):
            if matrix[row][col] == 'c':
                cord = (row, col)
                coal.append(cord)
            elif matrix[row][col] == 'e':
                cord = (row, col)
                end.append(cord)
    return coal, end


MOVEMENT = [(-1, 0), (1, 0), (0, -1), (0, 1),]
size = int(input())
moves = [el for el in input().split(" ")]
matrix = read_matrix(size)
collected_coals = []
coal_end = find_coal_or_end(size, matrix)
total_coal_end = find_coal_or_end(size, matrix)
not_collected = True

for move in moves:
    player_pos = find_player(size, size, matrix)
    if move == "up":
        matrix, new_pos = player_move(move, MOVEMENT, player_pos, matrix)
        coal, end = check_coal_end(new_pos, coal_end[0], coal_end[1])
    elif move == "down":
        matrix, new_pos = player_move(move, MOVEMENT, player_pos, matrix)
        coal, end = check_coal_end(new_pos, coal_end[0], coal_end[1])
    elif move == "left":
        matrix, new_pos = player_move(move, MOVEMENT, player_pos, matrix)
        coal, end = check_coal_end(new_pos, coal_end[0], coal_end[1])
    elif move == "right":
        matrix, new_pos = player_move(move, MOVEMENT, player_pos, matrix)
        coal, end = check_coal_end(new_pos, coal_end[0], coal_end[1])
    
    if (check_coal_end(new_pos, coal_end[0], coal_end[1])[0]):
        
        if new_pos in collected_coals:
            pass
        else:
            collected_coals.append(new_pos)
        
        if len(coal_end[0]) == len(collected_coals):
            print("You collected all coals!", new_pos)
            not_collected = False
            break
    elif (check_coal_end(new_pos, coal_end[0], coal_end[1])[1]):
        print("Game over!", new_pos)
        not_collected = False
        break
    else:
        not_collected = True


if not_collected:
    print(f"{(len(coal_end[0]) - len(collected_coals))} coals left. {new_pos}")
    
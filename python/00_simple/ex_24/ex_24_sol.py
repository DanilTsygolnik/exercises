"""

"""
def prepare_matrix(matrix_src):
    templ = []
    for i in matrix_src: # go through each row in matrix
        curr_row = []
        for j in i: # put each letter from the matrix_src[i] string into curr_row
            curr_row += [j]
        templ.append(curr_row)
    return templ

def get_rings(N, M):
    
    def iter_rings(N, M, rings_list):
        rings_list.append([N, M])
        if N == 2 or M == 2:
            return rings_list
        else:
            return iter_rings(N-2, M-2, rings_list)

    return iter_rings(N, M, [])

def get_left_col_as_row(N,M,matrix,delta):
    row = []
    for i in range(1+delta, N-delta):
        row += [matrix[i][delta]]
    return row

def get_right_col_as_row(N,M,matrix,delta):
    row = []
    for i in range(delta, N-1-delta):
        row += [matrix[i][M-1-delta]]
    return row

def get_rotated_ring(matrix, new_columns, delta):
    col_num = delta
    for i in new_columns:
        row_num = delta # нужно добавить переход от записи в столбец к записи строки, причем в зав-ти от левый/правый new_col
        for j in i:
            matrix[row_num][col_num] = j
            row_num += 1
        col_num += 1
    # no return, function changes initial matrix

def iter_rotate(matrix, N, M, delta):
    # N - number of rows in matrix
    # M - number of columns in matrix

    # horizontal segments of the ring
    top_row = []
    row_num = delta
    for j in range(delta, M-1-delta):
        top_row += [matrix[row_num][j]]

    bottom_row = []
    row_num = N-1-delta
    for j in range(1+delta, M-delta):
        bottom_row += [matrix[row_num][j]]


    # here is a chance to make optimal sol
    # combine vertical and horizontal segments into half-ring pieces
    new_left_col = get_left_col_as_row(N,M,matrix,delta) + bottom_row
    new_right_col = top_row + get_right_col_as_row(N,M,matrix,delta)

    new_columns = [new_left_col, new_right_col]
    print(new_columns)

    get_rotated_ring(matrix, new_columns, delta)
    # no return, function changes initial matrix


def turn_iter(matrix_src, num_rows, num_cols):
    # convert 'strings' into ['s', 't', 'r', 'i', 'n', 'g', 's']
    matrix = prepare_matrix(matrix_src)
    # get dimensions of the rings to be rotated at each step
    rings = get_rings(num_rows, num_cols)
    for i in rings:
        curr_num_rows = i[0]
        curr_num_cols = i[1]
        delta = (curr_num_rows - num_rows) // 2
        #
        iter_rotate(matrix, curr_num_rows, curr_num_cols, delta)
    #
    return src_format(matrix)


def MatrixTurn(matrix, num_rows, num_cols, turns_cnt):
    
    # ---------------- MatrixTurn -------------------------------------------
    if turns_cnt == 0:
        return matrix
    else:
        return MatrixTurn(turn_iter(matrix), num_rows, num_cols, turns_cnt-1)

# disabled linter notifications on missing docstrings & snake_case naming style
# pylint: disable=C0114,C0116
# pylint: disable=C0103


def prepare_matrix(matrix_src):
    templ = []
    for i in matrix_src: # go through each row in matrix
        curr_row = []
        for j in i: # put each letter from the matrix_src[i] string into curr_row
            curr_row += [j]
        templ.append(curr_row)
    return templ


def get_rings(N, M):
    """
    Получить список пар [N,M] для дальнейшего расчета delta (используется при вращении матрицы).
    Например, при в матрице 5х4 (N=5, M=4) при delta=1 поворачивается внешний слой массива 4х3.
    """
    def iter_rings(N, M, rings_list):
        rings_list.append([N, M])
        if N == 2 or M == 2:
            return rings_list
        return iter_rings(N-2, M-2, rings_list)

    return iter_rings(N, M, [])


def get_left_col_as_row(N,matrix,delta):
    row = []
    for i in range(1+delta, N-delta):
        row += [matrix[i][delta]]
    return row


def get_right_col_as_row(N,M,matrix,delta):
    row = []
    for i in range(delta, N-1-delta):
        row += [matrix[i][M-1-delta]]
    return row


def iter_rotate(matrix, N, M, delta):
    """
    1 поворот отдельного кольца в массиве, заданном параметром delta.
    """
    # N - rows in matrix
    # M - columns in matrix

    # horizontal segments of the "ring"
    top_row_templ = []
    row_num = delta
    for j in range(delta, M-1-delta):
        top_row_templ += [matrix[row_num][j]]

    bottom_row_templ = []
    row_num = N-1-delta
    for j in range(1+delta, M-delta):
        bottom_row_templ += [matrix[row_num][j]]

    # vertical segments of the "ring"
    left_col = get_left_col_as_row(N,matrix,delta)
    right_col = get_right_col_as_row(N,M,matrix,delta)

    # rewrite left column and top row in matrix (1/2 of the "ring")
    matrix_row_cnt = delta
    col_ind_cnt = 0
    for i in left_col:
        if col_ind_cnt == 0:
            matrix[matrix_row_cnt][delta:M-delta] = [i] + top_row_templ
        else:
            matrix[matrix_row_cnt][delta] = i
        matrix_row_cnt  += 1
        col_ind_cnt += 1
    # rewrite right column and bottop row in matrix (2/2 of the "ring")
    matrix_row_cnt = 1+delta
    col_ind_cnt = 0
    for i in right_col:
        if col_ind_cnt == len(right_col)-1:
            matrix[matrix_row_cnt][delta:M-delta] = bottom_row_templ + [i]
        else:
            matrix[matrix_row_cnt][M-1-delta] = i
        matrix_row_cnt  += 1
        col_ind_cnt += 1
    # no return, function changes initial matrix


def src_format(matrix):
    """ Prepare matrix for output """
    templ = []
    for i in matrix:
        curr_str = ''
        for j in i:
            curr_str += j
        templ.append(curr_str)
    return templ


def turn_iter(matrix_src, N, M):
    """ 1 step matrix rotation clockwise """
    # convert 'strings' into ['s', 't', 'r', 'i', 'n', 'g', 's']
    matrix = prepare_matrix(matrix_src)
    # get dimensions of the rings to be rotated at each step
    rings = get_rings(N, M)
    for i in rings:
        curr_num_rows = i[0]
        delta = (N - curr_num_rows) // 2
        #
        iter_rotate(matrix, N, M, delta)
    #
    return src_format(matrix)


def MatrixTurn(matrix, num_rows, num_cols, turns_cnt):
    """ Rotate matrix clockwise several (turns_cnt) times """
    if turns_cnt == 0:
        return matrix
    return MatrixTurn(turn_iter(matrix, num_rows, num_cols), num_rows, num_cols, turns_cnt-1)

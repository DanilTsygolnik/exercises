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


def turn_iter(matrix_src, num_rows, num_cols):
    # convert 'strings' into ['s', 't', 'r', 'i', 'n', 'g', 's']
    matrix = prepare_matrix(matrix_src)
    #
    rings = get_rings(num_rows, num_cols)
    for i in rings:
        curr_num_rows = i[0]
        curr_num_cols = i[1]
        delta = (curr_num_rows-num_rows) // 2
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

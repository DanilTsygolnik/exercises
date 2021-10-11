def get_data(source):
    output = []
    for i in source:
        curr_str = []
        for j in i:
            if j == '.':
                curr_str.append([0, '.'])
            else:
                curr_str.append([1, '+'])
        output.append(curr_str)
    return output

def aging(data):
    output = data
    for i in output:
        for j in i:
            j[0] += 1
            j[1] = '+'
    return output

def decay(data, H, W):

    def add_in_list(item, target):
        if item not in target:
            target.append(item)

    def modify_col(coord, h, w):
        if h == 0:
            add_in_list([h+1, w], coord)
        elif h == H-1:
            add_in_list([h-1, w], coord)
        else:
            add_in_list([h+1, w], coord)
            add_in_list([h-1, w], coord)
    
    def modify_row(coord, h, w):
        if w == 0:
            add_in_list([h, w+1], coord)
        elif w == W-1:
            add_in_list([h, w-1], coord)
        else:
            add_in_list([h, w+1], coord)
            add_in_list([h, w-1], coord)

    coord = []

    output = data
    curr_H = 0
    for i in output:
        curr_W = 0
        for j in i:
            if j[0] >= 3:
                modify_col(coord, curr_H, curr_W)
                modify_row(coord, curr_H, curr_W)
                add_in_list([curr_H, curr_W], coord)
            curr_W += 1
        curr_H += 1
    for i in coord:
        h = i[0]
        w = i[1]
        output[h][w][0] = 0
        output[h][w][1] = '.'
    return output

def get_output(templ):
    output = []
    for i in templ:
        curr_str = ''
        for j in i:
            curr_str += j[1]
        output.append(curr_str)
    return output

def TreeOfLife(H, W, N, data_src):
    
    def year_iter(data, cnt, N):
        if cnt < N:
            curr_tree = aging(data)
            if cnt % 2 != 0:
                curr_tree = decay(curr_tree, H, W)
            return year_iter(curr_tree, cnt+1, N)
        else:
            return data

    curr_tree = get_data(data_src)
    templ = year_iter(curr_tree, 0, N)
    return get_output(templ)

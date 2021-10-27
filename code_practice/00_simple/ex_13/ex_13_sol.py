def UFO(N, data, octal=True):
    integers = []
    index_cnt = 0
    while index_cnt < N:
        if octal:
            integers.append(int(str(data[index_cnt]), 8))
        else:
            integers.append(int(str(data[index_cnt]), 16))
        index_cnt += 1
    return integers

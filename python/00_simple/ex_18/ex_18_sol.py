def is_sort(data):
    cnt = 1
    while cnt < len(data):
        if data[cnt-1] <= data[cnt]:
            result = True
        else:
            result = False
            break
        cnt += 1
    return result

# func(list, index) -> list_rotated
def get_rotated(data, index):
    data_mod = data.copy()
    tmp_head = data[index]
    data_mod[index] = data[index+1] # mid -> head
    data_mod[index+1] = data[index+2] # tail -> mid
    data_mod[index+2] = tmp_head # head -> tail
    return data_mod

def MisterRobot(N, data): # N >= 4, len(data) = N

    val_list = []
    
    def brute_force(data, val_list):
        if is_sort(data):
            return True
        elif data in val_list:
            return False
        else:
            val_list.append(data)
            result = False
            for i in range(N-2):
                if brute_force(get_rotated(data, i), val_list): # if True
                    result = True
                    break
            return result

    return brute_force(data, val_list)

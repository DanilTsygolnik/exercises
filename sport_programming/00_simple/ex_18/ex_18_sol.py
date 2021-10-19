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

def get_rotated_src(data, index):
    tmp_head = data[index]
    data[index] = data[index+1] # mid -> head
    data[index+1] = data[index+2] # tail -> mid
    data[index+2] = tmp_head # head -> tail
    

def MisterRobot(N, data): # N >= 4, len(data) = N
    if is_sort(data):
        return True
    else:
        cnt = N-3
        while cnt >= 0:
            curr_max = max(data[cnt:cnt+3])
            while True:
                if data[cnt+2] == curr_max:
                    break
                get_rotated_src(data, cnt)
            if cnt == 0:
                curr_min = min(data[cnt:cnt+3])
                if  data[0] == curr_min:
                    return True
                else:
                    return False
            cnt -= 1

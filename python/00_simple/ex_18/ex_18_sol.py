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
            print('outlook befor rot --', data)
            print('ind =', cnt, 'curr_list --', data[cnt:cnt+3])
            curr_max = max(data[cnt:cnt+3])
            #while curr_max != curr_list[2]:
            while True:
                if data[cnt+2] == curr_max:
                    break
                get_rotated_src(data, cnt)
                #curr_list = get_rotated(curr_list, 0) # !! нужно обновлять исходный список data, когда curr_list[2] == curr_max
            # test print
            print('curr_list rotated --', data[cnt:cnt+3])
            print('outlook --', data)
            if cnt == 0:
                curr_min = min(data[cnt:cnt+3])
                if  data[0] == curr_min:
                    return True
                else:
                    return False
            cnt -= 1

#print(MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]))
#print(MisterRobot(4, [3, 2, 4, 1]))
print(MisterRobot(6, [1, 3, 4, 6, 2, 7]))

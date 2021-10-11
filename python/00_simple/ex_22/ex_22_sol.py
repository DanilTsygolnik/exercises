def letters_count(string):
    letters = {}
    for i in string:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    count_list = []
    for i in letters.values():
        count_list.append(i)
    return count_list

def SherlockValidString(inp_string):
    output = True
    val = letters_count(inp_string)
    N = len(val)
    del_not_used = True
    cnt = 1
    while cnt < N:
        if val[cnt] != val[cnt-1]:
            if del_not_used:
                if abs(val[cnt] - val[cnt-1]) > 1:
                    output = False
                    break
                else:
                    if val[cnt] == 1:
                        val = val[:cnt] + val[cnt+1:]
                        N -= 1
                        cnt -= 1
                    else:
                        val[cnt] -= 1
                    del_not_used = False
            else:
                output = False
                break
        cnt += 1
    return output

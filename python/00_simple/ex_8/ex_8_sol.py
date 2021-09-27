def SumOfThe(N, data):
    curr_sum = sum(data[1:])
    cnt = 0
    while cnt < N:
        if data[cnt] == curr_sum:
            break
        if cnt != N-1:
            curr_sum += data[cnt] - data[cnt+1]
        cnt += 1
    return curr_sum

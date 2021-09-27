import random

for N in [2, 3, 5, 6]:
    data = []
    sum_curr = 0
    cnt = 0
    while cnt < N:
        if cnt == N - 1:
            data += [sum_curr]
        else:
            curr = random.randint(-100, 100)
            sum_curr += curr
            data += [curr]
        cnt += 1
    print(data)
    check_value = data[N-1]
    random.shuffle(data)
    print(data)

    def SumOfThe(N, data):
        curr_sum = sum(data[1:])
        #    curr_sum += 1
        #answer = None
        #cnt = -1
        #for i in data:
        #    cnt += 1
        #    if i == curr_sum:
        #        answer = i
        #        break
        #    if cnt != N-1:
        #        curr_sum += i - data[cnt+1]
        #return answer
        cnt = 0
        while cnt < N:
            if data[cnt] == curr_sum:
                break
            if cnt != N-1:
                curr_sum += data[cnt] - data[cnt+1]
                #else:
                #    answer = data[cnt]
            cnt += 1
        return curr_sum

    print("answer -", SumOfThe(N, data), "-- check -", check_value)


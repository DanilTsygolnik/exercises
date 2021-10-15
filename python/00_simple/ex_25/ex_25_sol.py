def transform(data):
    """
    Реализация алгоритма обработки массива данных в соответствии с заданием.
    """
    output = []
    for i in range(0, len(data)):
        if i == len(data)-1:
            output.append(data[i])
        else:
            for j in range(0, len(data)-i-1):
                k = i + j
                output.append(max(data[j:k+1]))
    return output

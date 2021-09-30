def big_num_small_num(first_str, second_str):
    if len(first_str) < len(second_str):
        big_n = second_str
        small_n = first_str
    elif len(first_str) > len(second_str):
        big_n = first_str 
        small_n = second_str
    else:
        if first_str < second_str:
            big_n = second_str
            small_n = first_str
        else:
            big_n = first_str 
            small_n = second_str
    return [big_n, small_n]

def add_zeros(big_int, small_int):
    if len(big_int) > len(small_int):
        zeros_cnt = len(big_int) - len(small_int)
        zeros_str = zeros_cnt * '0'
        result = zeros_str + small_int
        return result
    else:
        return small_int

def BigMinus(first_str, second_str):

    integers = big_num_small_num(first_str, second_str)
    big_int = integers[0]
    small_int = integers[1]
    small_int = add_zeros(big_int, small_int)
    subtract_results = []
    index_cnt = len(big_int) - 1
    imaginary_register = 0
    while index_cnt >= 0:
        i = int(big_int[index_cnt])
        j = int(small_int[index_cnt])
        result = imaginary_register + i - j
        #if i < j:
        if result < 0:
            result += 10
            imaginary_register = -1
        else:
            imaginary_register = 0
        subtract_results.append(str(result))  
        index_cnt -= 1
    output_str = ''
    index_cnt = len(subtract_results) - 1
    num_is_first = True
    while index_cnt >= 0:
        if subtract_results[index_cnt] == '0' and num_is_first:
            output_str += ''
        else:
            output_str += subtract_results[index_cnt]
            num_is_first = False
        index_cnt -= 1
    if num_is_first:
        if subtract_results != []:
            return '0'
        else:
            return ''
    else:
        return output_str

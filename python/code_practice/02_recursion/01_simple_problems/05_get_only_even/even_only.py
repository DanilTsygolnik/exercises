def get_only_even(src_list):
    
    def iter_func(even_numbers, curr_list):
        if curr_list == []:
            return even_numbers
        if curr_list[0] % 2 == 0:
            even_numbers.append(curr_list[0])
        return iter_func(even_numbers, curr_list[1:])

    return iter_func([], src_list)

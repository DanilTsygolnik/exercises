def is_palindrome(string):
    
    def iter_func(curr_list, left_part, right_part):
        if len(curr_list) < 2:
            return left_part == right_part
        left_part.append(curr_list[0])
        right_part.append(curr_list[-1])
        return iter_func(curr_list[1:-1], left_part, right_part)

    return iter_func(string, [], [])

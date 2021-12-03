def get_second_max(src_list):

    def iter_func(max_val, second_max_val, index_count, src_list, index_limit):
        if index_count == index_limit:
            return second_max_val
        
        curr_val = src_list[index_count]
        
        if curr_val > max_val:
            return iter_func(curr_val, max_val, index_count+1, src_list, index_limit)
        
        if curr_val < max_val and (second_max_val is None or curr_val > second_max_val):
            return iter_func(max_val, curr_val, index_count+1, src_list, index_limit)
        
        return iter_func(max_val, second_max_val, index_count+1, src_list, index_limit)

    if len(src_list) < 2:
        return None
    return iter_func(src_list[0], None, 1, src_list, len(src_list))

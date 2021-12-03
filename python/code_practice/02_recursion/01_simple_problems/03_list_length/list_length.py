def get_length(inp_list):
    
    def iter_func(curr_list, len_count):
        if curr_list == []:
            return len_count
        curr_list.pop(0)
        return iter_func(curr_list, len_count+1)

    return iter_func(inp_list, 0)

def read_from_even(src_list):
 
    def iter_func(output_list, even_index_count, index_limit):
        if even_index_count >= index_limit:
            return output_list
        output_list.append(even_index_count)
        return iter_func(output_list, even_index_count+2, index_limit)

    if src_list == []:
        return []
    return iter_func([], 0, len(src_list))

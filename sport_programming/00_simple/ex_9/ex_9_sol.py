def TheRabbitsFoot(string_input, encode=True):

    def round_custom(number, high=False):
        number_x10 = number * 10
        if high:
            round_result = int(number_x10 // 10 + 1)
        else:
            round_result = int(number_x10 // 10)
        return round_result

    def letters_only(message):
        words_list = message.split()
        output = ''
        for i in words_list:
            output += i
        return output

    def matrix_size_calc(message): 
        string_no_spaces = letters_only(message)
        letters_in_message = len(string_no_spaces)
        sizes = ['rows', 'columns']
        string_length = letters_in_message **(1/2)
        string_length_x10 = string_length*10
        if string_length == string_length_x10 // 10:
            sizes[0] = sizes[1] = int(string_length)
        else:
            sizes[0] = round_custom(string_length)
            sizes[1] = round_custom(string_length, True)
        if sizes[0]*sizes[1] < letters_in_message:
            sizes[0] += 1
        return sizes

    def get_matrix(message, encode):

        matrix = []

        if encode:
            string_no_spaces = letters_only(message)
            letters_in_message = len(string_no_spaces)
            sizes = matrix_size_calc(message)
            for j in range(sizes[0]):
                matrix.append([])
            letter_index_cnt = 0
            for j in matrix:
                row_index_cnt = 0
                while row_index_cnt < sizes[1] and letter_index_cnt < letters_in_message:
                    j.append(string_no_spaces[letter_index_cnt])
                    letter_index_cnt += 1
                    row_index_cnt += 1
                if letter_index_cnt >= letters_in_message:
                    while row_index_cnt < sizes[1]:
                        j.append('')
                        row_index_cnt += 1
        else:
            words_list = message.split()
            num_rows = len(words_list[0])
            row_cnt = 0
            while row_cnt < num_rows:
                matrix.append([])
                row_cnt += 1
            for word in words_list:
                row_cnt = 0 
                for j in word:
                    matrix[row_cnt] += j
                    row_cnt += 1
        return matrix

    def sypher(message, encode):
    
        matrix = get_matrix(message, encode)    
    
        message_syphered = ''

        sizes = matrix_size_calc(message)
        row_indexes = range(sizes[0])
        col_indexes = range(sizes[1])
        for i in col_indexes:
            for j in row_indexes:
                message_syphered += matrix[j][i]
            if i != sizes[1]-1:
                message_syphered += ' '
        return message_syphered

    def desypher(message_syphered, encode):
    
        matrix = get_matrix(message_syphered, encode)    
        
        message_desyphered = ''
        for j in matrix:
            for i in j:
                message_desyphered += i
        return message_desyphered

    # ----------------------------------------------
    if string_input == '':
        return ''
    else:
        if encode: # sypher mode
            return sypher(string_input, encode)
        else: # desypher mode
            return desypher(string_input, encode)

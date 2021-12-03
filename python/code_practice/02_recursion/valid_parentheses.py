def iter_func(valid_pairs_num, invalid_pairs_num, strict_invalid_pairs_num, num_curr_step, parens):
    if parens == []:
        # анализируем результаты (счетчики пар)
        # only valid pairs
        if invalid_pairs_num == 0 and strict_invalid_pairs_num == 0:
            return True
        if invalid_pairs_num != 0:
            # 3.1
            if strict_invalid_pairs_num == 0:
                if invalid_pairs_num <= valid_pairs_num:
                    return True
                return False
            # 3.3?
            if strict_invalid_pairs_num % 2 == 0 and \
               strict_invalid_pairs_num > invalid_pairs_num:
                return True
            return False
        # 3.2
        if strict_invalid_pairs_num % 2 == 0 and \
           strict_invalid_pairs_num > valid_pairs_num:
            return True
        return False

    curr_pair = "".join([parens[0], parens[-1]]) # подготовить текущую пару для проверки

    if num_curr_step == 1:
        if curr_pair != "()":
            return False
        if len(parens) == 2:
            return True
        # иначе переходим к сл. шагу итерации
        return iter_func(valid_pairs_num+1, # обновляем счетчика валидных пар \
                         invalid_pairs_num, strict_invalid_pairs_num, # невалидных пар пока нет \
                         num_curr_step+1, # обновим счетчик, чтобы далее не проверять это условие \
                         parens[1:-1]) # исключаем проверенную пару скобок из рассмотрения 

    # на остальных шагах считаем пары "()", ")(", "((", "))"
    if curr_pair == "()": # увеличиваем счетчик валидных
        return iter_func(valid_pairs_num+1, invalid_pairs_num, strict_invalid_pairs_num, num_curr_step+1, parens[1:-1])
    if curr_pair == ")(": # увеличиваем счетчик невалидных
        return iter_func(valid_pairs_num, invalid_pairs_num+1, strict_invalid_pairs_num, num_curr_step+1, parens[1:-1])
    # иначе увеличиваем счетчик строго невалидных
    return iter_func(valid_pairs_num, invalid_pairs_num, strict_invalid_pairs_num+1, num_curr_step+1, parens[1:-1])

def valid_parentheses(string):
    parentheses = []
    left_paren_num = 0
    right_paren_num = 0
    for c in string.strip(): # пройти по строке, собрать скобки
        if c in "()":
            parentheses.append(c)
            if c == "(":
                left_paren_num += 1
            else:
                right_paren_num = 0
    if left_paren_num == right_paren_num:
        return iter_func(0,0,0, 1, parentheses)
    return False

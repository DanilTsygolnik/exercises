def iter_func(num_curr_step, iter_steps_num, parentheses, valid_num, invalid_num):

    # записываем комбинацию рассматриваемой пары скобок в переменную curr_pair
    curr_pair = "".join([parentheses[0], parentheses[-1]])

    if num_curr_step == 1:
        if curr_pair != "()": # проверка внешней пары скобок:
            return False
        if iter_steps_num == 1: # скобок всего 2, и они валидные ==> вернуть окончательный ответ
            return True
        return iter_func(num_curr_step+1, # переход к сл. итерации \
                         iter_steps_num, \
                         parentheses[1:-1], # исключаем из рассмотрения проверенные скобки \
                         valid_num+1, # обновляем счетчик валидных пар \
                         invalid_num)

    # действия на втором и последующих шагах итерации
    if not curr_pair in ["()", ")("]: # если curr_pair не "()" и не ")(":
        return False # т.к. скобок четное кол-во, то "(" и ")" должно быть строго поровну
    if curr_pair == "()":
        valid_num += 1
    else:
        invalid_num += 1
    if num_curr_step != iter_steps_num: # если шаг_итерации не последний:
        return iter_func(num_curr_step+1, iter_steps_num, parentheses[1:-1], \
                         valid_num, # текущие значения счетчиков валидных ... \
                         invalid_num) # ... и невалидных пар

    # иначе, на последнем шаге проводим анализ соотношения числа валидных и невалидных пар
    if iter_steps_num % 2 == 0: # если при четном числе шагов итерации:
        if valid_num >= invalid_num:
            return True
        return False
    # иначе, при нечетном числе шагов
    if valid_num < invalid_num:
        return False
    return True

def valid_parentheses(string):

    parentheses = []
    parentheses_cnt = 0
    for c in string.strip(): # пройти по строке, собрать скобки
        if c in "()":
            parentheses.append(c)
            parentheses_cnt += 1
    if parentheses_cnt % 2 == 0:
        if parentheses_cnt == 0:
            return True
        iter_steps_num = parentheses_cnt // 2
        return iter_func(1, iter_steps_num, parentheses, 0, 0)
    return False

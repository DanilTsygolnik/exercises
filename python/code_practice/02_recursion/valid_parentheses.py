def valid_parentheses(string):

    # def recurr_fun(parentheses:list):
    #     if parentheses == []:
    #         return True
    #     if parentheses[0] == "(" and parentheses[-1] == ")":
    #         return recurr_fun(parentheses[1:-1])
    #     return False

    parentheses = []
    parentheses_cnt = 0
    for c in string.strip(): # пройти по строке, собрать скобки
        if c in "()":
            parentheses.append(c)
            parentheses_cnt += 1
    if parentheses_cnt != 0 and parentheses_cnt % 2 == 0:
        valid_marker = 1
        for p in parentheses:
            if p == ")":
                valid_marker *= -1
        if valid_marker == 1:
            return True
    return False

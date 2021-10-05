def LineAnalysis(string):
    if string[0] == '*' and string[len(string)-1] == '*':
        if '.' not in string:
            return True
        else:
            result = True
            pattern = '*'
            checklist = []
            for i in string[1:]:
                pattern += i
                if i == '*':
                    if pattern not in checklist:
                        checklist.append(pattern)
                        if len(checklist) > 1:
                            result = False
                            break
                    pattern = '*'
            return result
    else:
        return False

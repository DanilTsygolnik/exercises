curr_str = ''

def BastShoe(command):
    
    def cmd_check(command):
        cnt = 0
        cmd_ids = ['1', '2', '3', '4', '5']
        id_templ = ''
        for i in command:
            if cnt > 1:
                break
            id_templ += i
            cnt += 1
        id_test = id_templ.split()
        if id_test[0] not in cmd_ids:
            return None 
        else:
            return id_test[0]

    def str_is_number(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    # ----------------------------

    curr_id = cmd_check(command)
    if curr_id == None:
        return curr_str
    else:
        # смотрим по конкретному id
        if curr_id == '1':
            pass






        elif curr_id in ['2', '3']:
            if len(command.split()) == 2: # проверка на корректность команды с id=2;3
                # проверяем N
                N = command.split()[1]
                if str_is_number(N): # обращаемся к операции, в зав-ти от id
                    N = int(N)
                    if curr_id == '2' and N >= 0: # id=2
                        if N >= len(curr_str):
                            curr_str = ''
                        else:
                            curr_str = curr_str[:len(curr_str)-N]
                        # добавить влияние на Undo и Redo
                        return curr_str
                    if curr_id == '3' and N >= 0:
                        if N > len(curr_str)-1:
                            return ''
                        else:
                            return curr_str[N]
            else:
                return curr_str
                

        else: # id=4;5

            # сперва проверяем корректность команды. Для id=4;5 нужна только цифра в запросе, поэтому:
            if len(command.split()) == 1:
                # далее по id
                #4. Undo() -- отмена последней операции 1 или 2;
                #отмена должна уметь выполняться при необходимости неограниченное число раз;
                if curr_id == '4':
                    > записываем текущее состояние в лог для Redo
                    > записываем в текущую строку бекап, сделанный перед последней операцией 1 или 2

                #5. Redo() -- выполнить заново последнюю отменённую с помощью Undo операцию;
                # Redo должна уметь выполняться при необходимости неограниченное число раз.
                if curr_id == '5':
                    
            else:
                return curr_str













#1. Добавить(S) -- в конец текущей строки (исходно пустая) добавляется строка S;
    def add_in_tail(string):
        curr_str += string


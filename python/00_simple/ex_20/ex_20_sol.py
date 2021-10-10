curr_str = ''
undo_done = False
undo_log = []
redo_log = []

def S_is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def BastShoe(command):
    
    def undo_log_update():
        global curr_str, undo_done, undo_log, redo_log
        if undo_done:
            undo_done = False
            undo_log = [curr_str]
            redo_log = []
        else:
            undo_log += [curr_str]

    def get_head(string):
        cnt = 1
        while string[cnt] == ' ':
            cnt += 1
        return cnt

    def get_tail(string):
        cnt = len(string) - 1
        while string[cnt] == ' ':
            cnt -= 1
        return cnt


    def add_in_tail():
        global curr_str, undo_done, undo_log, redo_log
        if len(cmd_splitted) > 1:
            undo_log_update()
            curr_str += command[get_head(command):get_tail(command)+1]
        return curr_str

    def delete(N):
        global curr_str, undo_done, undo_log, redo_log
        undo_log_update()
        if N>=len(curr_str):
            curr_str = ''
        else:
            curr_str = curr_str[:len(curr_str)-N]
        return curr_str
        
    def get_letter(N):
        global curr_str, undo_done, undo_log, redo_log
        if N>=len(curr_str):
            return ''
        else:
            return curr_str[N]

    def undo():
        global curr_str, undo_done, undo_log, redo_log
        undo_done = True
        if undo_log != []:
            redo_log += [curr_str]
            curr_str = undo_log[len(undo_log)-1]
            undo_log = undo_log[:len(undo_log)-1]
        return curr_str
    
    def redo():
        global curr_str, undo_done, undo_log, redo_log
        undo_log += [curr_str]
        if redo_log != []:
            curr_str = redo_log[len(redo_log)-1]
            redo_log = redo_log[:len(redo_log)-1]
        return curr_str

    # ----------------------------

    cmd_ids = ['1', '2', '3', '4', '5']
    cmd_splitted = command.split()
    if cmd_splitted[0] in cmd_ids:
        curr_id = cmd_splitted[0]
        # id=1
        if curr_id == '1':
            return add_in_tail()

        # id=2;3
        if curr_id in ['2', '3']: 
            if len(cmd_splitted) == 2:
                N = cmd_splitted[1]
                if S_is_number(N):
                    N = int(N)
                    if curr_id == '2':
                        return delete(N)
                    if curr_id == '3':
                        return get_letter(N)

        # id=4,5
        if curr_id in ['4', '5']: 
            if len(cmd_splitted) == 1:
                if curr_id == '4':
                    return undo()
                if curr_id == '5':
                    return redo()
    #return curr_str


commands = [
                '1 Привет', 
                '1 , Мир!', 
                '1 ++ ', 
                '2 2', 
                '4', 
                '4', 
                '1 *', 
                '4', 
                '4 ', 
                '4', 
                '3 6', 
                '2 100', 
                '1 Привет', 
                '1 , Мир!', 
                '1 ++ ', 
                '4', 
                '4', 
                '5', 
                '4', 
                '5', 
                '5', 
                '5', 
                '5', 
                '4', 
                '4', 
                '2 2', 
                '4', 
                '5', 
                '5', 
                '5']

answers = [

                'Привет', 
                'Привет, Мир!', 
                'Привет, Мир!++', 
                'Привет, Мир!', 
                'Привет, Мир!++', 
                'Привет, Мир!', 
                'Привет, Мир!*', 
                'Привет, Мир!', 
                'Привет, Мир!', 
                'Привет, Мир!', 
                ',', 
                '', 
                'Привет', 
                'Привет, Мир!', 
                'Привет, Мир!++', 
                'Привет, Мир!', 
                'Привет', 
                'Привет, Мир!', 
                'Привет', 
                'Привет, Мир!', 
                'Привет, Мир!++', 
                'Привет, Мир!++', 
                'Привет, Мир!++', 
                'Привет, Мир!', 
                'Привет', 
                'Прив', 
                'Привет', 
                'Прив', 
                'Прив', 
                'Прив']

cnt = 0
for i in commands:
    print('step', cnt, '--', BastShoe(i))
    cnt += 1

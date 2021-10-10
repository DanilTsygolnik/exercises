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

    def delete(N):
        global curr_str, undo_done, undo_log, redo_log
        undo_log_update()
        if N>=len(curr_str):
            curr_str = ''
        else:
            curr_str = curr_str[:len(curr_str)-N]
        
    def get_letter(N):
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
    
    def redo():
        global curr_str, undo_done, undo_log, redo_log
        if redo_log != []:
            undo_log += [curr_str]
            curr_str = redo_log[len(redo_log)-1]
            redo_log = redo_log[:len(redo_log)-1]

    # ----------------------------

    global curr_str, undo_done, undo_log, redo_log
    
    if command[0] == '1':
        undo_log_update()
        curr_str += command[2:]
        return curr_str

    elif command[0] == '2':
        delete(int(command[2:]))
        return curr_str
        
    elif command[0] == '3':
        return get_letter(int(command[2:]))
        
    elif command[0] == '4':
        undo()
        return curr_str

    elif command[0] == '5':
        redo()
        return curr_str

    else:
        return curr_str

#
#commands = [
#                '1 Привет', 
#                '1 , Мир!', 
#                '1 ++', 
#                '2 2', 
#                '4', 
#                '4', 
#                '1 *', 
#                '4', 
#                '4 ', 
#                '4', 
#                '3 6', 
#                '2 100', 
#                '1 Привет', 
#                '1 , Мир!', 
#                '1 ++', 
#                '4', 
#                '4', 
#                '5', 
#                '4', 
#                '5', 
#                '5', 
#                '5', 
#                '5', 
#                '4', 
#                '4', 
#                '2 2', 
#                '4', 
#                '5', 
#                '5', 
#                '5']
#
#answers = [
#
#                'Привет', 
#                'Привет, Мир!', 
#                'Привет, Мир!++', 
#                'Привет, Мир!', 
#                'Привет, Мир!++', 
#                'Привет, Мир!', 
#                'Привет, Мир!*', 
#                'Привет, Мир!', 
#                'Привет, Мир!', 
#                'Привет, Мир!', 
#                ',', 
#                '', 
#                'Привет', 
#                'Привет, Мир!', 
#                'Привет, Мир!++', 
#                'Привет, Мир!', 
#                'Привет', 
#                'Привет, Мир!', 
#                'Привет', 
#                'Привет, Мир!', 
#                'Привет, Мир!++', 
#                'Привет, Мир!++', 
#                'Привет, Мир!++', 
#                'Привет, Мир!', 
#                'Привет', 
#                'Прив', 
#                'Привет', 
#                'Прив', 
#                'Прив', 
#                'Прив']
#
#cnt = 0
#for i in commands:
#    print('step', cnt, '--', BastShoe(i))
#    cnt += 1

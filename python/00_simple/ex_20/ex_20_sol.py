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
        if undo_done:
            undo_done = False
            undo_log = [curr_str]
            redo_log = []
        else:
            undo_log += [curr_str]

    def add_in_tail():
        if len(command) > 2:
            cnt = 2
            while command[cnt] == ' ' and cnt < len(command):
                cnt += 1
            undo_log_update()
            curr_str += command[cnt:]

    def delete(N):
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
        undo_done = True
        if undo_log != []:
            redo_log += [curr_str]
            curr_str = undo_log[len(undo_log)-1]
            undo_log = undo_log[:len(undo_log)-1]
    
    def redo():
        undo_log += [curr_str]
        if redo_log != []:
            curr_str = redo_log[len(redo_log)-1]
            redo_log = redo_log[:len(redo_log)-1]

    # ----------------------------

    cmd_ids = ['1', '2', '3', '4', '5']
    cmd_splitted = command.split()
    if cmd_splitted[0] in cmd_ids:
        curr_id = cmd_splitted[0]
        # id=1
        if curr_id == '1':
            add_in_tail()

        # id=2;3
        if curr_id in ['2', '3']: 
            if len(cmd_splitted) == 2:
                N = cmd_splitted[1]
                if S_is_number(N):
                    N = int(N)
                    if curr_id == '2':
                        delete(N)
                    if curr_id == '3':
                        get_letter(N)

        # id=4,5
        if curr_id in ['4', '5']: 
            if len(cmd_splitted) == 1:
                if curr_id == '4':
                    undo()
                if curr_id == '5':
                    redo()

    return curr_str

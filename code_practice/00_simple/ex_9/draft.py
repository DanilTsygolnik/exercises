
# ------------------ solution development ------------------------            
считываем строку | string_source

создаем строку без пробелов 
def letters_only(string_source, desypher_mode=False):
    words_list = string_source.split()
    if desypher_mode:
        return words_list
    else:
        output = ''
        for i in words_list:
            letters_only += i
        return output

    тут нужна не просто строка ??
    нужны также:
    - порядковые номера слов в сообщении
    - длина каждого слова (кол-во символов)


# шифровка
def sypher(string_letters_only):
    # считаем количество букв в строкe
    N = len(string_letters_only)
    
    функция расчета размеров матрицы по длине строки
        определяем параметры матрицы -- создаем пустой список | matrix_size = []
          округление (корня из N) вниз -- число строк | matrix_size[0] = 
          округление корня вверх -- число столбцов
        если строки*столбцы < длины string_only_letters ==> число строк += 1
    
        возвращаем список (параметры матрицы)

    # запись символов из исходной строки в матрицу (подготовка к шифровке)
    в каждую строку матрицы записываются буквы из строки в порядке следования
    цикл строка в матрице
        цикл: идем по строке, пока не дойдем до конца (счетчик длины строки)
            запись текущей буквы из строки (счетчик символов)
            если символ последний: # это случится на последней строке матрицы ==> из осн. цикла выйдем автоматически
                прерываем запись
            # иначе: (продолжаем)
            переходим к след. символу (счетчик символов) += 1
            переходим к след. ячейке (счетчик длины строки += 1)
    
    возвращаем заполненную матрицу

    создаем пустую строку под зашифрованное сообщение

    #зашифрованное сообщение
    цикл - i-й столбец в матрице | for i in range(matrix_size[1]) # matrix_size = [num_rows, num_columns]
        цикл - j-я строка в матрице (идем сверху вниз по столбцу) | for j in range(matrix_size[0]
            записываем i-й символ (текущий столбец - индекс буквы в слове из матрицы) в i-е слово
            если i-й столбец не последний:
                добавляем пробел в конец строки

    возвращаем зашифрованное сообщение


# дешифровка
def desypher(string_letters_only):

    допустим, считываю строку (в режиме дешифра), вывожу список слов
    
создать список из пустых списков
0-й пустой - первая строка ориг матрицы
1-я пустая - вторая и т.д.
всего пустых списков - кол-во букв в самом длинном слове (первом) в шифровке

пока так:
шаг 1 - создать список пустых списков

    matrix_filled = []
    for i in words_list[0]:
        matrix_filled.append('')

шаг 2 - заполняем матрицу

    каждое слово в шифровке - это столбец в матрице (вести счет не нужно, т.к. буквы из слова добавляю в конец каждой строки)
    индекс буквы в слове - индекс строки, в которую записывается (вот тут нужен счетчик, каждый раз с нуля)
    
    цикл: i-е слово в списке | for word in words_list
        row_index_cnt = 0
        цикл: j-я буква в слове | for j in word
            записываю j-ю букву в matrix_filled[row_index_cnt] | matrix_filled[row_index_cnt] += j

должна получиться матрица, идентичная заполненной матрице на этапе шифровки
вопрос: как из полученных строк выудить верные слова?

можно получить строку из букв и правильно разделить на пробелы. Да, все сводится к позициям пробелов

ключ к шифру - список:
- длина списка - кол-во слов в оригинальном сообщении
- значения в списке - длина каждого слова
- индексы значений в списке соответствуют индексам слов в оригинальном сообщении

шаг 3 - получить исходную строку без пробелов
    
    string_letters_only = ''
    
    
    for i in matrix_filled: # цикл: для i-й строки матрицы
        string_letters_only += i

шаг 4 - заполняю собираю расшифрованное сообщение

    message = ''

    letter_cnt = 0 # текущяя буква под запись в message
    цикл: перебираем ключи
        end_word_index = 0 # отслеживаем окончание очередного слова
        цикл: двигаемся по буквам в string_letters_only, пока не дойдем до последней буквы очередного слова:
            # цикл для слова, соотв. ключу 
            # вход в цикл возможен, только если end_word_index < key
            while end_word_index < key:
                if end_word_index == key - 1:
                    пишем пробел
                else:
                    пишем очередную букву
                end_word_index += 1
                letter_cnt += 1
        

здесь должно получиться исходное сообщение
return message

    #вопрос: как из полученных строк (см. решение, шаг 2) выудить верные слова?
    #можно получить строку из букв и правильно разделить на пробелы. Да, все сводится к позициям пробелов
    #
    #ключ к шифру - список:
    #- длина списка - кол-во слов в оригинальном сообщении
    #- значения в списке - длина каждого слова
    #- индексы значений в списке соответствуют индексам слов в оригинальном сообщении
    
    # ---- решение, если бы был ключ, и нужно было выводить строку с пробелам --------
    #шаг 4 - заполняю собираю расшифрованное сообщение
    #
    #    message = ''
    
        #letter_cnt = 0 # текущяя буква под запись в message
        #цикл: перебираем ключи
        #    end_word_index = 0 # отслеживаем окончание очередного слова
        #    цикл: двигаемся по буквам в string_letters_only, пока не дойдем до последней буквы очередного слова:
        #        # цикл для слова, соотв. ключу 
        #        # вход в цикл возможен, только если end_word_index < key
        #        while end_word_index < key:
        #            if end_word_index == key - 1:
        #                пишем пробел
        #            else:
        #                пишем очередную букву
        #            end_word_index += 1
        #            letter_cnt += 1

        # --- решение по заданию (выводим исходное сообщение, но в виде строки без пробелов) --- 

# ------------------ solution based on notes ------------------------            
 
def TheRabbitsFoot(string_input, encode=True):

    def round_custom(number, high=False):
        number_x10 = number * 10
        if high:
            round_result = int(number_x10 // 10 + 1)
        else:
            round_result = int(number_x10 // 10)
        return round_result

    # создаем строку без пробелов 
    def letters_only(message):
        words_list = message.split()
        output = ''
        for i in words_list:
            output += i
        return output

    def matrix_size_calc(message): # расчет размеров матрицы
        string_no_spaces = letters_only(message)
        letters_in_message = len(string_no_spaces)
        # заготовка списка размеров матрицы
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

        # заготовка для матрицы
        matrix = []

        if encode:
            # получаем размеры матрицы
            string_no_spaces = letters_only(message)
            letters_in_message = len(string_no_spaces)
            sizes = matrix_size_calc(message)
            # в заготовку записываем j пустых строк в соответствии с заданным размером
            for j in range(sizes[0]):
                #matrix.append('')
                matrix.append([])
            # будем записывать каждую букву в строку матрицы
            letter_index_cnt = 0
            for j in matrix: # в каждую строку матрицы
                row_index_cnt = 0
                while row_index_cnt < sizes[1] and letter_index_cnt < letters_in_message: # запись в одну строку до предела ее длины
                    #j = j + string_no_spaces[letter_index_cnt] # не нужно следить за длиной последней строки, т.к.
                    j.append(string_no_spaces[letter_index_cnt]) # запись остановится в конце строки с сообщением
                    letter_index_cnt += 1
                    row_index_cnt += 1
                if letter_index_cnt >= letters_in_message:
                    while row_index_cnt < sizes[1]:
                        j.append('')
                        row_index_cnt += 1

            # здесь должна получиться матрица нужного вида
        else:
            words_list = message.split()
            num_rows = len(words_list[0]) # кол-во строк в матрице равно длине первого столбца
            row_cnt = 0
            while row_cnt < num_rows: # создаем пустые строки
                #matrix.append('')
                matrix.append([])
                row_cnt += 1
            # заполняем матрицу
            for word in words_list: # проходим по словам, в каждом слове
                row_cnt = 0 
                for j in word: # индекс каждой буквы - индекс строки, в которую пишем эту букву
                    matrix[row_cnt] += j
                    row_cnt += 1 # переходим к сл. букве - переходим к сл. строке
            # здесь должна получиться матрица нужного вида
        return matrix

    # шифровка
    def sypher(message, encode):
    
        # шаг 1 - создаем заполненную матрицу
        matrix = get_matrix(message, encode)    
    
        # test print for matrix
        print('filled matrix test print')
        message_test = ''
        for j in matrix:
            print(j)
            for k in j:
                message_test += k
    
        message_syphered = '' # заготовка зашифрованного сообщения

        # получаем зашифрованное сообщение
        sizes = matrix_size_calc(message)
        print("num_rows =", sizes[0], "num_cols =", sizes[1])
        row_indexes = range(sizes[0])
        col_indexes = range(sizes[1])
        for i in col_indexes: # перебор столбцов; i - индекс буквы, которую берем в каждой из строк матрицы
            for j in row_indexes: # цикл - j-я строка в матрице (идем сверху вниз по столбцу)
                # записываем i-й символ (текущий столбец - индекс буквы в слове из матрицы) в i-е слово
                message_syphered += matrix[j][i]
            # добавляем пробел в конец строки
            if i != sizes[1]-1:
                message_syphered += ' '
        # здесь должно получиться зашифрованное сообщение
        return message_syphered

    # дешифровка
    def desypher(message_syphered, encode):
    
        # шаг 1 - создаем заполненную матрицу
        matrix = get_matrix(message_syphered, encode)    
        
        # должна получиться матрица, идентичная заполненной матрице на этапе шифровки
        print("matrix") # тестовый вывод
        for i in matrix:
            print(i)
        sizes = matrix_size_calc(message)
        print("num_rows =", sizes[0], "num_cols =", sizes[1])
        
        # шаг 3 - получить исходную строку без пробелов
        message_desyphered = ''
        for j in matrix: # цикл: для j-й строки матрицы
            for i in j:
                message_desyphered += i # перебор всех букв в i-й строке
        # здесь должно получиться исходное сообщение
        return message_desyphered

    # ----------------------------------------------
    if string_input == '':
        return ''
    else:
        if encode: # sypher mode
            return sypher(string_input, encode)
        else: # desypher mode
            return desypher(string_input, encode)


message = 'fo mo'
print('Original message:', message)
message_encrypted = TheRabbitsFoot(message)
print('Encrypted message:', message_encrypted)
message_decrypted = TheRabbitsFoot(message_encrypted, False)
print('Decripted message:', message_decrypted)

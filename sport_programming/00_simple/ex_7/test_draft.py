
words = get_words("1) строка разбивается на набор строк через выравнивание по заданной ширине")
get_lines(12, words, "", [])
    let_left = 12
    
    wd = 1)
        letters = 2
        2 < 12
            2 < 12
                cl = "1) "
                let_left = 9
    wd = строка
        letters = 6
        6 < 12 | letters--L
            6 < 9 | letters--let_left
                cl = "1) строка "
                let_left = -1
    wd = разбивается
        letters = 11
        11 < 12 | letters--L
            11 > -1 | letters--let_left
                nl("1) строка ", [], let_left, 12)
                    storage = ["1) строка "]
                    cl = ""
                    let_left = 12
                cl = "разбивается "
                let_left = 0
    wd = "на"
        letters = 0
        2 < 12 | letters--L
            2 > 0 | letters--let_left
                nl("разбивается ", storage, let_left, 12)
                    storage = ["1) строка ", "разбивается "]
                    cl = ""
                    let_left = 12
                cl = "на "
                let_left = 9
    wd = "набор"
        letters = 5
        5 < 12 | letters--L
            5 < 9 | letters--let_left
                cl = "на набор "
                let_left = 3
    wd = "строк"
        letters = 5
        5 < 12 | letters--L
            5 > 3 | letters--let_left
                nl
                    storage = ["1) строка ", "разбивается ", "на набор "]
                    cl = ""
                    let_left = 12
                cl = "строк "
                let_left = 6


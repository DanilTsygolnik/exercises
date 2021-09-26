def WordSearch(L, string, subs):
    print("Searching for >> "+subs+" <<\n")
    def get_words(string):
        return string.split( )
    
    def get_lines(L, words):
        
        def let_cnt(word):
            cnt = 0
            for l in word:
                cnt += 1
            return cnt
    
        let_left = L
        cl =  ""
        storage = []
    
        cnt = 1
        for wd in words:
            #print("\nCurrent word:", wd)
            #print("-------------")
            #print("current let_left:", let_left)
            #print("current line:", cl)
            if len(wd) >= L:
                if let_left != L:
                    storage.append(cl)
                    cl = ""
                    let_left = L
                while True:
                    if len(wd) <= L:
                        break
                    storage.append(wd[:L])
                    wd = wd[L:]
                if len(wd) == L:
                    storage.append(wd)
                else:
                    cl = wd + " "
                    let_left = L - len(cl)
                    if cnt == len(words):
                        storage.append(cl)
            else:
                if len(wd) <= let_left:
                    if len(wd) == let_left:
                        storage.append(cl+wd)
                        cl = ""
                        let_left = L
                    else:
                        cl += wd + " "
                        let_left = L - len(cl)
                        if cnt == len(words):
                            storage.append(cl)
                else:
                    storage.append(cl)
                    cl = wd + " "
                    let_left = L - len(cl)
                    if cnt == len(words):
                        storage.append(cl)
            #print(" - - - ")
            #print("current let_left:", let_left)
            #print("current line:", cl)
            cnt += 1
    
        print("align result\n-----------")
        for line in storage:
            print(line)
        return storage

    words = get_words(string)
    lines = get_lines(L, words)
    
    answer = []
    
    for line in lines:
        search_res = 0
        for wd in line.split():
            if wd == subs:
                search_res = 1
                break
        if search_res != 0:
            answer.append(1)
        else:
            answer.append(0)

    print("\nResult\n--------------------")
    return answer

#words = get_words("1) строка разбивается на набор строк через выравнивание по заданной ширине")
#get_lines(12, words)
#get_lines(1, words)
#get_lines(16, words)
#get_lines(17, words)
#get_lines(60, words)

print(WordSearch(3, "1) строка разбивается на набор строк через выравнивание по заданной ширине", "зад"))
print(WordSearch(12, "1) строка разбивается на набор строк через выравнивание по заданной ширине", "строк"))


    def length(wd):
        cnt = 1
        for l in wd:
            cnt += 1
        return cnt

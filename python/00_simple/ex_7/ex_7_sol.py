def WordSearch(L, string, subs):

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
            cnt += 1
    
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

    return answer

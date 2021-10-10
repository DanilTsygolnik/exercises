def switch_letters(word, index_2):
    new_word = word[index_2] + word[1:index_2] + word[0] + word[index_2+1:]
    return new_word

def get_combos(string):

    def combo_check(string):
        if string not in combos_list:
            combos_list.append(string)
            cnt = 1
            while cnt < len(string):
                new_combo = switch_letters(string, cnt)
                if new_combo not in combos_list:
                    combo_check(new_combo)
                cnt += 1

    combos_list = []
    combo_check(string)
    return combos_list

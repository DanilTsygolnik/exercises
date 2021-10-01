MassVote(int N, int [] Votes)
    N # <class integer>, num_condidates
    votes # <class list>, list of integer numbers 

    return ''

MassVote(int N, int [] Votes)

N # <class integer>, num_condidates >= 1
votes # <class list>, list of integer numbers 

 - победитель, набравший больше всех голосов и при этом более 50% голосов;
scenario 1 --> [60, 10, 10, 15, 5] --> return 'majority winner 1'

- победитель, набравший больше всех голосов и при этом менее или ровно 50% голосов;
scenario 2 --> [10, 15, 10] --> return 'minority winner 2'

- перевыборы (выявлено несколько победителей с одинаковым количеством голосов). 
scenario 3 --> [111, 111, 110, 110] --> return 'no winner'


```python
def MassVote(num_candidates, votes):
    
    total_votes = 0
    max_num_votes = 0
    max_cnt = 0
    votes_index_cnt = 0
    for i in votes:
        total_votes += i
        if i > max_num_votes:
            max_count = 1
            max_num_votes = i
            winner = votes_index_cnt + 1
        elif i == max_num_votes:
            #max_cnt += 1
            winner = None
            break # т.к. не требуется выводить номера кандидатов с одинаковым числом голосов, можно не продолжать перебор
        votes_index_cnt += 1
    
    # ожидаемые результаты здесь:
    сценарий 1, 2: сумма, max_count = 1, winner_id = X
    сценарий 3: сумма, max_count = n, winner = None

    if winner != None: # есть победитель
        proportion = 100 * round((max_num_votes/total_votes), 3)
        if proportion > 50.0:
            return 'majority winner ' + str(winner)
        else:
            return 'minority winner ' + str(winner)
    else:
        return 'no winner'
            
        
Кроме того, нужно реализовать анализ каждого результата по отношению к остальным (3 сценария):
1. максимум единственный --> сценарий 1 или 2, нужно подсчитать долю голосов победителя в общем кол-ве
2. максимумов несколько --> сценарий 3, подсчитывать долю от суммы не нужно

```

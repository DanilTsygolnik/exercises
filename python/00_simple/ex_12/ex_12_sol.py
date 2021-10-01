def MassVote(num_candidates, votes):
    total_votes = 0
    max_num_votes = 0
    votes_index_cnt = 0
    for i in votes:
        total_votes += i
        if i > max_num_votes:
            max_count = 1
            max_num_votes = i
            winner = votes_index_cnt + 1
        elif i == max_num_votes:
            winner = None
        votes_index_cnt += 1
    if winner != None:
        proportion = 100 * round((max_num_votes/total_votes), 3)
        if proportion > 50.0:
            return 'majority winner ' + str(winner)
        else:
            return 'minority winner ' + str(winner)
    else:
        return 'no winner'

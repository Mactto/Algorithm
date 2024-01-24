def solution(players, callings):
    rank_dict = {}
    for rank, player in enumerate(players):
        rank_dict[player] = rank

    for calling in callings:
        callee_rank = rank_dict[calling]
        front_player = players[callee_rank-1]
        players[callee_rank], players[callee_rank-1] = players[callee_rank-1], players[callee_rank]
        rank_dict[calling] = callee_rank - 1
        rank_dict[front_player] = callee_rank

    return players
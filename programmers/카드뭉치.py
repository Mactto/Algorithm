def solution(cards1, cards2, goal):
    card1_idx = 0
    card2_idx = 0
    
    for g in goal:
        if g == cards1[card1_idx]:
            if len(cards1) - 1 > card1_idx:
                card1_idx += 1
        elif g == cards2[card2_idx]:
            if len(cards2) - 1 > card2_idx:
                card2_idx += 1
        else:
            return "No"
            
    return "Yes"
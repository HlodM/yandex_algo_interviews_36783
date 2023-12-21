def get_card_count(n, k, cards) -> int:
    max_score = cur_score = sum(cards[:k])
    for i in range(k):
        cur_score += -cards[k-1-i] + cards[n-1-i]
        max_score = max(max_score, cur_score)
    return max_score


n = int(input())
k = int(input())
cards = list(map(int, input().split()))

print(get_card_count(n, k, cards))

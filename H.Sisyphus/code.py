import heapq


def get_min_energy(heaps):
    heapq.heapify(heaps)
    min_energy = 0
    while len(heaps) > 1:
        two_mins = heapq.heappop(heaps) + heapq.heappop(heaps)
        min_energy += two_mins
        heapq.heappush(heaps, two_mins)

    return min_energy


n = int(input())
heaps = list(map(int, input().split()))
print(get_min_energy(heaps))

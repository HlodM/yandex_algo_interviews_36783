import heapq


def get_max_final_capital(buildings, start_capital, max_buildings):
    max_capital = start_capital
    heapq.heapify(buildings)
    profit_heap = []
    for _ in range(max_buildings):
        while buildings and buildings[0][0] <= max_capital:
            _, profit = heapq.heappop(buildings)
            heapq.heappush(profit_heap, -profit)
        max_capital -= heapq.heappop(profit_heap) if profit_heap else 0

    return max_capital


with open('input.txt') as f:
    n, k = map(int, f.readline().split())
    buildings = []
    for _ in range(n):
        buildings.append(tuple(map(int, f.readline().split())))
    M = int(f.readline())


print(get_max_final_capital(buildings, M, k))

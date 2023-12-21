class HistoricalArray:
    def __init__(self, size) -> None:
        self.era_counter = 0
        self.eras_dict = {0: 0}
        self.array = [[[0], [0]] for _ in range(size)]

    def set(self, index, value) -> None:
        if self.array[index][-1] == self.era_counter:
            self.array[index][-2] = value
        else:
            self.array[index][0].append(value)
            self.array[index][1].append(self.era_counter)

    def get(self, index, era_id) -> int:
        era_pos = self.eras_dict[era_id]
        if self.array[index][1][-1] <= era_pos:
            return self.array[index][0][-1]
        idx = self.bin_search(self.array[index][1], era_pos)
        return self.array[index][0][idx]

    def begin_new_era(self, era_id) -> None:
        self.era_counter += 1
        self.eras_dict[era_id] = self.era_counter

    @staticmethod
    def bin_search(arr, pos):
        left, right = 0, len(arr) - 1
        while left < right:
            m = (left + right + 1) // 2
            if arr[m] > pos:
                right = m - 1
            else:
                left = m
        return left


size = int(input())
q = int(input())
historical_array = HistoricalArray(size)
for i in range(q):
    query = input().split()
    query_type = query[0]
    if query_type == "set":
        historical_array.set(int(query[1]), int(query[2]))
    elif query_type == "begin_new_era":
        historical_array.begin_new_era(int(query[1]))
    else:
        print(historical_array.get(int(query[1]), int(query[2])))

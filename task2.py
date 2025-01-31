import heapq

def merge_k_lists(iterable):
    merged = []
    heap = []
    heapq.heapify(heap)
    for list in iterable:
        for elem in list:
            heapq.heappush(heap, elem)

    while heap:
        merged.append(heapq.heappop(heap))
    return merged

# Дано
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

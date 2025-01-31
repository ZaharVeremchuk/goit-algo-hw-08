import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables) 
    total_cost = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables) 
        connection_cost = cable1 + cable2 
        total_cost += connection_cost 
        heapq.heappush(cables, connection_cost)  

    return total_cost

# Дано
cables = [5, 2, 10, 3, 7, 1]
min_cost = min_cost_to_connect_cables(cables)
print("Мінімальні витрати:", min_cost)  # Виведе: Мінімальні витрати: 65
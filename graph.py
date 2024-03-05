from collections import Counter

# По системе двусторонних дорог, определить, можно ли, закрыв какие-либо три из них,
# добиться того, чтобы из города А нельзя было попасть в город В.



def can_reach(graph, start, end, Counter):
    visited = set()
    stack = [start]
    Counter = 0

    while stack:
        current = stack.pop()
        visited.add(current)
        if current == end:
            Counter += 1
            #return Counter
        for neighbor in range(len(graph[current])):
            if graph[current][neighbor] == 1 and neighbor not in visited:
                stack.append(neighbor)
        #Counter += 1


    return Counter

# Матрица смежности графа
graph = {
1 : [0, 1, 1, 1, 0, 0],
2 : [1, 0, 1, 0, 0, 0],
3 : [1, 1, 0, 1, 1, 0],
4 : [1, 0, 1, 0, 0, 0],
5 : [0, 0, 1, 0, 0, 1],
0 : [0, 0, 0, 0, 1, 0]
}

# Город A и город B
start = 1
end = 2

Counter = can_reach(graph, start, end, Counter)

# Проверяем, можно ли из города A попасть в город B
print(Counter)
if Counter > 3:
    print("Из города A можно попасть в город B")
else:
    print("Из города A нельзя попасть в город B")

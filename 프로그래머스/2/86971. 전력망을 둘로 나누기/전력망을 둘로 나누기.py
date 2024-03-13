def solution(n, wires):
    from collections import defaultdict

    def build_graph(wires):
        graph = defaultdict(list)
        for v1, v2 in wires:
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph

    def count_nodes(graph, start, blocked_edge):
        visited = set()
        stack = [start]
        count = 0

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                count += 1
                for neighbor in graph[node]:
                    if (node, neighbor) != blocked_edge and (neighbor, node) != blocked_edge:
                        stack.append(neighbor)
        return count

    graph = build_graph(wires)
    min_difference = n
    
    for v1, v2 in wires:
        count1 = count_nodes(graph, v1, (v1, v2))
        count2 = n - count1  
        difference = abs(count1 - count2)  

        if difference < min_difference:
            min_difference = difference

    return min_difference



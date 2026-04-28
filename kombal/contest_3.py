import heapq


def solve():
    try:
        with open('in_2.txt', 'r') as f:
            data = f.read().split()
    except FileNotFoundError:
        return

    if not data:
        return

    ptr = 0
    n = int(data[ptr])
    ptr += 1

    adj = [[] for _ in range(n + 1)]

    for v in range(1, n + 1):
        while True:
            u = int(data[ptr])
            ptr += 1
            if u == 0:
                break
            weight = int(data[ptr])
            ptr += 1
            adj[u].append((v, weight))

    source = int(data[ptr])
    target = int(data[ptr + 1])

    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[source] = 0
    parent = {i: None for i in range(1, n + 1)}
    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > distances[u]:
            continue

        for v, weight in adj[u]:
            distance = current_dist + weight
            if distance < distances[v]:
                distances[v] = distance
                parent[v] = u
                heapq.heappush(pq, (distance, v))

    with open('out_2.txt', 'w') as out:
        if distances[target] == float('inf'):
            out.write("N")
        else:
            path = []
            curr = target
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()

            out.write("Y\n")
            out.write(" ".join(map(str, path)) + "\n")
            out.write(str(distances[target]))


if __name__ == "__main__":
    solve()

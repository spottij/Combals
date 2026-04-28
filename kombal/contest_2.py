import sys

def solve():
    try:
        with open('in_1.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return

    if not lines:
        return

    n = int(lines[0].strip())
    adj_matrix = [] # список списков
    for i in range(1, n + 1):
        adj_matrix.append(list(map(int, lines[i].split())))

    visited = [False] * n
    components = []

    def dfs(v, current_component):
        visited[v] = True
        current_component.append(v + 1)
        for neighbor in range(n):
            if adj_matrix[v][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor, current_component)

    for i in range(n):
        if not visited[i]:
            component = []
            dfs(i, component)
            component.sort()
            components.append(component)
    with open('out_1.txt', 'w') as f:
        f.write(f"{len(components)}\n")
        for comp in components:
            f.write(" ".join(map(str, comp)) + "\n")
if __name__ == "__main__":
    solve()
class GraphColoring:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.graph = [[0]*n for _ in range(n)]
        self.colors = [0]*n

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def is_safe(self, v, c):
        for i in range(self.n):
            if self.graph[v][i] == 1 and self.colors[i] == c:
                return False
        return True

    def solve(self, v=0):
        if v == self.n:
            return True

        for c in range(1, self.k+1):
            if self.is_safe(v, c):
                self.colors[v] = c

                if self.solve(v+1):
                    return True

            
                self.colors[v] = 0

        return False


def read_input(file_name):
    with open(file_name, 'r') as f:
        data = f.readlines()

    n, m, k = map(int, data[0].split())
    gc = GraphColoring(n, k)

    for i in range(1, m+1):
        u, v = map(int, data[i].split())
        gc.add_edge(u, v)

    return gc


if __name__ == "__main__":
    file_name = "input.txt"  
    gc = read_input(file_name)

    if gc.solve():
        print(f"Coloring Possible with {gc.k} Colors")
        print("Color Assignment:", gc.colors)
    else:
        print(f"Coloring Not Possible with {gc.k} Colors")

class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, src, dest):
        if src not in self.graph:
            self.add_node(src)
        if dest not in self.graph:
            self.add_node(dest)
        self.graph[src].append(dest)

    def has_cycle(self):
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                # Cycle detected
                return True
            if node in visited:
                return False

            visiting.add(node)
            for neighbor in self.graph.get(node, []):
                if dfs(neighbor):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False

        for node in self.graph:
            if dfs(node):
                return True

        return False

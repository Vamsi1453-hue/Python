class Graph:
    def __init__(self, directed=False):
        self.adj       = {}
        self.directed = directed
    def add_vertex(self,v):
        self.adj.setdefault(v,[])
    def add_edge(self,u,v,weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v,weight))
        if not self.directed:
            self.adj[v].append((u,weight))
    def neighbours(self,v):
        return [n for n, _ in self.adj.get(v, [])]
    
g = Graph()
for u,v in [("A","B"),("A","C"),("A","E"),("B","D"),("C","E"),("D","E")]:
    g.add_edge(u,v)
print(g.neighbours("A"))

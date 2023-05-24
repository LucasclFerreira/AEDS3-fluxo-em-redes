class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adj = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, v1, v2):
        self.lista_adj[v1].append(v2)
        self.lista_adj[v2].append(v1)

    def remover_aresta(self, v1, v2):
        self.lista_adj[v1].remove(v2)
        self.lista_adj[v2].remove(v1)

    def mostrar_lista(self):
        for i in range(self.num_vertices):
            print(f"[V{i}]", end="")
            for vert in self.lista_adj[i]:
                print(f"-> {vert}", end="")
            print()


grafo = Grafo(8)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 4)
grafo.adicionar_aresta(3, 5)
grafo.adicionar_aresta(4, 5)
grafo.adicionar_aresta(4, 6)
grafo.adicionar_aresta(6, 7)

grafo.remover_aresta(0, 2)

grafo.mostrar_lista()

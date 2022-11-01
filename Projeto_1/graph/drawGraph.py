import networkx as nx
import matplotlib.pyplot as plt

from utils.utils import Vertice, Edge


def draw_graph(vertices: list[Vertice], edges: list[Edge]):
    G = nx.Graph()

    labels = {}
    positions = {}
    for v in vertices:
        labels[v] = str(v.weight)
        positions[v] = [v.x, v.y]
        G.add_node(v)

    for e in edges:
        G.add_edge(e.v1, e.v2)

    nx.draw(G, labels=labels, with_labels=True, node_size=300, width=2, font_size=10, pos=positions)
    plt.show()
    plt.close()



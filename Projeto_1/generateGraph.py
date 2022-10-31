import math
import numpy as np

from utils import Vertice, Edge


def generate_graph(v, p):
    n_mec = 98497

    np.random.seed(n_mec)
    num_edges = math.floor(v * p)

    vertices = []
    while len(vertices) < v:

        x = np.random.randint(1, 21)
        y = np.random.randint(1, 21)
        vertice_weight = np.random.randint(1, 30)

        vertice = Vertice(x, y, vertice_weight)

        if vertice not in vertices:
            vertices.append(vertice)

    edges = []
    while len(edges) < num_edges:

        v1_idx = np.random.randint(0, v)
        v2_idx = np.random.randint(0, v)

        v1 = vertices[v1_idx]
        v2 = vertices[v2_idx]

        edge = Edge(v1, v2)

        if v1 != v2 and edge not in edges:
            edges.append(edge)

    return vertices, edges

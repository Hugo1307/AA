from itertools import chain, combinations
from math import comb
from domainClasses import Vertice, Edge, Clique


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def is_clique(vertice_subset: list[Vertice], edges: list[Edge]):

    edges_found = []
    vertices_in_subset_count = len(vertice_subset)

    if comb(vertices_in_subset_count, 2) > len(edges):
        return False

    for current_vertice_idx in range(0, vertices_in_subset_count):
        for next_vertice_idx in range(0, vertices_in_subset_count):

            if current_vertice_idx == next_vertice_idx:
                continue

            current_vertice = vertice_subset[current_vertice_idx]
            next_vertice = vertice_subset[next_vertice_idx]

            temp_edge = Edge(current_vertice, next_vertice)

            if temp_edge in edges and temp_edge not in edges_found:
                edges_found.append(temp_edge)
                # print("Found Edge: ", temp_edge)

    """
    There is one edge for each choice of two vertices, therefore, the number of edges
    is equal to the combination of (n 2) i.e., from each n vertices choose 2
    """
    return len(edges_found) > 0 and len(edges_found) == comb(vertices_in_subset_count, 2)


def subset_weight_sum(vertices_subset: list[Vertice]):

    weight_sum = 0
    for vertice in vertices_subset:
        weight_sum += int(vertice.weight)
    return weight_sum


def get_vertice_neighbors(vertice: Vertice, edges: list[Edge]) -> list[Vertice]:

    neighbors = []

    for edge in edges:
        if edge.v1 == vertice:
            neighbors.append(edge.v2)
        if edge.v2 == vertice:
            neighbors.append(edge.v1)

    return neighbors


def print_results(max_weight_clique: Clique):

    if max_weight_clique is not None:

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        print(" Results Found!")
        print()
        print(" Max Weight Clique:")
        print("  ", max_weight_clique.vertices)
        print()
        print(" Max Weight:")
        print("  ", max_weight_clique.weight)
        print()
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    else:

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        print(" No Cliques found...")
        print()
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

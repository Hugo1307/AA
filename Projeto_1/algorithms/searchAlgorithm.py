from typing import Tuple

from graph import generateGraph
from utils.domainClasses import Clique, Vertice, Edge
from graph.drawGraph import draw_graph


class SearchAlgorithm:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def perform_search(self) -> Clique:
        raise NotImplemented()

    def draw_graph(self):
        # Draw the graph
        draw_graph(self.vertices, self.edges)

    @staticmethod
    def print_results(clique: Clique, header: str):

        if clique is not None:

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print()
            print(f" {header}")
            print()
            print(" Max Weight Clique:")
            print("  ", clique.vertices)
            print()
            print(" Max Weight:")
            print("  ", clique.weight)
            print()
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        else:

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print()
            print(" No Cliques found...")
            print()
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

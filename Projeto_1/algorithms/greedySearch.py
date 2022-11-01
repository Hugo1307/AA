from algorithms.searchAlgorithm import SearchAlgorithm
from utils import utils
from utils.domainClasses import Clique


class GreedySearch(SearchAlgorithm):

    def __init__(self, vertices_count, edges_probability):
        super().__init__(vertices_count, edges_probability)

    def perform_search(self) -> Clique:

        vertices_queue = []

        # Sort the vertices by their weight
        sorted_vertices = sorted(self.vertices, key=lambda v: v.weight, reverse=True)

        # Get starting vertice (the highest weight vertice with neighbors)
        for vertice in sorted_vertices:
            vertice_neighbors = utils.get_vertice_neighbors(vertice, self.edges)
            if len(vertice_neighbors) > 0:
                vertices_queue.append(vertice)
                break

        while True:

            highest_neighbor = utils.get_max_common_neighbor(vertices_queue, self.edges)
            if highest_neighbor is None:
                break

            vertices_queue.append(highest_neighbor)

        return Clique(vertices_queue, sum(map(lambda v: v.weight, vertices_queue)))

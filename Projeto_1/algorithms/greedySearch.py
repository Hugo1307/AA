from algorithms.searchAlgorithm import SearchAlgorithm
from utils import utils
from utils.domainClasses import Clique
from utils.utils import is_clique


class GreedySearch(SearchAlgorithm):

    def __init__(self, vertices_count, edges_probability):
        super().__init__(vertices_count, edges_probability)

    def perform_search(self) -> tuple[Clique, int, int]:

        vertices_queue = []
        performed_operations = 0
        tested_solutions = 0

        # Sort the vertices by their weight
        sorted_vertices = sorted(self.vertices, key=lambda v: v.weight, reverse=True)

        # Get starting vertice (the highest weight vertice with neighbors)
        for vertice in sorted_vertices:
            vertice_neighbors, operations_count = utils.get_vertice_neighbors(vertice, self.edges)
            performed_operations += operations_count
            if len(vertice_neighbors) > 0:
                vertices_queue.append(vertice)
                break

        while True:

            highest_neighbor, operations_count = utils.get_max_common_neighbor(vertices_queue, self.edges)
            performed_operations += operations_count
            if highest_neighbor is None and is_clique(vertices_queue, self.edges):
                tested_solutions += 1
                break

            vertices_queue.append(highest_neighbor)

        return (Clique(vertices_queue, sum(map(lambda v: v.weight, vertices_queue))), performed_operations,
                tested_solutions)

from algorithms.searchAlgorithm import SearchAlgorithm
from utils.domainClasses import Clique
from utils.utils import powerset, is_clique


class ExhaustiveSearch(SearchAlgorithm):

    def __init__(self, vertices_count, edges_probability):
        super().__init__(vertices_count, edges_probability)

    def perform_search(self) -> tuple[Clique | None, int, int]:

        # With Optimization
        # self.vertices = self.optimize_vertices(self.vertices, self.edges)

        performed_operations = 0
        tested_solutions = 0

        # Generate all Subsets of vertices
        all_vertices_subsets, operations_count = list(powerset(self.vertices))
        performed_operations += operations_count

        all_cliques_found = []

        for vertice_subset in all_vertices_subsets:

            vertice_subset_is_clique, operations_count = is_clique(vertice_subset, self.edges)
            performed_operations += operations_count

            if vertice_subset_is_clique:
                # print("Clique found in subset {0}".format(vertice_subset))
                new_clique = Clique(vertice_subset, sum(map(lambda v: v.weight, vertice_subset)))
                all_cliques_found.append(new_clique)

            tested_solutions += 1

        return (max(all_cliques_found, key=lambda clique: clique.weight) if len(all_cliques_found) > 0 else None,
                performed_operations, tested_solutions)

    # Remove all the vertices disconnected before generating subsets.
    # Disconnected vertices can be removed because they won't form cliques
    @staticmethod
    def optimize_vertices(vertices_list, edges):
        vertices_list = list(filter(lambda v: v.is_connected(edges), vertices_list))
        return vertices_list

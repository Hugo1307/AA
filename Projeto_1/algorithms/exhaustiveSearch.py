from algorithms.searchAlgorithm import SearchAlgorithm
from utils.domainClasses import Clique
from utils.utils import powerset, is_clique


class ExhaustiveSearch(SearchAlgorithm):

    def __init__(self, vertices_count, edges_probability):
        super().__init__(vertices_count, edges_probability)

    def perform_search(self) -> Clique:

        # With Optimization
        vertices = self.optimize_vertices(self.vertices, self.edges)

        # Generate all Subsets of vertices
        all_vertices_subsets = list(powerset(vertices))

        all_cliques_found = []

        for vertice_subset in all_vertices_subsets:

            if is_clique(vertice_subset, self.edges):
                # print("Clique found in subset {0}".format(vertice_subset))
                new_clique = Clique(vertice_subset, sum(map(lambda v: v.weight, vertice_subset)))
                all_cliques_found.append(new_clique)

        return max(all_cliques_found, key=lambda clique: clique.weight) if len(all_cliques_found) > 0 else None

    # Remove all the vertices disconnected before generating subsets.
    # Disconnected vertices can be removed because they won't form cliques
    @staticmethod
    def optimize_vertices(vertices_list, edges):

        vertices_amount_before_optimization = len(vertices_list)
        vertices_list = list(filter(lambda v: v.is_connected(edges), vertices_list))
        vertices_amount_after_optimization = len(vertices_list)

        print(
            f"Optimization removed {vertices_amount_before_optimization - vertices_amount_after_optimization} vertices.")

        return vertices_list

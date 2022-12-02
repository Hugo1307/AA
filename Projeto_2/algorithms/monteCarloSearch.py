import random
from math import comb

from algorithms.searchAlgorithm import SearchAlgorithm
from utils.domainClasses import Clique
from utils.utils import is_clique


class MonteCarloSearch(SearchAlgorithm):

    def __init__(self, vertices, edges_probability):
        super().__init__(vertices, edges_probability)

    def perform_search(self) -> tuple[Clique, int, int]:

        performed_operations = 0
        tested_solutions = 0

        # Sort the vertices by their weight
        # sorted_vertices = sorted(self.vertices, key=lambda v: v.weight, reverse=True)

        testing_vertices_count = 1
        max_clique = None

        while testing_vertices_count <= len(self.vertices):

            # Incrementing the amount of vertices to test for next iteration
            testing_vertices_count += 1

            max_combinations_count = comb(len(self.vertices), testing_vertices_count)
            tested_subsets = list()

            while len(tested_subsets) < max_combinations_count:

                subset = set()

                while len(subset) < testing_vertices_count:
                    random_vertice_idx = random.randint(0, len(self.vertices) - 1)
                    random_vertice = self.vertices[random_vertice_idx]
                    subset.add(random_vertice)

                # for _ in range(0, testing_vertices_count):
                #     random_vertice_idx = random.randint(0, len(self.vertices) - 1)
                #     random_vertice = self.vertices[random_vertice_idx]
                #     subset.append(random_vertice)

                tuple_subset = tuple(subset)

                # If we already calculated this subset interrupt the loop
                if tuple_subset not in tested_subsets:
                    # print(f"Subset {subset} is in tested_subsets")
                    tested_subsets.append(tuple_subset)
                    #print("Appended tuple: ", tuple_subset)

                #print("TESTING SUBSET ", tuple_subset)

                is_clique_bool, n = is_clique(list(subset), self.edges)

                #print("TEST RESULT", is_clique_bool)

                performed_operations += 1

                if is_clique_bool:
                    clique_weight = sum(list(map(lambda x: x.weight, list(subset))))
                    current_clique = Clique(list(subset), clique_weight)
                    if max_clique is None or max_clique.weight < clique_weight:
                        max_clique = current_clique

            #print("Tested Subsets:", tested_subsets)

        return max_clique, performed_operations, tested_solutions

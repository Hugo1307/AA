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

        max_clique = None

        # Generate subsets with n elements. N varies from 2 up to "len(self.vertices)"
        for number_of_vertices_in_subset in range(2, len(self.vertices)+1):

            # Here, I use a set because we will not have duplicated entries once we will not test the same subset twice,
            # and we can use the O(1) average complexity for "in" operation inside python set. This will make our
            # algorithm slightly faster
            tested_subsets = set()

            # The maximum number of possible subsets with "number_of_vertices_in_subset" elements in a list with
            # "len(self.vertices)" elements
            max_combinations_count = comb(len(self.vertices), number_of_vertices_in_subset)

            # While we didn't test all the possible subsets
            while len(tested_subsets) < max_combinations_count:

                # We use a set because we don't want to add the same vertice twice in the same subset.
                subset = set()

                # While our subset doesn't have the necessary number of vertices, keep getting random vertices and
                # try to add them to the subset
                while len(subset) < number_of_vertices_in_subset:
                    random_vertice_idx = random.randint(0, len(self.vertices) - 1)
                    random_vertice = self.vertices[random_vertice_idx]
                    subset.add(random_vertice)

                # We create a frozen set that is hashable (and can be appended to a list) but also
                # contains the properties of a set, i.e., doesn't care about the order of its elements.
                frozen_subset = frozenset(subset)

                # If we already calculated this subset interrupt the loop to avoid unnecessary operations
                if frozen_subset in tested_subsets:
                    continue

                # Mark the current subset as testes so we don't test it again in the future
                tested_subsets.add(frozen_subset)

                # Check if the current subset is a clique
                is_clique_bool, n = is_clique(list(subset), self.edges)
                performed_operations += 1

                # Calculate the weight of the current clique and update the maximum weight clique if needed
                if is_clique_bool:

                    clique_weight = sum(list(map(lambda x: x.weight, list(subset))))
                    current_clique = Clique(list(subset), clique_weight)

                    if max_clique is None or max_clique.weight < clique_weight:
                        max_clique = current_clique

        return max_clique, performed_operations, tested_solutions

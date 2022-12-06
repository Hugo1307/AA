import math
import random
import time
from math import comb

from algorithms.searchAlgorithm import SearchAlgorithm
from utils.domainClasses import Clique
from utils.utils import is_clique


# Probabilistic Monte Carlo Algorithm Search
class MonteCarloProbSearch(SearchAlgorithm):

    def __init__(self, vertices, edges_probability, ):
        super().__init__(vertices, edges_probability)

    def perform_search(self) -> tuple[Clique, int, int]:

        performed_operations = 0
        tested_solutions = 0
        start_time = time.time()

        # Sort the vertices by their weight
        sorted_vertices = sorted(self.vertices, key=lambda v: v.weight, reverse=True)

        max_clique = None

        # Generate subsets with n elements. N varies from 2 up to "len(self.vertices)"
        for number_of_vertices_in_subset in range(2, len(sorted_vertices) + 1):

            # Here, I use a set because we will not have duplicated entries once we will not test the same subset twice,
            # and we can use the O(1) average complexity for "in" operation inside python set. This will make our
            # algorithm slightly faster
            tested_subsets = set()

            time_elapsed = time.time() - start_time

            # While we didn't test all the possible subsets
            while len(tested_subsets) < self.get_subset_test_count(len(sorted_vertices), number_of_vertices_in_subset) \
                    and not self.is_over_limits(performed_operations, time_elapsed, tested_solutions):

                time_elapsed = time.time() - start_time

                # We use a set because we don't want to add the same vertice twice in the same subset.
                subset = set()

                # While our subset doesn't have the necessary number of vertices, keep getting random vertices and
                # try to add them to the subset
                while len(subset) < number_of_vertices_in_subset:

                    # Use a random vertice that is in the first 60% elements of the list 80% of the times
                    # Use a random vertice that is in the last 40% elements of the list 20% of the times
                    random_prob = random.random()
                    if random_prob < 0.80:
                        random_vertice_idx = random.randint(0, math.floor(len(sorted_vertices)*0.6))
                    else:
                        random_vertice_idx = random.randint(math.floor(len(sorted_vertices)*0.6), len(sorted_vertices)-1)

                    random_vertice = sorted_vertices[random_vertice_idx]
                    subset.add(random_vertice)

                # We create a frozen set that is hashable (and can be appended to a list) but also
                # contains the properties of a set, i.e., doesn't care about the order of its elements.
                frozen_subset = frozenset(subset)

                # If we already calculated this subset interrupt the loop to avoid unnecessary operations
                if frozen_subset in tested_subsets:
                    continue

                # Mark the current subset as tested, so we don't test it again in the future
                tested_subsets.add(frozen_subset)

                # Check if the current subset is a clique
                is_clique_bool, n = is_clique(list(subset), self.edges)
                tested_solutions += 1
                performed_operations += n

                # Calculate the weight of the current clique and update the maximum weight clique if needed
                if is_clique_bool:

                    clique_weight = sum(list(map(lambda x: x.weight, list(subset))))
                    current_clique = Clique(list(subset), clique_weight)

                    if max_clique is None or max_clique.weight < clique_weight:
                        max_clique = current_clique

        return max_clique, performed_operations, tested_solutions

    # Check if the algorithm should be stopped due to meeting certain conditions
    @staticmethod
    def is_over_limits(operations_count, time_limit, tested_solutions):

        max_operations = 500000        # 500 k
        max_time_limit = 1              # 5 seconds
        max_tested_solutions = 50000   # 50 k

        if operations_count is not None and operations_count > max_operations:
            return True
        if time_limit is not None and time_limit > max_time_limit:
            return True
        if tested_solutions is not None and tested_solutions > max_tested_solutions:
            return True

    @staticmethod
    def get_subset_test_count(vertices_length, items_in_subset):
        max_subsets_amount = comb(vertices_length, items_in_subset)
        cut_probability = (-10 + 50 / (1.6*math.log10(items_in_subset))) / 100
        # print(f"Items in subset: {items_in_subset}; Cut probability: {cut_probability}")
        return max_subsets_amount * cut_probability

from utils import utils
from algorithms.searchAlgorithm import SearchAlgorithm
from utils.domainClasses import Clique


class BacktrackingSearch(SearchAlgorithm):

    def __init__(self, vertices_count, edges_probability):
        super().__init__(vertices_count, edges_probability)

    def perform_search(self) -> Clique:

        cliques_found = []

        vertices_queue = []
        visited_vertices = set()

        # Sort the vertices by their weight
        sorted_vertices = sorted(self.vertices, key=lambda v: v.weight, reverse=True)

        current_vertice_idx = None

        while True:

            # If we are in the beginning or back tracked to the first vertice
            if len(vertices_queue) == 0:

                # Get the first vertice - the vertice that is more likely to generate the maximum weight clique
                # I.e., the vertice with the higher weight that was not analysed yet.
                starting_vertice, current_vertice_idx = self.get_first_vertice(sorted_vertices, current_vertice_idx)
                vertices_queue.append(starting_vertice)

                # We "started again" i.e., selected a new first vertice, so we can clean up the visited vertices
                visited_vertices = set()

                # If we have analysed all vertices - tried to start form a clique starting in each one of
                # the vertices, we can exit the loop because we've already tried all possible vertices
                # combinations that could create cliques.
                if starting_vertice is None:
                    break

            # If we are not in the beginning, we get the vertice with the higher weight that is connected to
            # all the vertices in the current queue. We want to get a vertice that is connected to each one of
            # the others, so we can make sure a clique will be formed - discarding the vertices that would not
            # form a clique.

            # Get the vertice with the highest weight that is neighbor of all the others in the queue - form a clique.
            max_weight_neighbor_vertice = utils.get_max_common_neighbor(vertices_queue, self.edges)

            # If we found a vertice that is neighbor of all the others (is not None)
            # and we haven't visited it yet, let's check it
            if max_weight_neighbor_vertice is not None and max_weight_neighbor_vertice not in visited_vertices:

                # Let's append it to the vertices queue and add it to visited vertices, so we avoid loops
                vertices_queue.append(max_weight_neighbor_vertice)
                visited_vertices.add(max_weight_neighbor_vertice)

                # If the vertices in the queue form a Clique
                if utils.is_clique(vertices_queue, self.edges):
                    # Create a Clique entity and add it to a list
                    new_clique = Clique(vertices_queue.copy(), sum(map(lambda v: v.weight, vertices_queue)))
                    cliques_found.append(new_clique)

            # If the current vertice does not have neighbors, do a backtracking
            else:
                vertices_queue.pop(-1)

        # Clique with the highest Weight
        return max(cliques_found, key=lambda x: x.weight) if len(cliques_found) > 0 else None

    @staticmethod
    def get_first_vertice(sorted_vertices, current_first_vertice):

        current_first_vertice = current_first_vertice + 1 if current_first_vertice is not None else 0

        if current_first_vertice < len(sorted_vertices):
            return sorted_vertices[current_first_vertice], current_first_vertice
        else:
            return None, current_first_vertice


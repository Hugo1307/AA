from functools import reduce

from drawGraph import draw_graph
from generateGraph import generate_graph
import utils
from domainClasses import Vertice, Clique


def calculate_max_weight_clique_with_heuristic(vertices_count=50, edges_probability=.75):

    # Generate Graph vertices and edges
    vertices, edges = generate_graph(vertices_count, edges_probability)

    # Draw the graph
    draw_graph(vertices, edges)

    cliques_found = []

    vertices_queue = []
    visited_vertices = set()

    # Sort the vertices by their weight
    sorted_vertices = sorted(vertices, key=lambda v: v.weight, reverse=True)

    current_vertice_idx = None

    while True:

        # If we are in the beginning or back tracked to the first vertice
        if len(vertices_queue) == 0:

            # Get the first vertice - the vertice that is more likely to generate the maximum weight clique
            # I.e., the vertice with the higher weight that was not analysed yet.
            starting_vertice, current_vertice_idx = get_first_vertice(sorted_vertices, current_vertice_idx)
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
        max_weight_neighbor_vertice = get_max_common_neighbor(vertices_queue, edges)

        # If we found a vertice that is neighbor of all the others (is not None)
        # and we haven't visited it yet, let's check it
        if max_weight_neighbor_vertice is not None and max_weight_neighbor_vertice not in visited_vertices:

            # Let's append it to the vertices queue and add it to visited vertices, so we avoid loops
            vertices_queue.append(max_weight_neighbor_vertice)
            visited_vertices.add(max_weight_neighbor_vertice)

            # If the vertices in the queue form a Clique
            if utils.is_clique(vertices_queue, edges):
                # Create a Clique entity and add it to a list
                new_clique = Clique(vertices_queue.copy(), sum(map(lambda v: v.weight, vertices_queue)))
                cliques_found.append(new_clique)

        # If the current vertice does not have neighbors, do a backtracking
        else:
            # backtracked_vertice = vertices_queue[-1]
            # visited_vertices.remove(backtracked_vertice)
            vertices_queue.pop(-1)

    # Print the Clique with the highest Weight
    max_clique = max(cliques_found, key=lambda x: x.weight) if len(cliques_found) > 0 else None
    utils.print_results(max_clique)


def get_max_common_neighbor(vertices_list, edges) -> Vertice | None:

    neighbors_of_all_vertices = []

    for vertice in vertices_list:
        neighbors_of_all_vertices.append(utils.get_vertice_neighbors(vertice, edges))

    neighbors_of_all_vertices = list(reduce(set.intersection,
                                            [set(item) for item in neighbors_of_all_vertices]))

    # Remove all vertices already in the list - to not create a loop
    for vertice in vertices_list:
        if vertice in neighbors_of_all_vertices:
            neighbors_of_all_vertices.remove(vertice)

    if len(neighbors_of_all_vertices) > 0:
        return sorted(neighbors_of_all_vertices, key=lambda v: v.weight, reverse=True)[0]
    else:
        return None


def get_first_vertice(sorted_vertices, current_first_vertice):

    current_first_vertice = current_first_vertice + 1 if current_first_vertice is not None else 0

    if current_first_vertice < len(sorted_vertices):
        return sorted_vertices[current_first_vertice], current_first_vertice
    else:
        return None, current_first_vertice


if __name__ == "__main__":

    for vertices_amount in range(4, 100):
        for prob in [0.125, 0.25, 0.5, 0.75]:
            print()
            print(f"Calculating for {vertices_amount} vertices and {prob*100} probability of edges: ")
            print()
            calculate_max_weight_clique_with_heuristic(vertices_amount, prob)

    # calculate_max_weight_clique_with_heuristic(20, .75)

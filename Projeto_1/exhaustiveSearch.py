import utils
from domainClasses import Clique
from drawGraph import draw_graph
from generateGraph import generate_graph
from utils import powerset, is_clique, subset_weight_sum


def calculate_max_weight_clique_exhaustive(vertices_count=25, edges_probability=.75):

    # Generate Graph vertices and edges
    vertices, edges = generate_graph(vertices_count, edges_probability)

    # Draw the graph
    draw_graph(vertices, edges)

    # With Optimization
    vertices = optimize_vertices(vertices, edges)

    # Generate all Subsets of vertices
    all_vertices_subsets = list(powerset(vertices))

    all_cliques_found = []

    for vertice_subset in all_vertices_subsets:

        if is_clique(vertice_subset, edges):
            # print("Clique found in subset {0}".format(vertice_subset))
            new_clique = Clique(vertice_subset, sum(map(lambda v: v.weight, vertice_subset)))
            all_cliques_found.append(new_clique)

    max_weight_clique = max(all_cliques_found, key=lambda clique: clique.weight) if len(all_cliques_found) > 0 else None
    utils.print_results(max_weight_clique)


# Remove all the vertices disconnected before generating subsets.
# Disconnected vertices can be removed because they won't form cliques
def optimize_vertices(vertices_list, edges):

    vertices_amount_before_optimization = len(vertices_list)
    vertices_list = list(filter(lambda v: v.is_connected(edges), vertices_list))
    vertices_amount_after_optimization = len(vertices_list)

    print(f"Optimization removed {vertices_amount_before_optimization - vertices_amount_after_optimization} vertices.")

    return vertices_list


if __name__ == "__main__":

    for vertices_amount in range(4, 30):
        for prob in [0.125, 0.25, 0.5, 0.75]:
            print()
            print(f"Calculating for {vertices_amount} vertices and {prob*100} probability of edges: ")
            print()
            calculate_max_weight_clique_exhaustive(vertices_amount, prob)

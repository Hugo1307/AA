import pickle

from algorithms.backtrackingSearch import BacktrackingSearch
from algorithms.exhaustiveSearch import ExhaustiveSearch
from algorithms.greedySearch import GreedySearch

from graph.generateGraph import generate_graph

import time
import os


def main(output_mode=False):
    graphs = generate_all_graphs(400)
    run_simulation(graphs, output_mode, "Greedy")


def generate_all_graphs(max_vertices):
    if os.path.exists("graph/data/generated_graphs.pkl"):
        with open('graph/data/generated_graphs.pkl', 'rb') as f:
            return pickle.load(f)
    else:

        graphs = []

        print("Generating Graphs...")

        start = time.time()

        for vertices_count in range(5, max_vertices):
            for edges_probability in [0.125, 0.25, 0.5, 0.75]:
                graphs_gen_progress = vertices_count * 100 / max_vertices
                graphs.append((generate_graph(vertices_count, edges_probability), edges_probability,))
                print(f"Progress (%): {round(graphs_gen_progress, 2)}", end='\r')

        end = time.time()

        print(f"Generated {len(graphs)} graphs in {end - start} seconds")

        with open('graph/data/generated_graphs.pkl', 'wb') as f:
            pickle.dump(graphs, f)

        return graphs


def run_simulation(graphs, output_mode, algorithm_name):

    print(f"Max Weight Clique - {algorithm_name} Algorithm")
    print()

    # Erase file contents
    open(f"{algorithm_name}_results.txt", "w").close()

    output_file = open(f"{algorithm_name}_results.txt", "a")

    if not output_mode:
        print("Vertices\tEdges Prob.\tMax Weight\tSearch Time".expandtabs(30))
    else:
        output_file.write("Vertices\tEdges Prob.\tMax Weight\tSearch Time\n".expandtabs(30))

    # Get Results for Algorithm
    for graph in graphs:

        vertices, edges, edges_prob = graph[0][0], graph[0][1], graph[1]

        if algorithm_name == "Greedy":
            algorithm = GreedySearch(vertices, edges)
        elif algorithm_name == "Exhaustive":
            algorithm = ExhaustiveSearch(vertices, edges)
        elif algorithm_name == "Backtracking":
            algorithm = BacktrackingSearch(vertices, edges)
        else:
            raise NotImplemented()

        # algorithm.draw_graph()
        start_time_search = time.time()
        max_clique = algorithm.perform_search()
        end_time_search = time.time()

        search_delta_time = end_time_search - start_time_search

        if not output_mode:
            print(
                f"{len(vertices)}\t{edges_prob}\t{max_clique.weight}\t{search_delta_time}".expandtabs(
                    30))
        else:
            output_file.write(
                f"{len(vertices)}\t{edges_prob}\t{max_clique.weight}\t{search_delta_time}\n".expandtabs(
                    30))
            print(f"Progress (%): {round(len(vertices) * 100 / len(graphs), 2)}", end='\r')

    output_file.close()


if __name__ == "__main__":
    main(output_mode=False)

import sys
import pickle

from algorithms.monteCarloBlindSearch import MonteCarloBlindSearch
from algorithms.monteCarloProbSearch import MonteCarloProbSearch

from graph.generateGraph import generate_graph

import time
import os


def main(algorithm: str, file_as_output, graphs_slice: tuple):
    graphs = generate_all_graphs(200)
    run_simulation(graphs, file_as_output, algorithm, graphs_slice)


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


def run_simulation(graphs, output_mode, algorithm_name, slicing):

    print(f"Max Weight Clique - {algorithm_name} Algorithm")
    print()

    # Erase file contents
    if output_mode:
        open(f"results/{algorithm_name}_results.txt", "w").close()
    elif not os.path.exists("results/{algorithm_name}_results.txt"):
        open(f"results/{algorithm_name}_results.txt", "w").close()

    output_file = open(f"results/{algorithm_name}_results.txt", "a")

    if not output_mode:
        print("Vertices\tEdges_Prob.\tMax_Weight\tOps._Count\tTested_Solutions\tSearch_Time".expandtabs(30))
    else:
        output_file.write("Vertices\tEdges_Prob.\tMax_Weight\tOps._Count\tTested_Solutions\tSearch_Time\n".expandtabs(30))

    # Get Results for Algorithm
    graph_count = 0

    if slicing[0] == -1 or slicing[1] == -1:
        graphs_to_compute = graphs
    else:
        graphs_to_compute = graphs[slicing[0]:slicing[1]]

    for graph in graphs_to_compute:

        vertices, edges, edges_prob = graph[0][0], graph[0][1], graph[1]
        graph_count += 1

        if algorithm_name == "MonteCarloProb":
            algorithm = MonteCarloProbSearch(vertices, edges)
        elif algorithm_name == "MonteCarloBlind":
            algorithm = MonteCarloBlindSearch(vertices, edges)
        else:
            raise NotImplemented()

        # algorithm.draw_graph()
        start_time_search = time.time()
        max_clique, operations_count, tested_solutions = algorithm.perform_search()
        end_time_search = time.time()

        search_delta_time = end_time_search - start_time_search

        if not output_mode:
            print(
                f"{len(vertices)}\t{edges_prob}\t{max_clique.weight}\t{operations_count}\t{tested_solutions}\t{search_delta_time}"
                .expandtabs(30)
            )
        else:
            output_file.write(
                f"{len(vertices)}\t{edges_prob}\t{max_clique.weight}\t{operations_count}\t{tested_solutions}\t{search_delta_time}\n"
                .expandtabs(30)
            )
            print(f"Progress (%): {round(graph_count * 100 / len(graphs), 2)}", end='\r')

        if search_delta_time > 120:
            print("Stopped due to timeout...")
            break

    output_file.close()


def start_program():

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Arguments
    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # First Argument: Algorithm to be used
    # Second Argument: Output to file?
    # Third Argument: First element of graphs slice
    # Fourth Argument: Second element of graphs slice

    algorithm = sys.argv[1] if len(sys.argv) > 1 else "MonteCarloProb"
    output_to_file = sys.argv[2] == "True" if len(sys.argv) > 2 else False
    slicing = tuple([int(sys.argv[3]) if len(sys.argv) > 3 else -1, int(sys.argv[4]) if len(sys.argv) > 4 else -1])

    main(algorithm, output_to_file, slicing)


if __name__ == "__main__":
    start_program()

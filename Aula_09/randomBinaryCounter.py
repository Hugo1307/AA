from collections import Counter
import random

# Returns a list with the observed occurence for each experiment
def random_counter(count_limit, experiment_count):

    experiments = []

    for _ in range(0, experiment_count):

        counter = 0

        for _ in range (0, count_limit):
            prob_of_counting = random.randint(0,1)
            if prob_of_counting == 0:
                counter += 1

        experiments.append(counter)

    return experiments


def printResults(experimental_results, number_of_experiments, event_count):

    experimental_results_counted = dict(Counter(experimental_results))
    sorted_experimental_results_counted = dict(sorted(experimental_results_counted.items(), key=lambda item: item[1], reverse=True))
    
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print()

    print(f"Expected Value: {event_count/2}")
    print(f"Practical Value Obtained: {list(sorted_experimental_results_counted.keys())[0]}")
    print()
    print("Experiments: ")
    print()

    for key, value in sorted_experimental_results_counted.items():
        print(f" Value {key} has a probability of {round(value/number_of_experiments*100, 2)} % to happen.")
    
    print()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def main():

    experiments_count = 10000
    count_limit = 10

    printResults(random_counter(count_limit, experiments_count), experiments_count, count_limit)

main()
import random


def toss_coin(prob=0.5):
    
    rand_number = random.random()

    if rand_number <= prob:
        return 0
    else:
        return 1


print(toss_coin())


def toss_dice():
    return random.randint(1,6)


simulations = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
coin_toss_results = []

for i in range(0, len(simulations)):

    print("Running simulation for ", simulations[i])

    for i in range(0, simulations[i]): 
        coin_toss_results.append(toss_coin())

    print("  Zeros: ", coin_toss_results.count(0))
    print("  Ones: ", coin_toss_results.count(1))



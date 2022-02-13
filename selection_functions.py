import random
import numpy as np
from matplotlib.pyplot import switch_backend
from sympy import false, true

def fitness_proportional(population, fitness_values, no_of_selection, max_prob):
    sum_of_fitness = 0
    cumulative_fitness = 0
    fitness_values_cumulative = list()
    if max_prob == true:
        sum_of_fitness = sum(fitness_values)
        for i in range(len(population)):
            cumulative_fitness += (fitness_values[i] / sum_of_fitness)
            fitness_values_cumulative.append(cumulative_fitness)
    else:
        for fitness in fitness_values:
            sum_of_fitness += 1 / fitness
        for i in range(len(population)):
            cumulative_fitness += ((1 / fitness_values[i]) / sum_of_fitness)
            fitness_values_cumulative.append(cumulative_fitness)
    #* calculate best chromosome
    new_population = list()
    for i in range(no_of_selection):
        random_val = random.uniform(0,1)
        for j in range(len(fitness_values_cumulative)):
            if (random_val <= fitness_values_cumulative[j]):
                new_population.append(population[j])
                break
    return new_population

def rank_based(population, fitness_values, no_of_selection, max_prob):
    temp_fitness = list(fitness_values)
    total_fitness = 0
    ranks = np.zeros(len(temp_fitness), dtype=int).tolist()
    for i in range(len(temp_fitness)):
        val = max(temp_fitness) if max_prob == true else min(temp_fitness)
        ranks[temp_fitness.index(val)] = len(temp_fitness) - (i)
        total_fitness += (i + 1)
        temp_fitness[temp_fitness.index(val)] = -9999999999 if max_prob == true else 9999999999
    # fitness proportion based on ranks
    for i in range(len(temp_fitness)):
        ranks[i] = ranks[i] / total_fitness
    # cumulative
    for i in range(1, len(temp_fitness)):
        ranks[i] = ranks[i] + ranks[i-1]
    #* calculate best chromosome
    new_population = list()
    for i in range(no_of_selection):
        random_val = random.uniform(0,1)
        for j in range(len(ranks)):
            if (random_val <= ranks[j]):
                new_population.append(population[j])
                break
    # print(ranks)
    # print(new_population)
    return new_population

def binary_tournament(population, fitness_values, no_of_selection, max_prob):
    new_population = list()
    # print(temp)
    for i in range(no_of_selection):
        random_val_x = random.randint(0, len(population)-1)
        chromosome_x = population[random_val_x]
        random_val_y = random.randint(0, len(population)-1)
        chromosome_y = population[random_val_y]
        if fitness_values[random_val_x] > fitness_values[random_val_y]:
            if max_prob:
                new_population.append(chromosome_x)
            else:
                new_population.append(chromosome_y)
        else:
            if max_prob:
                new_population.append(chromosome_y)
            else:
                new_population.append(chromosome_x)
    return new_population
    # for i in range(no_of_selection):
    #     continue

def truncation(population, fitness_values, no_of_selection, max_prob):
    temp = fitness_values.copy()
    new_population = list()
    # print(len(fitness_values))
    # print(len(population))
    for i in range(no_of_selection):
        best_chromosome = max(temp) if max_prob == true else min(temp)

        new_population.append(population[temp.index(best_chromosome)])
        temp[temp.index(best_chromosome)] = -9999999999 if max_prob == true else 9999999999
    return new_population

def random_selection(population, fitness_values, no_of_selection, max_prob):
    new_population = list()
    temp = population.copy()
    # print(temp)
    for i in range(no_of_selection):
        random_val = random.randint(0, len(temp)-1)
        chromosome = temp[random_val]
        # temp.remove(chromosome)
        new_population.append(chromosome)
    return new_population

def termination():
    pass
# def selection_function(selection_func, total_size):


# population = ['a', 'b', 'c', 'd', 'e']
# fit = [10,15,20,30,25]
# print(rank_based(population, fit, 2, true))

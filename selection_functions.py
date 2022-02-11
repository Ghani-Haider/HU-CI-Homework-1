from ctypes import util
from hashlib import new
from random import randint

from matplotlib.pyplot import switch_backend
from sympy import false, true

def fitness_proportional():
    util.raiseNotDefined()

def rank_based():
    util.raiseNotDefined()

def binary_tournament():
    util.raiseNotDefined()

def truncation(population, fitness_values, population_size):
    temp = fitness_values
    new_population = list()
    # print(len(fitness_values))
    # print(len(population))
    for i in range(population_size):
        best_chromosome = max(temp)
        new_population.append(population[temp.index(best_chromosome)])
        temp[temp.index(best_chromosome)] = -999999
    return new_population

def random_selection(population, no_of_offspring, parent_selection = false):
    final_lst = list()
    temp = list(population)
    if parent_selection == true:
        # temp = population
        for i in range(no_of_offspring):
            parent_x = temp[randint(0, len(temp)-1)]
            temp.remove(parent_x)
            parent_y = temp[randint(0, len(temp)-1)]
            temp.remove(parent_y)
            final_lst.append([parent_x, parent_y])
    return final_lst

def termination():
    util.raisedNotDefined()

# def selection_function(selection_func, total_size):
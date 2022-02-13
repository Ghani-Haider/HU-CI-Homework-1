from ctypes import util
from math import trunc
import matplotlib.pyplot as plt
from EA_problem import *
from selection_functions import *
from knapsack import Knapsack
from graphcoloring import Graphcoloring
from tsp import tsp

population_size = 100
no_of_offspring = 80
no_of_generations = 100
mutation_rate = 0.3
no_of_iterations = 10

def evolutionaryAlgorithm(problem: Problem, max_prob=true): #TODO balance between randomness and deterministic (parent is usually stochastic, see lectures)
    generation_BSF = [0] * no_of_generations
    generation_ASF = [0] * no_of_generations
    
    # Step 1: Initialize the population randomly or with potentially good solutions
    #* list of chromosomes
    population = problem.populationInitialization(population_size)
    
    # Step 7: Go to Step 2 until the termination criteria are met
    for j in range(no_of_iterations):
        for i in range(no_of_generations):

            # Step 2: Compute the fitness of each individual in the population
            #* list of fitness values corresponding to population
            fitness_values = problem.fitnessFunction(population)
            # calculating sum of avg. and best fitness so far for each generation
            generation_BSF[i] = generation_BSF[i] + max(fitness_values)
            generation_ASF[i] = generation_ASF[i] + sum(fitness_values)/len(fitness_values)

            # Step 3: Select parents using a selection procedure
            #* double times the no_of_offsprings
            parent_list = random_selection(population, fitness_values, 2*no_of_offspring, true)

            # Step 4: Create offspring by crossover and mutation operators
            offspring_list = []
            for i in range(no_of_offspring-1):
                # corssover
                offspring = problem.crossOver(parent_list[i],
                            parent_list[i+1])
                # mutation
                offspring = problem.mutation(offspring, mutation_rate)
                offspring_list.append(offspring)

            # Step 5 Compute the fitness of the new offspring
            #TODO suggestion is to save offspring in the same population list, just calculate the fitness values before adding it to population
            offspring_fitness_val = problem.fitnessFunction(offspring_list)
            
            population = population + offspring_list
            fitness_values = fitness_values + offspring_fitness_val
            
            # Step 6  Select members of population to die using a
            # selection procedure.
            survivor = truncation(population, fitness_values, population_size, max_prob)
            population = survivor
    
    # calculating and plotting average best so far and average average fitnesss of each generation
    avg_generation_BSF = [x/no_of_iterations for x in generation_BSF]
    avg_generation_ASF = [x/no_of_iterations for x in generation_ASF]
    plt.plot(range(no_of_generations), avg_generation_BSF)
    plt.plot(range(no_of_generations), avg_generation_ASF)
    plt.legend(["BSF", "ASF"])
    plt.title("Test")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.show()
    return population

prob = Knapsack("f2_l-d_kp_20_878")
# prob = Graphcoloring("gcol7.txt")
# prob = tsp("qa194.tsp")
sol = evolutionaryAlgorithm(prob, true)
print(prob.fitnessFunction(sol))
# print(sol)
# print(prob._max_colors)
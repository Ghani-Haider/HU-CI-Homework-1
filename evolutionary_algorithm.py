from ctypes import util
from EA_problem import *
from selection_functions import *

population_size = 30
no_of_offspring = 10
no_of_generations = 100
mutation_rate = 0.5
no_of_iterations = 10

def evolutionaryAlgorithm(problem: Problem, parent_selection,
survival_selection): #TODO balance between randomness and deterministic (parent is usually stochastic, see lectures)
    # Step 1: Initialize the population randomly or
    # with potentially good solutions
    init_population = problem.populationInitialization(population_size)

    # Step 7: Go to Step 2 until the termination criteria are met.
    while (termination(init_population) == False):

        # Step 2: Compute the fitness of each individual in
        # the population
        #! use yield on chromosomes and save fitness inside problem
        # fitness_values = []
        # for chromosome in init_population:
        #     fitness_values.append((chromosome,
        #     problem.fitnessFunction(chromosome)))
        fitness_values = problem.fitnessFunction()

        # Step 3: Select parents using a selection procedure
        #! return val should be list
        #! parent should also be saved inside the problem
        parent_list = []
        for i in range(no_of_offspring):
            #! parent selection to deal with selection function
            parent = parent_selection #? individual or pair returned?
            parent_list.append(parent)

        # Step 4: Create offspring by crossover and mutation
        # operators
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
        offspring_fitness_val = []
        for i in range(no_of_offspring):
            offspring_fitness_val.append((offspring_list[i],
            problem.fitnessFunction(offspring_list[i])))
        
        # Step 6  Select members of population to die using a
        # selection procedure.
        survivor = survival_selection
        init_population = survivor

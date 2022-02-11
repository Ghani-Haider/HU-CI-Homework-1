from ctypes import util
from EA_problem import *
from selection_functions import *
from knapsack import Knapsack

population_size = 30
no_of_offspring = 10
no_of_generations = 100
mutation_rate = 0.5
no_of_iterations = 10

def evolutionaryAlgorithm(problem: Problem, parent_selection,
survival_selection): #TODO balance between randomness and deterministic (parent is usually stochastic, see lectures)
    # Step 1: Initialize the population randomly or
    # with potentially good solutions
    #* list of chromosomes
    population = problem.populationInitialization(population_size)
    

    # Step 7: Go to Step 2 until the termination criteria are met.
    #! can also give generation
    # while (termination(population) == False):
    for i in range(no_of_generations):

        # Step 2: Compute the fitness of each individual in
        # the population
        #! use yield on chromosomes and save fitness inside problem
        # fitness_values = []
        # for chromosome in init_population:
        #     fitness_values.append((chromosome,
        #     problem.fitnessFunction(chromosome)))
        #* list of fitness values corresponding to population
        fitness_values = problem.fitnessFunction(population)

        # Step 3: Select parents using a selection procedure
        #! return val should be list
        #! parent should also be saved inside the problem
        
        parent_list = random_selection(population, no_of_offspring, true)
        
        # for i in range(no_of_offspring):
        #     #! parent selection to deal with selection function
        #     parent = parent_selection #? individual or pair returned?
        #     parent_list.append(parent)

        # Step 4: Create offspring by crossover and mutation
        # operators
        offspring_list = []
        for i in range(no_of_offspring):
            # corssover
            offspring = problem.crossOver(parent_list[i][0],
                        parent_list[i][1])
            # mutation
            offspring = problem.mutation(offspring, mutation_rate)
            offspring_list.append(offspring)

        # Step 5 Compute the fitness of the new offspring
        #TODO suggestion is to save offspring in the same population list, just calculate the fitness values before adding it to population
        offspring_fitness_val = problem.fitnessFunction(offspring_list)
        # add offsprings to population
        # print('fit_val', len(fitness_values))
        
        population = population + offspring_list
        fitness_values = fitness_values + offspring_fitness_val
        # print(len(fitness_values))
        # print(len(population))

        # for i in range(no_of_offspring):
        #     offspring_fitness_val.append((offspring_list[i],
        #     problem.fitnessFunction(offspring_list[i])))
        
        # Step 6  Select members of population to die using a
        # selection procedure.
        survivor = truncation(population, fitness_values, population_size)
        population = survivor
    return population

prob = Knapsack("f2_l-d_kp_20_878")
sol = evolutionaryAlgorithm(prob, 'a', 'b')
print(prob.fitnessFunction(sol))
print(sol)

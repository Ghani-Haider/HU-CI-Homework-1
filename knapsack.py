from random import randint, uniform
import numpy as np
from EA_problem import Problem

population_size = 30
no_of_offspring = 10
no_of_generations = 100
mutation_rate = 0.5
no_of_iterations = 10

class Knapsack(Problem):
    def __init__(self, path):
        #* dataset is: profit, weight
        #* keep adding in the chromosome until weight hits 878
        self._data = list()
        self._population = list()

        file = open(path, "r")
        # for max items and knapsack capacity
        parameters = file.readline().strip().split()
        self._max_items = int(parameters[0])
        self._max_capacity = int(parameters[1])
        
        for line in file:
            val = line.strip().split(' ')
            self._data.append((int(val[0]), int(val[1])))
        
        # print(self.data)

    
    def populationInitialization(self, pop_size):
        self._population = np.random.randint(2, size = (pop_size, self._max_items))
        self._population = self._population.astype(int)
        # print(self._population)

    def fitnessFunction(self):
        # fitness value is the sum of profits, and zero if items in a chromosome outweight max knapsack weight
        self._fitness = np.empty(self._population.shape[0])
        for i in range(self._population.shape[0]):
            # print("pop[i]", self._population[i])
            total_profit = 0
            total_weight = 0
            for j in range(self._max_items):
                total_profit += self._population[i][j] * self._data[j][0]
                total_weight += self._population[i][j] * self._data[j][1]
                # print(self._data[j], total_profit, total_weight)
            if total_weight <= self._max_capacity:
                self._fitness[i] = total_profit
            else:
                # not a valid solution
                self._fitness[i] = 0 
        self._fitness = self._fitness.astype(int)
        # print(len(self._fitness))
        return self._fitness
    
    def crossOver(self, parentA, parentB):
        offspring = parentA[:len(parentA)//2] + parentB[len(parentB)//2:]
        # print(len(offspring))
        # print(offspring)
        return offspring
    
    def mutation(self, chromosome, mutation_rate):
        if uniform(0, 1) > mutation_rate:
            return chromosome
        else:
            random_pos = randint(0, len(chromosome)-1)
            if chromosome[random_pos] == 0:
                chromosome[random_pos] = 1
            else:
                chromosome[random_pos] = 0
        # print(chromosome)
        # print(random_pos)
        return chromosome  


prob = Knapsack("f2_l-d_kp_20_878")
prob.populationInitialization(population_size)
prob.fitnessFunction()
parenta = [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1]
parentb = [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

prob.crossOver(parenta, parentb)
print(parenta)
prob.mutation(parenta, 1)
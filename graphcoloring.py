from ast import literal_eval
from multiprocessing import parent_process
import random
import numpy as np
from sympy import are_similar
from EA_problem import Problem

population_size = 30
no_of_offspring = 10
no_of_generations = 100
mutation_rate = 0.5
no_of_iterations = 10

class Graphcoloring(Problem):
    def __init__(self, path):
        self._data = list()

        file = open(path, "r")
        #* for number of vertices and edges
        parameters = file.readline().strip().split()
        self._total_vertices = int(parameters[2])
        self._total_edges = int(parameters[3])
        # print(self._total_vertices)
        # print(self._total_edges)
        
        #* adjacency matrix representation of the graph
        self._graph = np.zeros((self._total_vertices, self._total_vertices), dtype=int).tolist()
        # print(len(self._graph))
        for line in file:
            val = line.strip().split()
            vertex_1 = int(val[1])
            vertex_2 = int(val[2])
            self._graph[vertex_1 - 1][vertex_2 - 1] = self._graph[vertex_2 - 1][vertex_1 - 1] = 1

        # print(np.array(self._graph))
        
        #* calculating max color needed for given vertices
        #* max colors should be vertex with max degree + 1
        self._max_colors = 1
        for i in range(self._total_vertices):
            degree_vertex = sum(self._graph[i])
            if(degree_vertex > self._max_colors):
                self._max_colors = degree_vertex + 1
        # print(self._max_colors)
    
    def populationInitialization(self, pop_size):
        population = np.random.randint(1, self._max_colors+1, size = (pop_size, self._total_vertices))
        population = population.tolist()
        # print(len(population))
        # print(len(population[0]))
        return population
    
    def fitnessFunction(self, population: list):
        fitness = np.zeros(len(population), dtype=int).tolist()
        # print(fitness)
        for i in range(len(population)):
            for j in range(self._total_vertices):
                for k in range(j, self._total_vertices):
                    if(population[i][j] == population[i][k] and self._graph[j][k] == 1):
                        fitness[i] = fitness[i] + 1
        # print(fitness)
        return fitness

    def crossOver(self, parentA, parentB):
        crossover_point = random.randint(2, self._total_vertices - 2)
        offspring = list()
        for i in range(crossover_point + 1):
            offspring.append(parentA[i])
        for i in range(crossover_point + 1, self._total_vertices):
            offspring.append(parentB[i])
        return offspring
    
    def mutation(self, chromosome, mutation_rate):
        if random.uniform(0, 1) < mutation_rate:
            random_pos = random.randint(0, len(chromosome) - 1)
            chromosome[random_pos] = random.randint(1, self._max_colors)
        return chromosome
    
# prob = Graphcoloring("gcol1.txt")
# pop = prob.populationInitialization(30)
# prob.fitnessFunction(pop)

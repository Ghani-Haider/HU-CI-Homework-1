from turtle import end_fill
from soupsieve import select
import tsplib95
from random import randint, uniform
#from myapp import get_distance
from EA_problem import Problem

population_size = 30
no_of_offspring = 10
no_of_generations = 100
mutation_rate = 0.5
no_of_iterations = 10

# problem.get_edges() #get edges
# problem.get_nodes() #get nodes
# problem.node_coords[3] #get coords
# print(list(problem.get_edges())) #get edges
# problem.get_graph() get graph
# problem.get_display(3) get coords

'''
edge = 3, 8
weight = problem.get_weight(*edge)
print(f'The driving distance from node {edge[0]} to node {edge[1]} is {weight}.')

G=problem.get_graph()
print(G.graph)
'''

# print(list(problem.get_nodes()))


class tsp(Problem):
    def __init__(self, path):
        # * dataset is: start, end, weight

        self.tspdata = tsplib95.load(path)

        '''
        self.data = list()
        for start in list(self.tspdata.get_nodes()):
            for end in list(self.tspdata.get_nodes()):
                if start != end:
                    edge = start, end
                    self.data.append(
                        (start, end, self.tspdata.get_weight(*edge)))
        '''

        self.no_of_nodes = len(list(self.tspdata.get_nodes()))

        # print(self.no_of_nodes)
        # print(self.data)

    def populationInitialization(self, pop_size):
        init_pop = 0

        population = list()

        while init_pop != pop_size:
            node = randint(1, self.no_of_nodes)
            path = list()
            while len(path) != self.no_of_nodes:
                #print(len(path))
                # print(path)
                node = randint(1, self.no_of_nodes)
                # print(node)
                if node not in path:
                    path.append(node)

            #print(path)
            population.append(path)
            init_pop += 1

        return population

    def fitnessFunction(self, population):
        # fitness is the cummulative distance travelled
        fitness = [None] * len(population)
        for i in range(len(population)):
            total_weight = 0

            #weight of one path
            path=population[i]
            for j in range(1, len(path)):
                start = path[j-1]
                end = path[j]
                edge = start, end                       
                total_weight += self.tspdata.get_weight(*edge)
            fitness[i] = total_weight

        return fitness

    def crossOver(self, parentA, parentB):
        offspring=[None] * len(parentA)     #dummy list for offspring

        #select half of parentA to be carried forward
        start=randint(1,(len(parentA)//2)-2)    
        end=start+(len(parentA)//2)        
        offspring[start:end] = parentA[start:end]
        #print(offspring)

        #update the rest of offspring via parentB
        parentb_idx=end
        offspring_idx=end
        while None in offspring:
            if parentB[parentb_idx] not in offspring:
                offspring[offspring_idx]=parentB[parentb_idx]
                offspring_idx=(offspring_idx+1)%(len(parentB))
            parentb_idx=(parentb_idx+1)%(len(parentB))
            #print((parentb_idx,offspring_idx))
            #print(offspring)

        return offspring

    def mutation(self, chromosome, mutation_rate):
        #if mutation occurs then swap too genes
        if uniform(0, 1) < mutation_rate:
            while True:
                pos1 = randint(1, len(chromosome)-2)
                pos2 = randint(1, len(chromosome)-2)
                if pos1!=pos2:
                    chromosome[pos1], chromosome[pos2] = chromosome[pos2], chromosome[pos1]
                    break
        
        #print(chromosome)
        return chromosome

    #def survivorSelection(self, chromosome):



# prob = tsp('qa194.tsp')
# pop=prob.populationInitialization(population_size)
#print(pop)
#print(prob.fitnessFunction(pop))

#parenta=[1,2,3,4,5,6,7,8,9,10]
#parentb=[5,10,9,3,4,7,8,2,1,6]

#print(prob.crossOver(parenta, parentb))
#print(parenta)
#print(prob.mutation(parenta, 0.5))

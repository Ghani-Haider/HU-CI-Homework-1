from ctypes import util

class Problem:
    def __init__():
        util.raiseNotDefined()

    def populationInitialization(self, pop_size):
        """
            data: any csv file containing population information.
        
        Initialize the population randomly or with potentially good solutions.
        """
        util.raiseNotDefined()

    def fitnessFunction(self, population: list):
        """
            chromosome: An individual in the population

        Returns fitness value of the chromosome.
        """
        util.raiseNotDefined()

    def crossOver(self, parentA, parentB):
        """
            parentA: Parent chromosome
            parentB: Parent chromosome

        For given parents, this should return a new offspring based on infomration 
        sharing between parent according to some criteria.
        """
        util.raiseNotDefined()

    def mutation(self, chromosome, mutation_rate):
        """
            chromosome: An individual in the population

        Unitary operation that allows random change in offspring and return mutated offsrping.
        """
        util.raiseNotDefined()
    
    def survivorSelection(self, chromosome):
        """
            chromosome: An individual in the population

        Returns chromosomes with hight fitness values.
        """
        util.raiseNotDefined()
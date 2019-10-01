import random
import time

class DNA():
    """docstring for DNA"""

    def __init__(self, size, target):
        self.size = size
        self.value = []
        self.target = target
        self.fit = -1

    def seed(self):
        value = []
        for i in range(self.size):
            value.append(chr(random.randint(65, 123)))
        self.value = value

    def fitness(self):
        score = 0
        for i in range(self.size):
            if self.value[i] == self.target[i]:
                score += 1
        fitness = (score * 100) // self.size
        self.fit = fitness
        return self.fit

    def asString(self):
        return ' '.join(map(str, self.value))


class Population():
    """docstring for Population"""

    def __init__(self, PopSize, DNASize, target):
        self.size = PopSize
        self.DNASize = DNASize
        self.target = target
        self.value = self.create()

    def create(self):
        pop = []
        for i in range(self.size):
            dna = DNA(self.DNASize, self.target)
            dna.seed()
            pop.append(dna)
        return pop


def createPop(popsize, DNAsize, target):
    population = Population(popsize, DNAsize, target)
    return population


def calcFitness(population):
    for dna in population.value:
        dna.fitness()


def reproduce(population, target):
	mating_pool = []
	for dna in population.value:
		for i in range(dna.fit):
			mating_pool.append(dna)

	for i in range(population.size):
		A = random.randint(0, len(mating_pool) - 1)
		B = random.randint(0, len(mating_pool) - 1)
		parentA = mating_pool[A]
		parentB = mating_pool[B]

		while parentA.value == parentB.value:
			B = random.randint(0, len(mating_pool) - 1)
			parentB = mating_pool[B]

		mid = random.randint(0, len(mating_pool) - 1)
		child = DNA(parentA.size, parentA.target)
		child.value = parentA.value[:mid] + parentB.value[mid:]
		child = mutate(child)
		population.value[i] = child
	return population


def mutate(child):
	if random.random() <= 0.1:
		child.value[random.randint(0, child.size - 1)] = chr(random.randint(65, 123))
	return child


# def kill(pop, killMany):
#    newlist = sorted(pop.value, key=lambda x: x.fit)
#    for i in range(killMany):
#       pop.value.remove(newlist[i])
#    return pop


def main():
	target = "Do_not_call_me"
	targLen = len(target)
	popSize = 200
	mutation = 0.1
	population = createPop(popSize, targLen, target)
	gen = 1
	while(1):
		calcFitness(population)
		population = reproduce(population, target)
		calcFitness(population)
		# kill(population, len(children))
		for dna in population.value:
			print(dna.asString())
			if dna.fit == 100:
				print("Done")
				exit()
		gen += 1


if __name__ == '__main__':
	main()
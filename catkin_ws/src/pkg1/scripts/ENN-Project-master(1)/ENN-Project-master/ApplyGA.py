import random
import numpy
from numpy.matlib import rand


def sub2ind(array_shape, rows, cols):
    ind = rows * array_shape[1] + cols
    ind[ind < 0] = -1
    ind[ind >= array_shape[0] * array_shape[1]] = -1
    return ind


def ApplyGA(GA, Chromosomes, Chromosomes_Fitness):  # Because number of chromosomes are not nessesarly GA.populationSize
    smallerPopulationSize = len(Chromosomes_Fitness)  # Should be even number !

    # Selection
    if (GA.selection_option == 0):  # Tournament
        T = rand(smallerPopulationSize, GA.tournament_size) * (
                    smallerPopulationSize - 1) + 1  # Tournaments(Random from 1 to smallerPopulationSize)
        T = numpy.matrix(T).tolist()
        x = []
        for k in range(len(T)):
            l = []
            for i in range(len(T[k])):
                T[k][i] = round(T[k][i])% len(Chromosomes_Fitness)
                l.append(Chromosomes_Fitness[T[k][i]])
            x.append(l)
        tmp = (numpy.array(x)).max(1)
        tmp = tmp.tolist()
        idx = []
        for i in range(len(tmp)):
            idx.append(x[i].index(tmp[i]))
        # Index to determine the winners
        WinnersIdx = []  # Winners Indeces
        for i in range(len(idx)):
            WinnersIdx.append(T[i][idx[i]])
    elif (GA.selection_option == 1):  # Truncation
        tmp = Chromosomes_Fitness.copy()
        V = numpy.argsort(tmp, kind='mergesort', axis=0).tolist()[::-1]
        nbrOfSelections = round(smallerPopulationSize * GA.truncation_percentage / 100)  # Number of selected chromosomes
        V = V[0:nbrOfSelections]  # Winners Pool
        x = rand(smallerPopulationSize, 1)
        x = x.tolist()
        WinnersIdx = []
        for i in range(len(x)):
            WinnersIdx.append(V[((round(x[i][0]) * (nbrOfSelections - 1)) + 1)%len(V)])  # Winners Indeces

    # Crossover
    all_parents = []
    for i in range(len(WinnersIdx)):
        all_parents.append(Chromosomes[WinnersIdx[i]])
    x = rand(int(smallerPopulationSize / 2), 1)
    x = x.tolist()
    first_parents = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = round(x[i][j] * (smallerPopulationSize - 1) + 1) % len(x[i])
            first_parents.append(all_parents[x[i][j]])  # Random smallerPopulationSize / 2 Parents
    x = rand(int(smallerPopulationSize / 2), 1)
    x = x.tolist()
    second_parents = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = round(x[i][j] * (smallerPopulationSize - 1) + 1) % len(x[i])
            second_parents.append(all_parents[x[i][j]])  # Random smallerPopulationSize / 2 Parents
    references_matrix = []
    for j in range(int(smallerPopulationSize / 2)):
        l = []
        for i in range(GA.chromosomeLength):
            l.append(0)
        references_matrix.append(l)
    for j in range(int(smallerPopulationSize / 2)):
        for i in range(GA.chromosomeLength):
            references_matrix[j][
                i] = i  # = numpy.ones(smallerPopulationSize / 2, 1) [1:GA.chromosomeLength] # The Reference Matrix
    randNums = []
    x = rand(int(smallerPopulationSize / 2), 1).tolist()
    for i in range(len(x)):
        for j in range(len(x[i])):
            randNums.append((GA.corssoverProb_stdDev_percent * GA.chromosomeLength / 100) * round(
                x[i][j]) + GA.corssoverProb_mean_percent * GA.chromosomeLength / 100)
    # randNums = min(round(randNums), GA.chromosomeLength) # Truncation
    # randNums = max(randNums, 1) # Truncation: Vector of smallerPopulationSize / 2  length  of random numbers in range of 1: GA.chromosomeLength
    idx = []
    for i in range(len(randNums)):  # Binary matrix of selected genes for each parents couple
        l = []
        for j in range(GA.chromosomeLength):
            r = 1 * round(randNums[i])
            if (r > references_matrix[i][j]):
                l.append(1)
            else:
                l.append(0)
        idx.append(l)

    Chromosomes_Childs1 = []
    Chromosomes_Childs2 = []
    for i in range(len(first_parents)):
        l = []
        l2 = []
        for j in range(GA.chromosomeLength):
            l.append(0)
            l2.append(0)
        Chromosomes_Childs1.append(l)
        Chromosomes_Childs2.append(l2)
    # Do actual corssover
    for i in range(len(Chromosomes_Childs1)):
        for j in range(len(Chromosomes_Childs1[i])):
            if (idx[i][j] == 1):
                Chromosomes_Childs1[i][j] = first_parents[i][j]
                Chromosomes_Childs2[i][j] = second_parents[i][j]
            else:
                Chromosomes_Childs1[i][j] = second_parents[i][j]
                Chromosomes_Childs2[i][j] = first_parents[i][j]

    Chromosomes_Childs = []
    for i in range(len(Chromosomes_Childs1)):
        Chromosomes_Childs.append(Chromosomes_Childs1[i])
    for i in range(len(Chromosomes_Childs2)):
        Chromosomes_Childs.append(Chromosomes_Childs2[i])

    # Mutation
    idx = rand(smallerPopulationSize, GA.chromosomeLength)
    idx = idx.tolist()
    for i in range(len(idx)):  # Indeces for mutations
        for j in range(len(idx[i])):
            if (idx[i][j] <= GA.mutationProb):
                idx[i][j] = 1
            else:
                idx[i][j] = 0
    x = rand(len(idx) * len(idx[0]))
    x = x[0].tolist()
    mutedValues = []
    for i in range(len(x[0])):
        mutedValues.append(GA.weightsRange * (2 * x[0][i] - 1))

    c = 0
    for i in range(len(Chromosomes_Childs)):
        for j in range(len(Chromosomes_Childs[i])):
            if (idx[i][j] == 1):
                Chromosomes_Childs[i][j] = mutedValues[c]  # Do actual mutation
                c += 1

    return Chromosomes_Childs

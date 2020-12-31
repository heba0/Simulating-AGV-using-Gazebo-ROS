import numpy


def Feedforward(Sample, Chromosome, Network_Arch, unipolarBipolarSelector):
    # Feed Forward
    print("sample", Sample)
    activations = []
    for i in range(len(Sample)):
        activations.append(Sample[i])  # Adding Bias Node
    activations.append(1)
    print("activations", activations)
    startId = 0
    v = 3
    for Layer in range(1, len(Network_Arch)):
        d1 = len(activations)
        d2 = Network_Arch[Layer]
        weights = Chromosome[startId: startId + d1 * d2]
        print("w",len(weights))
        weights2 = []
        idx = 0
        for i in range(int(len(weights) / v)):
            l = []
            for j in range(idx, v + idx):
                l.append(weights[j])
            weights2.append(l)
            idx += v
        activations2 = []
        print("w2",len(weights2))
        for j in range(v):
            x = 0
            for k in range(len(activations)):
                x = x + activations[k] * weights2[k][j]
            activations2.append(x)

        activations = activations2
        if (unipolarBipolarSelector == 0):
            for i in range(len(activations)):
                activations[i] = 1. / (1 + numpy.exp(-activations[i]))
        else:
            for i in range(len(activations)):
                activations[i] = -1 + 2. / (1 + numpy.exp(-activations[i]))
        if (Layer != len(Network_Arch)-1):  # Adding Bias
            activations.append(1)  # Adding Bias Node
        startId = d1 * d2
        v -= 1

    outputs = activations

    return outputs

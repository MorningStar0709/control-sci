# The Boltzmann Machine

The Boltzmann Machine may be viewed as a generalization of a perceptron. It was designed to be a highly simplified model of a neural network. The machine consists of a collection of elements whose outputs are zero or one. The elements are linked by connections having different weights. The output of an element is determined by the outputs of the connecting elements and the weights of the interconnections. The firing is randomized in such a way that the probability of firing increases with the weighted sum of the inputs to an element. Some elements are connected to inputs and others to outputs, and there are also internal nodes. The connections in a Boltzmann Machine are assumed to be symmetric, which is a significant restriction.

In the perceptron there is a direct coupling between the inputs and the output. The Boltzmann Machine is much more complicated, because it can also have internal nodes. This implies that Hebb's principle cannot be applied directly. An extension called back-propagation has been suggested in Rumelhart and McClelland (1986).

There are many variations of neural networks. Dynamics can be introduced in the nodes. Hopfield observed that the weights could be chosen so that the network would solve specific optimization problems (Hopfield and Tank, 1986).

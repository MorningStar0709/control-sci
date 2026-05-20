# 6.3.1 What is state-space?

Recall from last chapter that 2D space has two axes: x and y. We represent locations within this space as a pair of numbers packaged in a vector, and each coordinate is a measure of how far to move along the corresponding axis. State-space is a Cartesian coordinate system with an axis for each state variable, and we represent locations within it the same way we do for 2D space: with a list of numbers in a vector. Each element in the vector corresponds to a state of the system.

In state-space notation, there are also input and output vectors with corresponding input and output spaces. Inputs drive the system to other points in the state-space, and outputs are sensor measurements that have a linear relationship to the state and input. Since the mapping from state and input to change in state is a system of equations, it’s natural to write it in matrix form.

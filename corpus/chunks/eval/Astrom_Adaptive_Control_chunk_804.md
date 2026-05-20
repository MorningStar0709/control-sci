# The Perceptron

In a system such as Michie's Boxes the control law is a logic function that gives the control action as a function of sensor patterns. The function is adaptive in the sense that it will adjust itself automatically. The perceptron proposed by Rosenblatt (1962) is one way to obtain a learning function. To describe the perceptron, let $u_{i}, i = 1, 2, \ldots, n$ , be inputs, and let $y_{i}, i = 1, 2, \ldots, n$ , be outputs. In the perceptron the output is formed as

$$y _ {i} (t) = f \left(\sum_ {j = 1} ^ {n} w _ {i j} (t) u _ {j} (t) - b\right) \quad i = 1, 2, \dots , m \tag {13.5}$$

where $w_{ij}$ are weights, $b$ is a bias, and $f$ is a threshold function, for example,

$$
f (x) = \left\{ \begin{array}{l l} 1 & \text { if } x \geq 0 \\ 0 & \text { if } x <   0 \end{array} \right.
$$

To update the weights, the perceptron uses a very simple idea, which is called Hebb's principle: Apply a given pattern to the inputs and clamp the outputs to the desired response, then increase the weights between nodes that are simultaneously excited.

This principle was formulated in Hebb (1949), in an attempt to model neuron networks. Mathematically it can be expressed as follows:

$$w _ {i j} (t + 1) = w _ {i j} (t) + \gamma u _ {i} (t) \left(y _ {j} ^ {0} (t) - y _ {j} (t)\right) \tag {13.6}$$

where $y_{j}^{0}$ is the desired response and $y_{j}$ is the response predicted by the model Eq. (13.5). By regarding the weights as parameters, it becomes clear that the updating formula of Eq. (13.6) is identical to a gradient method for parameter estimation.

Widrow and Hoff (1960) developed special-purpose hardware, called the Adaline, to implement perceptronlike devices. The learning algorithm used by Widrow was based on a simple gradient algorithm like Eq. (13.6). In devices like the perceptron and the Adaline, learning is interpreted as adjusting the coefficients in a network. From this point of view it can equally well be claimed that an adaptive system like the MRAS or the STR is learning. The mechanisms for determining the parameters are also similar.

A drawback of the perceptron is that it can recognize only patterns that can be separated linearly. It fell into disfavor because of exaggerated claims that could not be justified. It was heavily criticized in a book by Minsky and Papert (1969). The idea of designing learning networks did, however, persist.

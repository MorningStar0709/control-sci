# Selection of Model Structure

The model structures are derived from prior knowledge of the process and the disturbances. In some cases the only a priori knowledge is that the process can be described as a linear system in a particular operating range. It is then natural to use general representations of linear systems. Such representations are called black-box models. A typical example is the difference-equation model

$$A (q) y (k) = B (q) u (k) + C (q) e (k) \tag {13.1}$$

where u is the input, y is the output, and e is a white-noise disturbance. The parameters, as well as the order of the models, are considered as the unknown parameters.

Sometimes it is possible to apply physical laws to derive models of the process that contain only a few unknown parameters. The model may then be of the form

$$
\begin{array}{l} \frac {d x}{d t} = f (x, u, v, \theta) \\ y = g (x, u, e, \theta) \\ \end{array}
$$

where $\theta$ is a vector of unknown parameters, $x$ is the state of the system, and $v$ and $e$ are disturbances.

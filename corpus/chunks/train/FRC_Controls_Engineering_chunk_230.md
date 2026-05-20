# Linearization around θ = 0

To apply our tools for linear control theory, the model must be a linear combination of the states and inputs (addition and multiplication by constants). Since this model is nonlinear on account of the sine function, we should linearize it.

Linearization finds a tangent line to the nonlinear dynamics at a desired point in the statespace. The Taylor series is a way to approximate arbitrary functions with polynomials, so we can use it for linearization.

The taylor series expansion for sin θ around θ = 0 is $\theta - { \textstyle \frac { 1 } { 6 } } \theta ^ { 3 } + { \textstyle \frac { 1 } { 1 2 0 } } \theta ^ { 5 } - . . .$ . We’ll take just the first-order term θ to obtain a linear function.

$$
\begin{array}{l} \dot {\theta} = \omega \\ \dot {\omega} = - \frac {g}{l} \theta \\ \end{array}
$$

Now write the model in state-space representation. We’ll write out the system of equations with the zeroed variables included to assist with this.

$$
\begin{array}{l} \dot {\theta} = 0 \theta + 1 \omega \\ \dot {\omega} = - \frac {g}{l} \theta + 0 \omega \\ \end{array}
$$

Factor out θ and ω into a column vector.

$$
\left[ \begin{array}{l} \dot {\theta} \\ \omega \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \\ - \frac {g}{l} & 0 \end{array} \right] \left[ \begin{array}{l} \theta \\ \omega \end{array} \right] \tag {8.5}
$$

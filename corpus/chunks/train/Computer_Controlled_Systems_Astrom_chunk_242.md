# Example 4.7 Double integrator

For the double integrator we have

$$
\Phi = \left( \begin{array}{c c} 1 & h \\ 0 & 1 \end{array} \right) \quad \Gamma = \binom {h ^ {2} / 2} {h} \quad C = \left( \begin{array}{c c} 1 & 0 \end{array} \right)
$$

Hence

$$
\begin{array}{l} y (k) = x _ {1} (k) \\ y (k) = x _ {1} (k - 1) + h x _ {2} (k - 1) + \frac {h ^ {2}}{2} u (k - 1) \\ = y (k - 1) + h \left(x _ {2} (k) - h u (k)\right) + \frac {h ^ {2}}{2} u (k - 1) \\ \end{array}
$$

Solving these equations with respect to $x_{1}$ and $x_{2}$ we get

$$
\begin{array}{l} x _ {1} (k) = y (k) \\ x _ {2} (k) = \frac {y (k) - y (k - 1)}{h} + \frac {h}{2} u (k - 1) \\ \end{array}
$$

The first component $x_{1}$ is equal to the measured value and the second component $x_{2}$ is obtained by taking differences of the output and adding a fraction of the control signal.

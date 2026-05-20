# Example 2.3 Motor

A simple normalized model of an electrical DC motor (see Example A.2 in Appendix A) is given by

$$
\frac {d x}{d t} = \left( \begin{array}{c c} - 1 & 0 \\ 1 & 0 \end{array} \right) x + \binom{1}{0} u

y = \left( \begin{array}{c c} 0 & 1 \end{array} \right) x
$$

The Laplace transform method gives

$$
(s I - A) ^ {- 1} = \left( \begin{array}{c c} s + 1 & 0 \\ - 1 & s \end{array} \right) ^ {- 1} = \frac {1}{s (s + 1)} \left( \begin{array}{c c} s & 0 \\ 1 & s + 1 \end{array} \right) = \left( \begin{array}{c c} \frac {1}{s + 1} & 0 \\ \frac {1}{s (s + 1)} & \frac {1}{s} \end{array} \right)
$$

Hence

$$
\Phi = e ^ {A h} = \mathcal {L} ^ {- 1} (s I - A) ^ {- 1} = \left( \begin{array}{c c} e ^ {- h} & 0 \\ 1 - e ^ {- h} & 1 \end{array} \right)
$$

and

$$\Gamma = \int_ {0} ^ {h} \binom{e ^ {- v}}{1 - e ^ {- v}} d v = \binom{1 - e ^ {- h}}{h - 1 + e ^ {- h}}$$

where $L^{-1}$ is the inverse of the Laplace transform.

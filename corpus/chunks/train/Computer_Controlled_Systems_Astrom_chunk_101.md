# Example 2.2 Double integrator

The double integrator (see Example A.1 in Appendix A) is described by

$$
\begin{array}{l} \frac {d x}{d t} = \left( \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right) x + \left( \begin{array}{l} 0 \\ 1 \end{array} \right) u \\ y = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x \\ \end{array}
$$

Hence

$$
\Phi = e ^ {A h} = I + A h + A ^ {2} h ^ {2} / 2 + \dots = \left( \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right) + \left( \begin{array}{l l} 0 & h \\ 0 & 0 \end{array} \right) = \left( \begin{array}{l l} 1 & h \\ 0 & 1 \end{array} \right)

\Gamma = \int_ {0} ^ {h} \binom{s}{1} d s = \left( \begin{array}{c} \frac {h ^ {2}}{2} \\ h \end{array} \right)
$$

The discrete-time model of the double integrator is

$$
x (k h + h) = \left( \begin{array}{l l} 1 & h \\ 0 & 1 \end{array} \right) x (k h) + \left( \begin{array}{l} \frac {h ^ {2}}{2} \\ h \end{array} \right) u (k h) \tag {2.7}

y (k h) = \left( \begin{array}{c c} 1 & 0 \end{array} \right) x (k h)
$$

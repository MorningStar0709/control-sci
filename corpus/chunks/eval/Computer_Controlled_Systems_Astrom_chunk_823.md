# Example B.1 Computation of matrix exponential

Let

$$
A = \left( \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right)
$$

and determine

$$e ^ {A h} = \alpha_ {0} A h + \alpha_ {1} I$$

Ah has the eigenvalues ±ih; the system of equations

$$e ^ {i h} = \alpha_ {0} i h + \alpha_ {1}e ^ {- i \hbar} = - \alpha_ {0} i \hbar + \alpha_ {1}$$

holds, giving

$$\alpha_ {0} = \frac {1}{2 i h} (e ^ {i h} - e ^ {- i h}) = \frac {\sin h}{h}\alpha_ {1} = \frac {1}{2} (e ^ {i h} + e ^ {- i h}) = \cos h$$

Finally,

$$
e ^ {A h} = \sin h \left( \begin{array}{l l} 0 & 1 \\ - 1 & 0 \end{array} \right) + \cos h \left( \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right) = \left( \begin{array}{l l} \cos h & \sin h \\ - \sin h & \cos h \end{array} \right)
$$

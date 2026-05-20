# Example 4.1 Pole placement for the double-integrator plant

By using the sampling-time convention, the sampled double-integrator plant is described by

$$
x (k + 1) = \left( \begin{array}{c c} 1 & h \\ 0 & 1 \end{array} \right) x (k) + \binom {h ^ {2} / 2} {h} u (k)
$$

A general linear feedback can be described by

$$u = - l _ {1} x _ {1} - l _ {2} x _ {2}$$

With this feedback, the closed-loop system becomes

$$
x (k + 1) = \left( \begin{array}{c c} 1 - l _ {1} h ^ {2} / 2 & h - l _ {2} h ^ {2} / 2 \\ - l _ {1} h & 1 - l _ {2} h \end{array} \right) x (k)
$$

The characteristic equation of the closed-loop system is

$$z ^ {2} + \left(\frac {l _ {1} h ^ {2}}{2} + l _ {2} h - 2\right) z + \left(\frac {l _ {1} h ^ {2}}{2} - l _ {2} h + 1\right) = 0$$

Assume that the desired characteristic equation is

$$z ^ {2} + p _ {1} z + p _ {2} = 0$$

This leads to the following linear equations for $l_{1}$ and $l_{2}$ :

$$
\begin{array}{l} \frac {l _ {1} h ^ {2}}{2} + l _ {2} h - 2 = p _ {1} \\ \frac {l _ {1} h ^ {2}}{2} - l _ {2} h + 1 = p _ {2} \\ \end{array}
$$

These equations have the solution

$$l _ {1} = \frac {1}{h ^ {2}} (1 + p _ {1} + p _ {2}) \tag {4.4}l _ {2} = \frac {1}{2 h} (3 + p _ {1} - p _ {2})$$

In this example it is always possible to find controller parameters that give an arbitrary characteristic equation of the closed-loop system. The linear system of equations for $l_{1}$ and $l_{2}$ has a solution for all values of $p_{1}$ and $p_{2}$ .

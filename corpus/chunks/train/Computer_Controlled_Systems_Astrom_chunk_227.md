# Example 4.2 Double integrator

Consider the double-integrator plant in Example 4.1. Assume that the desired characteristic polynomial is given by $P(z) = z^2 + p_1z + p_2$ . We have

$$
W _ {r} = \left( \begin{array}{c c} \Gamma & \Phi \Gamma \end{array} \right) = \left( \begin{array}{c c} h ^ {2} / 2 & 3 h ^ {2} / 2 \\ h & h \end{array} \right)
$$

and

$$
W _ {c} ^ {- 1} = \left( \begin{array}{l l} - 1 / h ^ {2} & 1. 5 / h \\ 1 / h ^ {2} & - 0. 5 / h \end{array} \right)
$$

The characteristic polynomial of the matrix $\Phi$ is $z^2 - 2z + 1$ . Hence

$$
P (\Phi) = \Phi^ {2} + p _ {1} \Phi + p _ {2} I = \left( \begin{array}{c c} 1 + p _ {1} + p _ {2} & 2 h + p _ {1} h \\ 0 & 1 + p _ {1} + p _ {2} \end{array} \right)
$$

Ackermann's formula (4.14) now gives

$$
\begin{array}{l} L = \left( \begin{array}{l l} 0 & 1 \end{array} \right) W _ {c} ^ {- 1} P (\Phi) = \left( \begin{array}{l l} 1 / h ^ {2} & - 0. 5 / h \end{array} \right) P (\Phi) \\ = \left(\frac {1 + p _ {1} + p _ {2}}{h ^ {2}} \quad \frac {3 + p _ {1} - p _ {2}}{2 h}\right) \\ \end{array}
$$

which is the same result obtained by the direct calculation in Example 4.1.

To solve the pole-placement problem it was assumed that the system is reachable. The following example illustrates what happens when this is not the case.

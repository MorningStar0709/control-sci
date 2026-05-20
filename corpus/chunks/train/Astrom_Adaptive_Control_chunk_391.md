# EXAMPLE 6.2 Persistence of excitation gives structural stability

Consider the same system as in Example 6.1, but assume now that the command signal is a step, that is, $u_{c}(t) = 1$ . The system is then described by the equations

$$\frac {d e}{d t} = - e + k \tilde {\theta}\frac {d \tilde {\theta}}{d t} = - \gamma e$$

The equilibrium is $e = \tilde{\theta} = 0$ . Linearization around this fixed point gives a linear system with the system matrix.

$$
A = \left( \begin{array}{c c} - 1 & k \\ - \gamma & 0 \end{array} \right)
$$

This matrix has the characteristic polynomial

$$s ^ {2} + s + \gamma k$$

and the equilibrium is thus stable if $\gamma k$ is positive.

Figure 2.10 in Chapter 2, which illustrates a case of identification under closed-loop conditions, is a typical example of structural instability. Additional examples are given in Section 6.9.

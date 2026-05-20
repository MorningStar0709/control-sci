# Solution:

For simplicity, let us consider the simplified notation $x = x ( t ) , u = u ( t )$ and $p = p ( t )$ ). We first calculate the Hamiltonian as

$$H (t, x, u, p, p _ {0}) = \langle p, f (t, x, u) \rangle + p _ {0} L (t, x, u) \tag {215}$$

In this case, $L = 0 ;$ the Hamiltonian will be

$$H (t, x, u, p, p _ {0}) = \left\langle \left(p _ {1}, p _ {2}\right), \left(- 4 x _ {1} + 2 x _ {2} + 2 u, 3 x _ {1} - 3 x _ {2}\right) \right\rangle + \underline {{{p _ {0} L (t , x , u)}}} ^ {0} \tag {216}= p _ {1} \left(- 4 x _ {1} + 2 x _ {2} + 2 u\right) + p _ {2} \left(3 x _ {1} - 3 x _ {2}\right) \tag {217}$$

Let’s consider the set $\mathcal { U } = [ - 1 , 1 ]$ for which $u \in \mathcal { U }$ . Then, by the Pontryagin’s maximum principle, we have

$$
u ^ {*} = \underset {u \in \mathcal {U}} {\operatorname{argmax}} H \left(t, x ^ {*}, u, p ^ {*}\right) \tag {218}= \underset {u \in \mathcal {U}} {\operatorname{argmax}} p _ {1} ^ {*} (- 4 x _ {1} + 2 x _ {2} + 2 u) + p _ {2} ^ {*} (3 x _ {1} - 3 x _ {2}) \tag {219}= \underset {u \in \mathcal {U}} {\operatorname{argmax}} 2 p _ {1} ^ {*} u \tag {220}
= \left\{ \begin{array}{l l} 1 & \text { if } p _ {1} ^ {*} > 0 \\ - 1 & \text { if } p _ {1} ^ {*} <   0 \\ \text { any   number } \in \mathcal {U} & \text { if } p _ {1} ^ {*} = 0 \end{array} \right. \tag {221}
$$

Where the value of $p _ { 1 } ^ { * }$ can be found by the costate optimality equation, which is independent from $p _ { 0 }$ in this case:

$$
\dot {p} ^ {*} = - H _ {x} \left(t, x ^ {*}, u ^ {*}, p ^ {*}\right) = \left[ \begin{array}{l} 4 p _ {1} ^ {*} - 3 p _ {2} ^ {*} \\ - 2 p _ {1} ^ {*} + 3 p _ {2} ^ {*} \end{array} \right] \tag {222}
$$

By solving the differential equations we obtain

$$
\left[ \begin{array}{c} p _ {1} ^ {*} \\ p _ {2} ^ {*} \end{array} \right] = \frac {1}{5} e ^ {t} \left[ \begin{array}{c} c _ {1} (3 e ^ {5 t} + 2) - 3 c _ {2} (e ^ {5 t} - 1) \\ c _ {2} (2 e ^ {5 t} + 3) - 2 c _ {1} (e ^ {5 t} - 1) \end{array} \right] \quad c _ {1}, c _ {2} \in \mathbb {R} \tag {223}
$$

In order to get the switching time for solving $p _ { 1 } ^ { * } ( t ) = 0$ , the following ODE can be solved by imposing the condition on the derivative of the state for the Hamiltonian; along with the intial and final conditions:

$$\dot {x} ^ {*} = H _ {p} \left(t, x ^ {*}, u ^ {*}, p ^ {*}\right) \tag {224}$$

which becomes

$$
\left[ \begin{array}{c} \dot {x} _ {1} ^ {*} \\ \dot {x} _ {2} ^ {*} \end{array} \right] = \left[ \begin{array}{c} - 4 x _ {1} + 2 x _ {2} + 2 u \\ 3 x _ {1} - 3 x _ {2} \end{array} \right] \tag {226}
$$

Which yields

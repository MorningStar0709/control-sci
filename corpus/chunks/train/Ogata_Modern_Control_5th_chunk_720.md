Note that it can be immediately proved that, in the system of Equations (9–114) and (9–115), complete state controllability on $0 \leq t \leq T$ implies complete output controllability on $0 \leq t \leq T$ if and only if m rows of C are linearly independent.

A–9–16. Discuss the state controllability of the following system:

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 3 & 1 \\ - 2 & 1. 5 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 1 \\ 4 \end{array} \right] u \tag {9-119}
$$

Solution. For this system,

$$
\mathbf {A} = \left[ \begin{array}{c c} - 3 & 1 \\ - 2 & 1. 5 \end{array} \right], \qquad \mathbf {B} = \left[ \begin{array}{c} 1 \\ 4 \end{array} \right]
$$

Since

$$
\mathbf {A B} = \left[ \begin{array}{c c} - 3 & 1 \\ - 2 & 1. 5 \end{array} \right] \left[ \begin{array}{c} 1 \\ 4 \end{array} \right] = \left[ \begin{array}{c} 1 \\ 4 \end{array} \right]
$$

we see that vectors B and AB are not linearly independent and the rank of the matrix $\mathbf { \left[ B \vdots \delta A B \right] }$ is 1. Therefore, the system is not completely state controllable. In fact, elimination of $x _ { 2 }$ from Equation (9–119), or the following two simultaneous equations,

$$\dot {x} _ {1} = - 3 x _ {1} + x _ {2} + u\dot {x} _ {2} = - 2 x _ {1} + 1. 5 x _ {2} + 4 u$$

yields

$$\ddot {x} _ {1} + 1. 5 \dot {x} _ {1} - 2. 5 x _ {1} = \dot {u} + 2. 5 u$$

or, in the form of a transfer function,

$$\frac {X _ {1} (s)}{U (s)} = \frac {s + 2 . 5}{(s + 2 . 5) (s - 1)}$$

Notice that cancellation of the factor (s+2.5) occurs in the numerator and denominator of the transfer function. Because of this cancellation, this system is not completely state controllable. This is an unstable system. Remember that stability and controllability are quite different things. There are many systems that are unstable, but are completely state controllable.

A–9–17. A state-space representation of a system in the controllable canonical form is given by

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 0. 4 & - 1. 3 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u \tag {9-120}

y = \left[ \begin{array}{l l} 0. 8 & 1 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] \tag {9-121}
$$

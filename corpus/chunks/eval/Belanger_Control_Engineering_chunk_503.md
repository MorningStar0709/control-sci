# 8.9 THE AUGMENTED STATE-SPACE MODEL

Current solution algorithms are based on the state-space representation

$$\dot {\mathbf {x}} = A \mathbf {x} + B _ {1} \mathbf {w} + B _ {2} \mathbf {u}\mathbf {z} = C _ {1} \mathbf {x} + D _ {1 1} \mathbf {w} + D _ {1 2} \mathbf {u}\mathbf {y} = C _ {2} \mathbf {x} + D _ {2 1} \mathbf {w} + D _ {2 2} \mathbf {u}. \tag {8.57}$$

This representation combines the system model and the models of the various weight functions, as shown by the following example.

Example 8.8 In Example 8.7, let the following be given:

$$P (s) = \frac {1}{s ^ {2} + 0 . 2 s + 2}; \quad W _ {1} (s) = \frac {s + 1}{s (s + 1 0)}W _ {2} (s) = 1; \quad W _ {3} (s) = 2 \times 1 0 ^ {- 3} (s + 1 0) ^ {2}.$$

Write a state-space representation in the form of Equation 8.57 for the system shown in Figure 8.14 (the same as in Figure 8.13, but with the controller removed). The measured output is taken to be e in order that the result be a standard 1-DOF controller.

Solution Because no state-space model can be written for $W_{3}(s)$ , we look upon the combination of P and $W_{3}$ as one system, with an input u and outputs y and $z_{3}$ .

Since

$$\frac {z _ {3}}{u} = \frac {2 \times 1 0 ^ {- 3} (s ^ {2} + 2 0 s + 1 0 0)}{s ^ {2} + . 2 s + 1} = 2 \times 1 0 ^ {- 3} \left[ 1 + \frac {1 9 . 8 s + 9 9}{s ^ {2} + . 2 s + 1} \right]$$

the controllable canonical form is

$$
\begin{array}{l} \left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & - \dot {0}. 2 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u \\ y = x _ {1} \\ e = y _ {d} - x _ {1} \\ z _ {3} = 2 \times 1 0 ^ {- 3} [ 9 9 x _ {1} + 1 9. 8 x _ {2} ] + 2 \times 1 0 ^ {- 3} u. \\ \end{array}
$$

Now,

$$\frac {z _ {1}}{e} = W _ {1} (s) = \frac {s + 1}{s ^ {2} + 1 0 . 0 1 s + 0 . 1}$$

so that

$$
\begin{array}{l} \left[ \begin{array}{l} \dot {x} _ {3} \\ \dot {x} _ {4} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ -. 1 & - 1 0. 0 1 \end{array} \right] \left[ \begin{array}{l} x _ {3} \\ x _ {4} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] (y _ {d} - x _ {1}). \\ z _ {1} = x _ {3} + x _ {4}. \\ \end{array}
$$

Putting these expressions together, with $w = y_{d}$ ,

$$
\dot {\mathbf {x}} = \left[ \begin{array}{r r r r} 0 & 1 & 0 & 0 \\ - 1 & - 0. 2 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ - 1 & 0 & -. 1 & - 1 0. 0 1 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 1 \end{array} \right] y _ {d} + \left[ \begin{array}{l} 0 \\ 1 \\ 0 \\ 0 \end{array} \right] u

y = \left[ \begin{array}{l l l l} - 1 & 0 & 0 & 0 \end{array} \right] \mathbf {x} + y _ {d}

\mathbf {z} = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ . 1 9 8 & . 0 3 9 6 & 0 & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{c} 0 \\ 1 \\ 2 \times 1 0 ^ {- 3} \end{array} \right] u.
$$

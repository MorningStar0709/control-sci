In this case, we have scalars instead of matrices, so the ARE becomes $$0 = a P + P a + q - p b \frac {1}{r} b p \tag {409}\Longrightarrow - \frac {b ^ {2} P ^ {2}}{r} + 2 a P + q = 0 \tag {410}$$ Solving the equation, we get as a solution (choosing the positive sign, since we have the condition that $P \geq 0 )$ : $$P = \frac {r \left(a + \sqrt {a ^ {2} + \frac {b ^ {2} q}{r}}\right)}{b ^ {2}} \tag {411}$$ Therefore, the closed-loop gain K becomes: $$K = - \frac {1}{r} b \frac {r \left(a + \sqrt {a ^ {2} + \frac {b ^ {2} q}{r}}\right)}{b ^ {2}} = - \frac {a + \sqrt {a ^ {2} + \frac {b ^ {2} q}{r}}}{b} \tag {412}$$ where $K \in \mathbb { R }$ .
The closed-loop system becomes: $$\dot {x} ^ {*} (t) = A x ^ {*} (t) + B u ^ {*} (t) = (a - K b) x ^ {*} (t) \tag {413}$$ The eigenvalue of the closed loop system is the value of the scalar $a - K b$ in this case.
# Eigenvalues of the closed-loop system by changing r • Case 1: $r 0 .$ , we have the following limit for the gain K $$\lim _ {r \rightarrow 0} (a - K b) = \lim _ {r \rightarrow 0} a - b \frac {a + \sqrt {a ^ {2} + \frac {b ^ {2} q}{r}}}{b} = a - (a + \sqrt {a ^ {2} + \infty}) = - \infty \tag {414}$$ • Case 2: $r \infty ,$ , we have the following limit for the gain K $$\lim _ {r \rightarrow \infty} (a - K b) = \lim _ {r \rightarrow \infty} a - b \frac {a + \sqrt {a ^ {2} + \frac {b ^ {2} q}{r}}}{b} = \tag {415}= a - \left(a + \sqrt {a ^ {2} + \frac {b ^ {2} q}{\infty}}\right) = a - \left(a + \sqrt {a ^ {2}}\right) = - a \tag {416}$$ # Exercise 6.25 (Boeing 747 Lateral Model) The complete lateral model of a Boeing 747 is $$\dot {x} (t) = A x (t) + B u (t) \tag {417}y (t) = C x (t) + D u (t) \tag {418}$$ where $$
A = \left[ \begin{array}{c c c c c c} - 1 0 & 0 & 0 & 0 & 0 & 0 \\ 0.
0 7 2 9 & - 0.
0 5 5 8 & - 0.
9 9 7 & 0.
0 8 0 2 & 0.
0 4 1 5 & 0 \\ - 4.
7 5 & 0.
5 9 8 & - 0.
1 1 5 & - 0.
0 3 1 8 & 0 & 0 \\ 1.
5 3 & - 3.
0 5 & 0.
3 8 8 & - 0.
4 6 5 & 0 & 0 \\ 0 & 0 & 0.
0 8 0 5 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & - 0.
3 3 3 3 \end{array} \right], \quad B = \left[ \begin{array}{l} 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{array} \right] \tag {419}
$$ and $$
C = \left[ \begin{array}{l l l l l l} 0 & 0 & 1 & 0 & 0 & - 0.
3 3 3 3 \end{array} \right], \quad D = 0 \tag {420}
$$ Minimize the sum of the energy of the output y and the energy of the control u.
The main effort is to minimize the energy of y which is supposed to be zero in a steady state condition.
So we put a weight $q = 9 .
5 2 7 > 1$ on the energy of y.
The problem now is as follows.

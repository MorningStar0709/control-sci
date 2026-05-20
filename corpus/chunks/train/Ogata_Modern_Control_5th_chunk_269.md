Now consider the following characteristic equation:

$$a _ {0} s ^ {4} + a _ {1} s ^ {3} + a _ {2} s ^ {2} + a _ {3} s + a _ {4} = 0$$

Obtain the conditions for stability using the Hurwitz stability criterion.

Solution. The conditions for stability are that all the a’s be positive and that

$$
\begin{array}{l} \Delta_ {2} = \left| \begin{array}{c c} a _ {1} & a _ {3} \\ a _ {0} & a _ {2} \end{array} \right| = a _ {1} a _ {2} - a _ {0} a _ {3} > 0 \\ \Delta_ {3} = \left| \begin{array}{c c c} a _ {1} & a _ {3} & 0 \\ a _ {0} & a _ {2} & a _ {4} \\ 0 & a _ {1} & a _ {3} \end{array} \right| \\ = a _ {1} \left(a _ {2} a _ {3} - a _ {1} a _ {4}\right) - a _ {0} a _ {3} ^ {2} \\ = a _ {3} \left(a _ {1} a _ {2} - a _ {0} a _ {3}\right) - a _ {1} ^ {2} a _ {4} > 0 \\ \end{array}
$$

It is clear that, if all the a’s are positive and if the condition $\Delta _ { 3 } > 0$ is satisfied, the condition $\Delta _ { 2 } > 0$ is also satisfied.Therefore, for all the roots of the given characteristic equation to have negative real parts, it is necessary and sufficient that all the coefficients a’s are positive and $\Delta _ { 3 } > 0$ .

A–5–19. Show that the first column of the Routh array of

$$s ^ {n} + a _ {1} s ^ {n - 1} + a _ {2} s ^ {n - 2} + \dots + a _ {n - 1} s + a _ {n} = 0$$

is given by

$$1, \quad \Delta_ {1}, \quad \frac {\Delta_ {2}}{\Delta_ {1}}, \quad \frac {\Delta_ {3}}{\Delta_ {2}}, \ldots , \quad \frac {\Delta_ {n}}{\Delta_ {n - 1}}$$

where

$$
\Delta_ {r} = \left| \begin{array}{c c c c c c} a _ {1} & 1 & 0 & 0 & \cdot & 0 \\ a _ {3} & a _ {2} & a _ {1} & 1 & \cdot & 0 \\ a _ {5} & a _ {4} & a _ {3} & a _ {2} & \cdot & 0 \\ \cdot & \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & \cdot & & \cdot \\ a _ {2 r - 1} & \cdot & \cdot & \cdot & \cdot & a _ {r} \end{array} \right|, \quad (n \geq r \geq 1)
a _ {k} = 0 \quad \text { if } k > n
$$

Solution. The Routh array of coefficients has the form

$$
\begin{array}{l} 1 \quad a _ {2} \quad a _ {4} \quad a _ {6} \quad \dots \quad a _ {n} \\ \begin{array}{c c c c} a _ {1} & a _ {3} & a _ {5} & \dots \end{array} \\ \begin{array}{c c c c} b _ {1} & b _ {2} & b _ {3} & \dots \end{array} \\ \begin{array}{c c c} c _ {1} & c _ {2} \end{array} . \\ \cdot \cdot \cdot \\ \cdot \cdot \cdot \\ \begin{array}{c c c} \bullet & \bullet & \bullet \\ \hline \end{array} \\ \end{array}
$$

The first term in the first column of the Routh array is 1. The next term in the first column is $a _ { 1 }$ , which is equal to $\Delta _ { 1 }$ The next term is. $b _ { 1 }$ , which is equal to

$$\frac {a _ {1} a _ {2} - a _ {3}}{a _ {1}} = \frac {\Delta_ {2}}{\Delta_ {1}}$$

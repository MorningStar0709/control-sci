# Example 2.8

Find the optimum of

$$J = \int_ {0} ^ {2} [ \dot {x} ^ {2} (t) - 2 t x (t) ] d t \tag {2.3.33}$$

that satisfy the boundary (initial and final) conditions

$$x (0) = 1 \quad \text { and } \quad x (2) = 5. \tag {2.3.34}$$

Solution: In the EL equation (2.3.19), we first identify that $V = \dot{x}^{2}(t) - 2tx(t)$ . Then applying the EL equation (2.3.15) to the performance index (2.3.33) we get

$$
\begin{array}{l} \frac {\partial V}{\partial x} - \frac {d}{d t} \left(\frac {\partial V}{\partial \dot {x}}\right) = 0 \longrightarrow - 2 t - \frac {d}{d t} (2 \dot {x} (t)) = 0 \\ \longrightarrow \ddot {x} (t) = t. \tag {2.3.35} \\ \end{array}
$$

Solving the previous simple differential equation, we have

$$x ^ {*} (t) = \frac {t ^ {3}}{6} + C _ {1} t + C _ {2} \tag {2.3.36}$$

where, $C_1$ and $C_2$ are constants of integration. Using the given boundary conditions (2.3.19) in (2.3.36), we have

$$x (0) = 1 \longrightarrow C _ {2} = 1, x (2) = 5 \longrightarrow C _ {1} = \frac {4}{3}. \tag {2.3.37}$$

With these values for the constants, we finally have the optimal function as

$$x ^ {*} (t) = \frac {t ^ {3}}{6} + \frac {4}{3} t + 1. \tag {2.3.38}$$

Another classical example in the calculus of variations is the brachistochrone (from brachisto, the shortest, and chrones, time) problem and this problem is dealt with in almost all books on calculus of variations [126].

Further, note that we have considered here only the so-called fixed-end point problem where both (initial and final) ends are fixed or given in advance. Other types of problems such as free-end point problems are not presented here but can be found in most of the books on the calculus of variations $[79, 46, 81, 48]$ . However, these free-end point problems are better considered later in this chapter when we discuss the optimal control problem consisting of a performance index and a physical plant.

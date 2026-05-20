# Example 3.1

Let us illustrate the previous procedure with a simple second order example. Given a double integral system

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t), \quad x _ {1} (0) = 2 \\ \dot {x} _ {2} (t) = - 2 x _ {1} (t) + x _ {2} (t) + u (t), \quad x _ {2} (0) = - 3, \tag {3.3.24} \\ \end{array}
$$

and the performance index (PI)

$$
\begin{array}{l} J = \frac {1}{2} \left[ x _ {1} ^ {2} (5) + x _ {1} (5) x _ {2} (5) + 2 x _ {2} ^ {2} (5) \right] \\ + \frac {1}{2} \int_ {0} ^ {5} \left[ 2 x _ {1} ^ {2} (t) + 6 x _ {1} (t) x _ {2} (t) + 5 x _ {2} ^ {2} (t) + 0. 2 5 u ^ {2} (t) \right] d t, \tag {3.3.25} \\ \end{array}
$$

obtain the feedback control law.

Solution: Comparing the present plant (3.3.24) and the PI (3.3.25) of the problem with the corresponding general formulations of the plant (3.2.31) and the PI (3.2.32), respectively, let us first identify the various quantities as

$$
\begin{array}{l} \mathbf {A} (t) = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & 1 \end{array} \right]; \quad \mathbf {B} (t) = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]; \quad \mathbf {F} (t _ {f}) = \left[ \begin{array}{c c} 1 & 0. 5 \\ 0. 5 & 2 \end{array} \right] \\ \mathbf {Q} (t) = \left[ \begin{array}{c c} 2 & 3 \\ 3 & 5 \end{array} \right]; \quad \mathbf {R} (t) = r (t) = \frac {1}{4}; \quad t _ {0} = 0; \quad t _ {f} = 5. \\ \end{array}
$$

It is easy to check that the system (3.3.24) is unstable. Let $\mathbf{P}(t)$ be the 2x2 symmetric matrix

$$
\mathbf {P} (t) = \left[ \begin{array}{l l} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right]. \tag {3.3.26}
$$

Then, the optimal control (3.2.33) is given by

$$
\begin{array}{l} u ^ {*} (t) = - 4 \left[ \begin{array}{c c} 0 & 1 \end{array} \right] \left[ \begin{array}{c c} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right] \left[ \begin{array}{c} x _ {1} ^ {*} (t) \\ x _ {2} ^ {*} (t) \end{array} \right] \\ = - 4 \left[ p _ {1 2} (t) x _ {1} ^ {*} (t) + p _ {2 2} (t) x _ {2} ^ {*} (t) \right] \tag {3.3.27} \\ \end{array}
$$

where, $\mathbf{P}(t)$ , the 2x2 symmetric, positive definite matrix, is the solution of the matrix DRE (3.2.34)

# Example 7.4

The system $\dot{\mathbf{x}} = [ \begin{array}{cc}0 & 1 \\ 0 & -1 \end{array} ]\mathbf{x} + [ \begin{array}{c}0 \\ 1 \end{array} ]u$ is to be controlled with the state feedback law $u = -kx_{1}$ . For $\mathbf{x}(0) = \mathbf{x}_0$ , calculate

$$J = \int_ {0} ^ {\infty} [ \mathbf {x} ^ {T} (t) Q \mathbf {x} (t) + r u ^ {2} (t) ] d t$$

with Q = I.

Solution From Equations 7.20 and 7.21, with $K = [k \ 0]$ ,

$$
\begin{array}{l} \dot {\mathbf {x}} = \left(\left[ \begin{array}{c c} 0 & 1 \\ 0 & - 1 \end{array} \right] - \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] [ k 0 ]\right) \mathbf {x} \\ = \left[ \begin{array}{c c} 0 & 1 \\ - k & - 1 \end{array} \right] \mathbf {x} \\ \end{array}
$$

and

$$
\begin{array}{l} J = \int_ {0} ^ {\infty} \mathbf {x} ^ {T} (t) \left\{\left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] + \left[ \begin{array}{l} k \\ 0 \end{array} \right] r [ k 0 ] \right\} \mathbf {x} (t) d t \\ = \int_ {0} ^ {\infty} \mathbf {x} ^ {T} (t) \left[ \begin{array}{c c} 1 + r k ^ {2} & 0 \\ 0 & 1 \end{array} \right] \mathbf {x} (t) d t. \\ \end{array}
$$

We then apply the matrix Lyapunov equation,

$$
\left[ \begin{array}{c c} 0 & - k \\ 1 & - 1 \end{array} \right] \left[ \begin{array}{c c} P _ {1 1} & P _ {1 2} \\ P _ {1 2} & P _ {2 2} \end{array} \right] + \left[ \begin{array}{c c} P _ {1 1} & P _ {1 2} \\ P _ {1 2} & P _ {2 2} \end{array} \right] \left[ \begin{array}{c c} 0 & 1 \\ - k & - 1 \end{array} \right] = - \left[ \begin{array}{c c} 1 + r k ^ {2} & 0 \\ 0 & \mathbf {1} \end{array} \right]
$$

where the symmetry of $P$ has been invoked, to make $P_{21} = P_{12}$ . This is a matrix equation, so we must equate element by element. For the 11 element,

$$- k P _ {1 2} - k P _ {1 2} = - 1 - r k ^ {2}.$$

For the 12 element,

$$- k P _ {2 2} + P _ {1 1} - P _ {1 2} = 0.$$

For the 21 element,

$$P _ {1 1} - P _ {1 2} - k P _ {2 2} = 0.$$

For the 22 element,

$$P _ {1 2} - P _ {2 2} + P _ {1 2} - P _ {2 2} = - 1.$$

Note that the "12" and "21" equations are identical. The reason is that both the LHS and RHS are symmetric matrices. In any case, since $P$ has only three distinct elements, we only need three equations. Summarized, they are

$$2 k P _ {1 2} = 1 + r k ^ {2}P _ {1 1} - P _ {1 2} - k P _ {2 2} = 02 P _ {1 2} - 2 P _ {2 2} = - 1.$$

The solution is

$$P _ {1 1} = \frac {1}{2 k} + \frac {1}{2} + (r + 1) \frac {k}{2} + \frac {r k ^ {2}}{2}P _ {1 2} = \frac {1}{2 k} + \frac {r k}{2}P _ {2 2} = \frac {1}{2 k} + \frac {1}{2} + \frac {r k}{2}.$$

Since $J = \mathbf{x}^T (0)P\mathbf{x}(0),$

$$J = P _ {1 1} x _ {1} ^ {2} (0) + 2 P _ {1 2} x _ {1} (0) x _ {2} (0) + P _ {2 2} x _ {2} ^ {2} (0).$$

In Figure 7.6, $J$ is plotted against $k$ , for $\mathbf{x}(0) = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $r = 0, 1, 2$ . As $r$ increases, the optimal value of $k$ decreases, reflecting the fact that increasing the penalty on the control effort tends to decrease the gain in order to reduce the control.

In Figure 7.7 we plot $J$ versus $k$ for $r = 1$ and two initial states, $\mathbf{x}(0) = [_{0}^{1}]$ and $[_{1}^{0}]$ . It is to be noted that the minimizing value of $k$ differs for different initial states; there does not exist a value of $k$ that is best for all initial states.

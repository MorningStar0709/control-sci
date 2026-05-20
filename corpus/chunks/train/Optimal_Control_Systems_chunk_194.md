Solving the previous equations for positive definiteness of $\bar{P}$ is easy in this particular case. Thus, solve the first equation in (3.5.25) for $\bar{p}_{12}$ , using this value of $\bar{p}_{12}$ in the third equation solve for $\bar{p}_{22}$ and finally using the values of $\bar{p}_{12}$ and $\bar{p}_{22}$ in the second equation, solve for $\bar{p}_{11}$ . In general, we have to solve the nonlinear algebraic equations and pick up the positive definite values for $\bar{P}$ . Hence, we get

$$
\bar {\mathbf {P}} = \left[ \begin{array}{l l} 1. 7 3 6 3 & 0. 3 6 6 0 \\ 0. 3 6 6 0 & 1. 4 7 2 9 \end{array} \right]. \tag {3.5.26}
$$

Using these Riccati coefficients (gains), the closed-loop optimal control (3.5.23) is given by

$$
\begin{array}{l} u ^ {*} (t) = - 4 \left[ 0. 3 6 6 x _ {1} ^ {*} (t) + 1. 4 7 2 9 x _ {2} ^ {*} (t) \right] \\ = - [ 1. 4 6 4 x _ {1} ^ {*} (t) + 5. 8 9 1 6 x _ {2} ^ {*} (t) ]. \tag {3.5.27} \\ \end{array}
$$

Using the closed-loop optimal control $u^{*}(t)$ from (3.5.27) in the original open-loop system (3.5.18), the closed-loop optimal system becomes

$$
\begin{array}{l} \dot {x} _ {1} ^ {*} (t) = x _ {2} ^ {*} (t) \\ \dot {x} _ {2} ^ {*} (t) = - 2 x _ {1} ^ {*} (t) + x _ {2} ^ {*} (t) - 4 \left[ 0. 3 6 6 x _ {1} ^ {*} (t) + 1. 4 7 2 9 x _ {2} ^ {*} (t) \right] \tag {3.5.28} \\ \end{array}
$$

and the implementation of the closed-loop optimal control is shown in Figure 3.9.

Using the initial conditions and the Riccati coefficient matrix (3.5.26), the optimal cost (3.5.17) is obtained as

$$
\begin{array}{l} J ^ {*} = \frac {1}{2} \mathbf {x} ^ {\prime} (0) \bar {\mathbf {P}} \mathbf {x} (0) = \frac {1}{2} \left[ 2 - 3 \right] \left[ \begin{array}{l l} 1. 7 3 6 3 & 0. 3 6 6 0 \\ 0. 3 6 6 0 & 1. 4 7 2 9 \end{array} \right] \left[ \begin{array}{l} 2 \\ - 3 \end{array} \right], \\ = 7. 9 0 4 7. \tag {3.5.29} \\ \end{array}
$$

![](image/d81b4f0d4676ef3914dee179d9b6a8d0dbbbff332220c74a0cef891f374c1339.jpg)

<details>
<summary>flowchart</summary>

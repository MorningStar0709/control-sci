Figure 5.2 Closed-Loop Optimal Controller for Linear Discrete-Time Regulator

Solution: Let us first identify the various matrices by comparing the system (5.3.31) and the PI (5.3.30) of the system with the system (5.2.1) and the PI (5.2.3) of the general formulation as

$$
\mathbf {A} (k) = \left[ \begin{array}{c c} 0. 8 & 1. 0 \\ 0. 0 & 0. 6 \end{array} \right]; \quad \mathbf {B} (k) = \left[ \begin{array}{c} 1. 0 \\ 0. 5 \end{array} \right];

\mathbf {F} (k _ {f}) = \left[ \begin{array}{c c} 2. 0 & 0 \\ 0 & 4. 0 \end{array} \right]; \quad \mathbf {Q} (k) = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right]; \quad \mathbf {R} = 1. \tag {5.3.33}
$$

Now let us use the procedure given in Table 5.3.

\- Step 1: Solve the matrix difference Riccati equation (5.3.11)

$$
\begin{array}{l} \left[ \begin{array}{c c} p _ {1 1} (k) & p _ {1 2} (k) \\ p _ {1 2} (k) & p _ {2 2} (k) \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] + \left[ \begin{array}{c c} 0. 8 & 0. 0 \\ 1. 0 & 0. 6 \end{array} \right] \left[ \begin{array}{c c} p _ {1 1} (k + 1) & p _ {1 2} (k + 1) \\ p _ {1 2} (k + 1) & p _ {2 2} (k + 1) \end{array} \right]. \\ \begin{array}{r} \left[ \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] + \left[ \begin{array}{l} 1. 0 \\ 0. 5 \end{array} \right] [ 1 ] ^ {- 1} [ 1. 0 0. 5 ] \left[ \begin{array}{l l} p _ {1 1} (k + 1) & p _ {1 2} (k + 1) \\ p _ {1 2} (k + 1) & p _ {2 2} (k + 1) \end{array} \right] \right] ^ {- 1} x \\ \left[ \begin{array}{l l} 0. 8 & 1. 0 \\ 0. 0 & 0. 6 \end{array} \right] \end{array} \tag {5.3.34} \\ \end{array}
$$

backwards in time starting with the final condition (5.3.14) as

$$
\left[ \begin{array}{l l} p _ {1 1} (1 0) & p _ {1 2} (1 0) \\ p _ {1 2} (1 0) & p _ {2 2} (1 0) \end{array} \right] = \mathbf {F} (k _ {f}) = \left[ \begin{array}{c c} 2. 0 & 0 \\ 0 & 4. 0 \end{array} \right]. \tag {5.3.35}
$$

\- Step 2: The optimal control $u^{*}(k)$ is obtained from (5.3.16) as

$$
u ^ {*} (k) = - \left[ l _ {1} (k) l _ {2} (k) \right] \left[ \begin{array}{l} x _ {1} (k) \\ x _ {2} (k) \end{array} \right] \tag {5.3.36}
$$

where $\mathbf{l}' = [l_1, l_2]$ is given by (5.3.17).

\- Step 3: Using the optimal control (5.3.36) the optimal states are computed by solving the state equation (5.3.18) forward in time. This is an iterative process in the backward direction. Evaluation of these solutions require the use of standard software such as MATLAB $^{©}$ as shown below.

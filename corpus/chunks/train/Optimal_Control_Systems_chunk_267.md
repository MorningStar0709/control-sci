# 5.2 Discrete-Time Optimal Control Systems

where, the positive definiteness of $\mathbf{R}(k)$ ensures its invertibility. Using the optimal control (5.2.20) in the state equation (5.2.17) we get

$$
\begin{array}{l} \mathbf {x} ^ {*} (k + 1) = \mathbf {A} (k) \mathbf {x} ^ {*} (k) - \mathbf {B} (k) \mathbf {R} ^ {- 1} (k) \mathbf {B} ^ {\prime} (k) \boldsymbol {\lambda} ^ {*} (k + 1) \\ = \mathbf {A} (k) \mathbf {x} ^ {*} (k) - \mathbf {E} (k) \boldsymbol {\lambda} ^ {*} (k + 1) \tag {5.2.21} \\ \end{array}
$$

where, $\mathbf{E}(k) = \mathbf{B}(k)\mathbf{R}^{-1}(k)\mathbf{B}'(k)$ .

\- Step 6: State and Costate System: The canonical (state and costate) system of (5.2.21) and (5.2.18) becomes

$$
\left[ \begin{array}{l} \mathbf {x} ^ {*} (k + 1) \\ \boldsymbol {\lambda} ^ {*} (k) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} (k) & - \mathbf {E} (k) \\ \mathbf {Q} (k) & \mathbf {A} ^ {\prime} (k) \end{array} \right] \left[ \begin{array}{l} \mathbf {x} ^ {*} (k) \\ \boldsymbol {\lambda} ^ {*} (k + 1) \end{array} \right]. \tag {5.2.22}
$$

The state and costate (or Hamiltonian) system (5.2.22) is shown in Figure 5.1. Note that the preceding Hamiltonian system (5.2.22) is not symmetrical in the sense that $\mathbf{x}^{*}(k+1)$ and $\boldsymbol{\lambda}^{*}(k)$ are related in terms of $\mathbf{x}^{*}(k)$ and $\boldsymbol{\lambda}^{*}(k+1)$ .

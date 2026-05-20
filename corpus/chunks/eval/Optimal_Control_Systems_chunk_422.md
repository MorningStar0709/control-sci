$$
u ^ {*} (t) = \left\{ \begin{array}{l l} + 1. 0 & \text { if } 0. 5 \lambda^ {*} (t) \leq - 1 \text { or } \lambda^ {*} (t) \leq - 2, \\ - 1. 0 & \text { if } 0. 5 \lambda^ {*} (t) \geq + 1 \text { or } \lambda^ {*} (t) \geq + 2, \\ - 0. 5 \lambda^ {*} (t) & \text { if } | 0. 5 \lambda^ {*} (t) | \leq 1 \text { or } | \lambda^ {*} (t) | \leq + 2. \end{array} \right. \tag {7.5.42}
$$

The previous relationship between the optimal control $u^{*}(t)$ and the optimal costate $\lambda^{*}(t)$ is shown in Figure 7.40.

We note from (7.5.42) that the condition $u^{*}(t) = -\frac{1}{2}\lambda^{*}(t)$ is also obtained from the results of unconstrained control using the Hamiltonian (7.5.38) and the condition

$$\frac {\partial H}{\partial u} = 0 \longrightarrow 2 u ^ {*} (t) + \lambda^ {*} (t) = 0 \longrightarrow u ^ {*} (t) = - \frac {1}{2} \lambda^ {*} (t). \tag {7.5.43}$$

Consider the costate function $\lambda^{*}(t)$ in (7.5.40). The condition $\lambda^{*}(0)=0$ is not admissible because then according to (7.5.41), $u^{*}(t)=0$ for $t\in[0,t_{f}]$ , and the state $x^{*}(t)=x(0)\epsilon^{at}$ in (7.5.39) will never reach the origin in time $t_{f}$ for an arbitrarily given initial state $x(0)$ .

Then, the costate $\lambda^{*}(t) = \lambda(0)\epsilon^{-at}$ has four possible solutions depending upon the initial values $(0 < \lambda(0) < 2, \lambda(0) > 2, -2 < \lambda(0) < 0, \lambda(0) < -2)$ as shown in Figure 7.41.

1. $0 < \lambda(0) < 2$ : For this case, Figure 7.41, curve (a),

$$u ^ {*} (t) = \left\{- \frac {1}{2} \lambda^ {*} (t) \right\} \text {or} \left\{- \frac {1}{2} \lambda^ {*} (t), - 1 \right\} \tag {7.5.44}$$

depending upon whether the system reaches the origin before or after time $t_{a}$ , the function $\lambda^{*}(t)$ reaches the value of +2.

2. $\lambda(0) > 2$ : In this case, Figure 7.41, curve (b), since $\lambda^{*}(t) > +2$ , the optimal control $u^{*}(t) = \{-1\}$ .

3. $-2 < \lambda(0) < 0$ : Depending on whether the state reaches the origin before or after time $t_c$ , the function $\lambda^*(t)$ reaches the value -2, the optimal control is (Figure 7.41, curve (c))

$$u ^ {*} (t) = \left\{- \frac {1}{2} \lambda^ {*} (t) \right\} \text {or} \left\{- \frac {1}{2} \lambda^ {*} (t), + 1 \right\}. \tag {7.5.45}$$

![](image/22fab1d1cdce96c28cc50b919cf1a835767993e3fa87f64d3cea24c2ca04eefa.jpg)

<details>
<summary>flowchart</summary>

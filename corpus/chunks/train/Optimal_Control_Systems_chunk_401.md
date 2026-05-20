|u*|+u*λ₂*
u* = -1
u* = +1
+1
u* = 0
-1
u* = 0
+1
λ₂*
0≤u*≤1
-1≤u*≤0
u* = +1
-1
u* = -1
</details>

Figure 7.17 Relations Between $\lambda_2^* (t)$ and $|u^{*}(t)| + u^{*}(t)\lambda_{2}^{*}(t)$

$$
\begin{array}{l} f _ {o} = \left\{ \begin{array}{l l} 0 & \text { if } | f _ {i} | <   1 \\ s g n \{f _ {i} \} & \text { if } | f _ {i} | > 1 \end{array} \right. \\ 0 \leq f _ {o} \leq 1 \\ - 1 \leq f _ {o} \leq 0 \\ \text { if } \quad f _ {i} = + 1 \\ \text { if } \quad f _ {i} = - 1. \\ \end{array}
$$

The dead-zone function is illustrated in Figure 7.18.

Using the definition of the $dez$ function (7.3.13), we write the control strategy (7.3.12) as

$$\boxed {u ^ {*} (t) = - d e z \{\lambda_ {2} ^ {*} (t) \}.} \tag {7.3.14}$$

Using the previous definition of dead-zone function (7.3.13), the optimal control (7.3.14) is illustrated by Figure 7.19.

\- Step 4: Costate Solutions: Using the Hamiltonian (7.3.4), the

![](image/c94e42fae836c4d736e783b3b11d3d9f5a6bd1110b824ce632a4139cb69953f0.jpg)

<details>
<summary>line</summary>

| f_i | f_o |
| --- | --- |
| -1 | -1 |
| +1 | +1 |
</details>

Figure 7.18 Dead-Zone Function   
![](image/169892883f7f959bc290ed6c44c46c92f41e41f1d75a5655d2fba49e5ea97b40.jpg)

<details>
<summary>text_image</summary>

-λ₂*
-1
+1
-1
+1
u*
</details>

Figure 7.19 Fuel-Optimal Control

costates are described by

$$\dot {\lambda} _ {1} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial x _ {1} ^ {*}} = 0,\dot {\lambda} _ {2} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial x _ {2} ^ {*}} = - \lambda_ {1} ^ {*} (t), \tag {7.3.15}$$

the solutions of which become

$$\lambda_ {1} ^ {*} (t) = \lambda_ {1} (0); \quad \lambda_ {2} ^ {*} (t) = - \lambda_ {1} (0) t + \lambda_ {2} (0). \tag {7.3.16}$$

From Figure 7.19), depending upon the values of $\lambda_1(0) \neq 0$ and $\lambda_2(0)$ , there are 9 admissible fuel-optimal control sequences:

$$\{0 \}, \quad \{+ 1 \}, \quad \{- 1 \}, \quad \{- 1, 0 \}, \quad \{0, + 1 \}, \quad \{+ 1, 0 \}, \quad \{0, - 1 \}\{- 1, 0, + 1 \}, \quad \{+ 1, 0, - 1 \}. \tag {7.3.17}$$

\- Step 5: State Trajectories: The solutions of the state equations (7.3.1), already obtained in (7.2.15) under time-optimal control system, are (omitting \* for simplicity)

$$x _ {1} (t) = x _ {1 0} - \frac {1}{2} U x _ {2 0} ^ {2} + \frac {1}{2} U x _ {2} ^ {2} (t),t = [ x _ {2} (t) - x _ {2 0} ] / U \tag {7.3.18}$$

# Exercise 3.7: Simulating a robust MPC controller

This exercise explores robust MPC for linear systems with an additive bounded disturbance

$$x ^ {+} = A x + B u + w$$

The first task, using the tube-based controller described in Section 3.4.3 is to determine state and control constraint sets Z and V such that if the nominal system $z ^ { + } = A z + B \nu$ satisfies $z \in \mathbb { Z }$ and $\nu \in \mathbb { V } ,$ then the actual system $x ^ { + } \ = \ A x + B u + w$ with $u \ =$ $\nu + K ( x - z )$ where K is such that $A + B K$ is strictly stable, satisfies the constraints $x \in \mathbb { X }$ and $u \in \mathbb { V }$ .

![](image/cbdf7d0503b0ddd2b2ddf32f66ade605de3463f38d8d7b1f4973cda6d5665b13.jpg)

<details>
<summary>scatter</summary>

| x1 | x2 |
| --- | --- |
| -1.0 | -1.0 |
| 0.0 | 0.0 |
| 1.0 | 1.0 |
| 1.0 | 0.0 |
</details>

Figure 3.9: Closed-loop robust MPC state evolution with $| \boldsymbol { w } | \le 0 . 1$ from four different $x _ { 0 }$ .

(a) To get started, consider the scalar system

$$x ^ {+} = x + u + w$$

with constraint sets $\mathbb { X } = \{ x \mid x \leq 2 \} , \mathbb { U } = \{ u \mid | u | \leq 1 \}$ and $\mathbb { W } = \{ w \mid \mid w \mid \leq$ 0.1}. Choose $K = - ( 1 / 2 )$ so that $A _ { K } = 1 / 2$ . Determine Z and V so that if the nominal system $z ^ { + } = z + \nu$ satisfies $z \in \mathbb { Z }$ and $\nu \in \mathbb { V } ,$ , the uncertain system $\pmb { x } ^ { + } = A \pmb { x } + B \pmb { u } + \pmb { w } , \pmb { u } = \pmb { \nu } + K ( \pmb { x } - z )$ satisfies $x \in \mathbb { X } , u \in \mathbb { U }$ .

(b) Repeat part (a) for the following uncertain system

$$
x ^ {+} = \left[ \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right] x + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u + w
$$

with the constraint sets $\mathbb { W } = [ - 0 . 1 , 0 . 1 ]$ . Choose $\begin{array} { r l } & { \mathbb { X } \ = \ \{ x \ \in \mathbb { R } ^ { 2 } \mid x _ { 1 } \leq 2 \} , \mathbb { U } \ = \ \{ u \in \mathbb { R } \mid | u | \leq 1 \} } \\ & { K = \Big \lceil - 0 . 4 \quad - 1 . 2 \Big \rceil . } \end{array}$ and

(c) Determine a model predictive controller for the nominal system and constraint sets Z and V used in (b).   
(d) Implement robust MPC for the uncertain system and simulate the closed-loop system for a few initial states and a few disturbance sequences for each initial state. The phase plot for initial states [−1, −1], [1, 1], [1, 0] and [0, 1] should resemble Figure 3.9.

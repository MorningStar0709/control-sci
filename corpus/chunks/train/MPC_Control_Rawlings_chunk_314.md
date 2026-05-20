# Exercise 2.7: Infinite horizon cost to go as terminal penalty

Consider the system

$$x ^ {+} = A x + B u$$

subject to the constraints

$$x \in \mathbb {X} \quad u \in \mathbb {U}$$

in which

$$
A = \left[ \begin{array}{c c} 2 & 1 \\ 0 & 2 \end{array} \right] \qquad B = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right]
$$

and

$$\mathbb {X} = \{x \in \mathbb {R} ^ {2} \mid - 5 \leq x _ {1} \leq 5 \} \quad \mathbb {U} = \{u \in \mathbb {R} ^ {2} | - \mathbf {1} \leq u \leq \mathbf {1} \}$$

The cost is

$$V _ {N} (x, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) + V _ {f} (x (N))$$

in which

$$
\ell (x, u) = (1 / 2) (| x | _ {Q} ^ {2} + | u | ^ {2}) \qquad Q = \left[ \begin{array}{c c} \alpha & 0 \\ 0 & \alpha \end{array} \right]
$$

![](image/a2bfd2a8afb8ab92476286c6762853da5799fbb107fde778583e94ad35c78dff.jpg)

<details>
<summary>line</summary>

| x1 | x2 |
| --- | --- |
| -3 | 3 |
| -2 | 2 |
| -1 | 1 |
| 0 | 0 |
| 1 | -1 |
| 2 | -2 |
| 3 | -3 |
</details>

Figure 2.8: The region $\mathbb { X } _ { f }$ , in which the unconstrained LQR control law is feasible for Exercise 2.7.

and $V _ { f } ( \cdot )$ is the terminal penalty on the final state and $\mathbf { 1 } \in \mathbb { R } ^ { 2 }$ is a vector of all ones. Use $\alpha = 1 0 ^ { - 5 }$ and $N = 3$ and terminal cost $V _ { f } ( x ) = ( 1 / 2 ) x ^ { \prime } \Pi x$ where Π is the solution to the steady-state Riccati equation.

(a) Compute the infinite horizon optimal cost and control law for the unconstrained system.   
(b) Find the region $\mathbb { X } _ { f } ,$ , the maximal constraint admissible set using the algorithm in Exercise 2.5 for the system $x ^ { + } = ( A + B K ) x$ with constraints $x \in \mathbb { X }$ and $K x \in \mathbb { U }$ . You should obtain the region shown in Figure 2.8.   
(c) Add a terminal constraint $x ( N ) \in \mathbb { X } _ { f }$ and implement constrained MPC. Find $x _ { N }$ , the region of attraction for the MPC problem with $V _ { f } ( \cdot )$ as the terminal cost and $x ( N ) \in \mathbb { X } _ { f }$ as the terminal constraint. Contrast it with the region of attraction for the MPC problem in Exercise 2.6 with a terminal constraint $x ( N ) = 0$ .   
(d) Estimate ${ \bar { X } } _ { N }$ , the set of initial states for which the MPC control sequence for horizon N is equal to the MPC control sequence for an infinite horizon. Hint: $x \in { \bar { X } } _ { N }$ if and only if $x ^ { 0 } ( N ; x ) \in \operatorname { i n t } ( \mathbb { X } _ { f } )$ . Why?

in which $\mathbf { 0 } : = \{ 0 , 0 , 0 \}$ is the zero disturbance sequence. In this case, $J _ { 3 } ( x , \pmb { \mu } )$ is the nominal cost, i.e., the cost associated with the nominal system $x ^ { + } = x + u$ in which the disturbance is neglected. With this cost function, the solution to $\mathbb { P } _ { 3 } ^ { * } ( x )$ is the DP solution, obtained previously, to the deterministic nominal optimal control problem.

![](image/65a64b1ab64d23293cc692a77a7a62e7a31cd92d6d7f7078ca522006eab8bce9.jpg)

<details>
<summary>text_image</summary>

x¹
X₁
X⁰
X₂
X₃
0
1
2
k
3
x²
-2
</details>

(a) Open-loop trajectories.

![](image/8058196b75c93876b2c362737893857ba51ba4249d2e00c7bb1839a9e4c16505.jpg)

<details>
<summary>line</summary>

| k | x¹ | x² | x⁰ |
| --- | --- | --- | --- |
| 0 | 1.0 | 1.0 | 1.0 |
| 1 | 1.5 | -1.0 | 0.5 |
| 2 | 1.8 | -1.5 | 0.3 |
| 3 | 2.0 | -2.0 | 0.2 |
</details>

(b) Feedback trajectories.   
Figure 3.1: Open-loop and feedback trajectories.

We now compare two solutions to $\mathbb { P } _ { 3 } ( x )$ : the open-loop solution in which M is restricted to be the set of control sequences, and the feedback solution in which M is the class of admissible policies. The solution to the first problem is the solution to the deterministic problem discussed previously; the optimal control sequence is

$$\mathbf {u} ^ {0} (x) = \{- (8 / 1 3) x, - (3 / 1 3) x, - (1 / 1 3) x \}$$

in which x is the initial state at time 0. The solution to the second problem is the sequence of control laws determined previously, also for the deterministic problem, using dynamic programming; the optimal policy is $\pmb { \mu } ^ { 0 } = \{ \mu _ { 0 } ^ { 0 } ( \cdot ) , \mu _ { 1 } ^ { 0 } ( \cdot ) , \mu _ { 2 } ( \cdot ) \}$ } where the control laws (functions) $\mu _ { i } ( \cdot ) , i = 0 , 1 , 2$ , are defined by

$$
\begin{array}{l} \mu_ {0} ^ {0} (x) := \kappa_ {3} ^ {0} (x) = - (8 / 1 3) x \quad \forall x \in \mathbb {R} \\ \mu_ {1} ^ {0} (x) := \kappa_ {2} ^ {0} (x) = - (3 / 5) x \quad \forall x \in \mathbb {R} \\ \mu_ {2} ^ {0} (x) := \kappa_ {1} ^ {0} (x) = - (1 / 2) x \quad \forall x \in \mathbb {R} \\ \end{array}
$$

The two solutions, $\mathbf { u } ^ { 0 } ( \cdot )$ and $\pmb { \mu } ^ { 0 }$ , when applied to the uncertain system $x ^ { + } = x + u + w$ do not yield the same trajectories for all disturbance sequences. This is illustrated in Figure 3.1 for the three disturbance sequences, $\mathbf { w } ^ { 0 } \ : = \ \{ 0 , 0 , 0 \} , \ \mathbf { w } ^ { 1 } \ : = \ \{ 1 , 1 , 1 \}$ , and $\mathbf { w } ^ { 2 } : = \{ - 1 , - 1 , - 1 \}$ ;

The set $\chi _ { j }$ may then be expressed as

$$\mathcal {X} _ {j} = \{x \in \mathbb {R} ^ {n} \mid \exists u \in \mathbb {R} ^ {m} \text { such that } (x, u) \in \mathcal {Z} _ {j} \}$$

i.e., $\chi _ { j }$ is the orthogonal projection of $\mathcal { Z } _ { j } \subseteq \mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$ onto $\mathbb { R } ^ { n }$ .

DP yields much more than an optimal control sequence for a given initial state; it yields an optimal feedback policy $\pmb { \mu } ^ { 0 }$ or sequence of control laws where

$$\boldsymbol {\mu} ^ {0} := \{\mu_ {0} (\cdot), \mu_ {1} (\cdot), \dots , \mu_ {N - 1} (\cdot) \} = \{\kappa_ {N} (\cdot), \kappa_ {N - 1} (\cdot), \dots , \kappa_ {1} (\cdot) \}$$

![](image/a971048bf240873997de4d380d795f4f3353d65601b81315b9de5d3f14550a83.jpg)

<details>
<summary>text_image</summary>

f^{-1}(X_{j-1})
Z_j
U
X_j
X
</details>

Figure 2.5: The sets $\mathcal { Z } _ { j }$ and $\chi _ { j }$ .

At event $( x , i )$ , i.e., at state x at time i, the time to go is $N - i$ and the optimal control is

$$\mu_ {i} ^ {0} (x) = \kappa_ {N - i} (x)$$

i.e., $\mu _ { i } ( \cdot )$ is the control law at time i. Consider an initial event $( x , 0 )$ , i.e., state x at time 0. If the terminal time (horizon) is N, the optimal control for (x, 0) is $\kappa _ { N } ( x )$ . The successor state, at time 1, is

$$x ^ {+} = f (x, \kappa_ {N} (x))$$

At event $( x ^ { + } , 1 )$ , the time to go to the terminal time is $N - 1$ and the optimal control is $\kappa _ { N - 1 } ( x ^ { + } ) = \kappa _ { N - 1 } ( f ( x , \kappa _ { N } ( x ) ) )$ . For a given initial event $( x , 0 )$ , the optimal policy generates the optimal state and control trajectories $\mathbf { x } ^ { 0 } ( x )$ and $\mathbf { u } ^ { 0 } ( x )$ that satisfy the difference equations

$$x (0) = x \quad u (0) = \kappa_ {N} (x) \tag {2.13}x (i + 1) = f (x (i), u (i)) \quad u (i) = \kappa_ {N - i} (x (i)) \tag {2.14}$$

for $i = 0 , 1 , \ldots , N - 1$ . These state and control trajectories are identical to those obtained, as in MPC, by solving $\mathbb { P } _ { N } ( x )$ directly for the particular initial event $( x , 0 )$ using a mathematical programming algorithm. Dynamic programming, however, provides a solution for any event $( x , i )$ such that $i \in \mathbb { I } _ { 0 : N - 1 }$ and $x \in { \mathcal { X } } _ { i }$ .

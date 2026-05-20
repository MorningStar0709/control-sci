# Exercise 2.6: Terminal constraint and region of attraction

Consider the system

$$x ^ {+} = A x + B u$$

subject to the constraints

$$x \in \mathbb {X} \qquad u \in \mathbb {U}$$

in which

$$
A = \left[ \begin{array}{c c} 2 & 1 \\ 0 & 2 \end{array} \right] \qquad B = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right]
\mathbb {X} = \{x \in \mathbb {R} ^ {2} \mid x _ {1} \leq 5 \} \quad \mathbb {U} = \{u \in \mathbb {R} ^ {2} \mid - \mathbf {1} \leq u \leq \mathbf {1} \}
$$

and $\mathbf { 1 } \in \mathbb { R } ^ { 2 }$ is a vector of ones. The MPC cost function is

$$V _ {N} (x, \mathbf {u}) = \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) + V _ {f} (x (N))$$

in which

$$
\ell (x, u) = (1 / 2) \big (| x | _ {Q} ^ {2} + | u | ^ {2} \big) \qquad Q = \left[ \begin{array}{c c} \alpha & 0 \\ 0 & \alpha \end{array} \right]
$$

and $V _ { f } ( \cdot )$ is the terminal penalty on the final state.

(a) Implement unconstrained MPC with no terminal cost $( V _ { f } ( \cdot ) = 0 )$ for a few values of α. Choose a value of α for which the resultant closed loop is unstable. Try $N = 3 .$ .

![](image/5a3ee12b768fefd2c006eea2b7b8a40ecdec44d2a6c4e0d3271c7f0e320a5030.jpg)

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

Figure 2.7: Region of attraction (shaded region) for constrained MPC controller of Exercise 2.6.

(b) Implement constrained MPC with no terminal cost or terminal constraint for the value of α obtained in the previous part. Is the resultant closed loop stable or unstable?   
(c) Implement constrained MPC with terminal equality constraint x(N) = 0 for the same value of α. Find the region of attraction for the constrained MPC controller using the projection algorithm from Exercise 2.4. The result should resemble Figure 2.7.

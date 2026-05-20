# Example 2.5: Linear quadratic MPC

Suppose the system is described by

$$x ^ {+} = f (x, u) := x + u$$

with initial state x. The stage cost and terminal cost are

$$\ell (x, u) := (1 / 2) \left(x ^ {2} + u ^ {2}\right) \quad V _ {f} (x) := (1 / 2) x ^ {2}$$

The control constraint is

$$\boldsymbol {u} \in [ - 1, 1 ]$$

and there are no state or terminal constraints. Suppose the horizon is $N = 2$ . Under the first approach, the decision variables are u and x, and the optimal control problem is minimization of

$$V _ {N} (x (0), x (1), x (2), u (0), u (1)) =(1 / 2) \left(x (0) ^ {2} + x (1) ^ {2} + x (2) ^ {2} + u (0) ^ {2} + u (1) ^ {2}\right)$$

with respect to $( x ( 0 ) , x ( 1 ) , x ( 2 ) )$ , and $( u ( 0 ) , u ( 1 ) )$ subject to the following constraints

$$x (0) = x \quad x (1) = x (0) + u (0) \quad x (2) = x (1) + u (1)u (0) \in [ - 1, 1 ] \quad u (1) \in [ - 1, 1 ]$$

The constraint $u \in [ - 1 , 1 ]$ is equivalent to two inequality constraints, $u \leq 1 \ \mathrm { a n d } \ - u \leq 1$ . The first three constraints are equality constraints enforcing satisfaction of the difference equation.

In the second approach, the decision variable is merely u because the first three constraints are automatically enforced by requiring x to be a solution of the difference equation. Hence, the optimal control problem becomes minimization with respect to $\mathbf { u } = ( u ( 0 ) ^ { \prime } , u ( 1 ) ) ^ { \prime }$ of

$$
\begin{array}{l} V _ {N} (x, \mathbf {u}) = (1 / 2) \left(x ^ {2} + (x + u (0)) ^ {2} + (x + u (0) + u (1)) ^ {2} + \right. \\ \left. \boldsymbol {u} (0) ^ {2} + \boldsymbol {u} (1) ^ {2}\right) \\ = (3 / 2) x ^ {2} + \left[ \begin{array}{c c} 2 x & x \end{array} \right] \mathbf {u} + (1 / 2) \mathbf {u} ^ {\prime} H \mathbf {u} \\ \end{array}
$$

![](image/7ad016c54f0d6ab5047a658051f8a0209091d3d0f8aae7d25679f56ecd3f92fe.jpg)

<details>
<summary>line</summary>

| x | u |
| --- | --- |
| -2 | 1.0 |
| -1 | 0.5 |
| 0 | 0.0 |
| 1 | -0.5 |
| 2 | -1.0 |
</details>

(a) Implicit MPC control law.

![](image/6b321a8d837052d04ee05b6b067df30a9765a982a80c0428976c48dd8dfefea2.jpg)

<details>
<summary>line</summary>

| k | x(k) | u(k) |
| --- | --- | --- |
| 0 | 10 | -1 |
| 2 | 9 | -1 |
| 4 | 8 | -1 |
| 6 | 7 | -1 |
| 8 | 6 | -1 |
| 10 | 5 | -0.5 |
| 12 | 4 | 0 |
| 14 | 3 | 0 |
</details>

(b) Trajectories of controlled system.   
Figure 2.1: Example of MPC.

in which

$$
H = \left[ \begin{array}{c c} 3 & 1 \\ 1 & 2 \end{array} \right]
$$

subject to the constraint $\mathbf { u } \in \mathcal { U } _ { N } ( x )$ where

$$\mathcal {U} _ {N} (x) = \{\mathbf {u} \mid | u (k) | \leq 1 k = 0, 1 \}$$

for some weighting matrix $W _ { x }$ . Hence the regulator problem can be posed as an optimal control problem with certain combined performance index on u and x. In this chapter, we shall be concerned exclusively with the $\mathcal { L } _ { 2 }$ performance problem or quadratic performance problem. Moreover, we shall focus on the infinite time regulator problem $( \mathrm { i . e . , } T  \infty )$ and, without loss of generality, we shall assume $t _ { 0 } = 0$ . In this case, our problem is as follows: Find a control $u ( t )$ defined on $[ 0 , \infty )$ such that the state $x ( t )$ is driven to the origin as $t \to \infty$ and the following performance index is minimized:

$$
\min _ {u} \int_ {0} ^ {\infty} \left[ \begin{array}{l} x (t) \\ u (t) \end{array} \right] ^ {*} \left[ \begin{array}{c c} Q & S \\ S ^ {*} & R \end{array} \right] \left[ \begin{array}{l} x (t) \\ u (t) \end{array} \right] d t \tag {13.2}
$$

for some $Q = Q ^ { * } , S ,$ and $R = R ^ { * } > 0$ . This problem is traditionally called a linear quadratic regulator problem or, simply, an LQR problem. Here we have assumed $R > 0$ to emphasize that the control energy has to be finite $( \mathrm { i . e . , } u ( t ) \in \mathcal { L } _ { 2 } [ 0 , \infty ) )$ . So $\mathcal { L } _ { 2 } [ 0 , \infty )$ is the space over which the integral is minimized. Moreover, it is also generally assumed that

$$
\left[ \begin{array}{c c} Q & S \\ S ^ {*} & R \end{array} \right] \geq 0. \tag {13.3}
$$

Since R is positive definite, it has a square root, $R ^ { 1 / 2 }$ , which is also positive-definite. $\mathrm { B y }$ the substitution

$$u \leftarrow R ^ {1 / 2} u,$$

we may as well assume at the start that $R = I .$ In fact, we can even assume $S = 0$ by using a pre-state feedback $u = - S ^ { * } x + v$ provided some care is exercised; however, this will not be assumed in the sequel. Since the matrix in equation (13.3) is positive semi-definite with $R = I ,$ , it can be factored as

$$
\left[ \begin{array}{l l} Q & S \\ S ^ {*} & I \end{array} \right] = \left[ \begin{array}{l} C _ {1} ^ {*} \\ D _ {1 2} ^ {*} \end{array} \right] \left[ \begin{array}{l l} C _ {1} & D _ {1 2} \end{array} \right].
$$

Then equation (13.2) can be rewritten as

$$\min _ {u \in \mathcal {L} _ {2} [ 0, \infty)} \| C _ {1} x + D _ {1 2} u \| _ {2} ^ {2}.$$

In fact, the LQR problem is posed traditionally as the minimization problem:

$$\min _ {u \in \mathcal {L} _ {2} [ 0, \infty)} \| C _ {1} x + D _ {1 2} u \| _ {2} ^ {2} \tag {13.4}\text { subject to: } \dot {x} = A x + B u, x (0) = x _ {0} \tag {13.5}$$

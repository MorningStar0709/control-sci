# Exercise 6.15: Optimizing one variable at a time

Consider the positive definite quadratic function partitioned into two sets of variables

$$
V (u) = (1 / 2) u ^ {\prime} H u + c ^ {\prime} u + d
V (u _ {1}, u _ {2}) = (1 / 2) \left[ \begin{array}{c c} u _ {1} ^ {\prime} & u _ {2} ^ {\prime} \end{array} \right] \left[ \begin{array}{c c} H _ {1 1} & H _ {1 2} \\ H _ {2 1} & H _ {2 2} \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] + \left[ \begin{array}{c c} c _ {1} ^ {\prime} & c _ {2} ^ {\prime} \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] + d
$$

in which $H > 0$ . Imagine we wish to optimize this function by first optimizing over the $_ { u _ { 1 } }$ variables holding $u _ { 2 }$ fixed and then optimizing over the $u _ { 2 }$ variables holding u1 fixed as shown in Figure 6.8. Let’s see if this procedure, while not necessarily efficient, is guaranteed to converge to the optimum.

(a) Given an initial point $( u _ { 1 } ^ { p } , u _ { 2 } ^ { p } )$ ), show that the next iteration is

$$u _ {1} ^ {p + 1} = - H _ {1 1} ^ {- 1} \left(H _ {1 2} u _ {2} ^ {p} + c _ {1}\right)u _ {2} ^ {p + 1} = - H _ {2 2} ^ {- 1} \left(H _ {2 1} u _ {1} ^ {p} + c _ {2}\right) \tag {6.29}$$

The procedure can be summarized as

$$u ^ {p + 1} = A u ^ {p} + b \tag {6.30}$$

in which the iteration matrix A and constant b are given by

$$
A = \left[ \begin{array}{c c} 0 & - H _ {1 1} ^ {- 1} H _ {1 2} \\ - H _ {2 2} ^ {- 1} H _ {2 1} & 0 \end{array} \right] \quad b = \left[ \begin{array}{c} - H _ {1 1} ^ {- 1} c _ {1} \\ - H _ {2 2} ^ {- 1} c _ {2} \end{array} \right] \tag {6.31}
$$

(b) Establish that the optimization procedure converges by showing the iteration matrix is stable

$$\left| \operatorname{eig} (A) \right| < 1$$

(c) Given that the iteration converges, show that it produces the same solution as

$$u ^ {*} = - H ^ {- 1} c$$

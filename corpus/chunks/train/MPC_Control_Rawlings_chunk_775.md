# Example 7.11: Parametric QP

Consider the example in Section 7.2. This may be expressed as

$$V ^ {0} (x) = \min _ {u} V (x, u), \quad V (x, u) := \{(1 / 2) x ^ {2} - u x + u ^ {2} \mid M u \leq N x + p \}$$

where

$$
M = \left[ \begin{array}{c} - 1 \\ - 1 \\ - 1 \end{array} \right], \quad N = \left[ \begin{array}{c} 0 \\ 1 / 2 \\ 1 \end{array} \right], \quad p = \left[ \begin{array}{c} - 1 \\ - 2 \\ - 2 \end{array} \right]
$$

At $x = 1 , u ^ { 0 } ( x ) = 3 / 2$ and $I ^ { 0 } ( x ) ~ = ~ \{ 2 \}$ . The equality constrained optimization problem $\mathbb { P } _ { x } ( \boldsymbol { w } )$ is

$$V _ {x} ^ {0} (w) = \min _ {u} \{(1 / 2) w ^ {2} - u w + u ^ {2} \mid - u = (1 / 2) w - 2 \}$$

so that $u ^ { 0 } ( w ) = 2 - w / 2$ . Hence

$$
R _ {x} ^ {0} := \left\{w   \Big | \begin{array}{c} M u _ {x} ^ {0} (w) \leq N w + p (w) \\ - \nabla_ {u} V (w, u _ {x} ^ {0} (w)) \in C ^ {*} (x, u ^ {0} (x)) \end{array} \right\}
$$

$\begin{array} { r l } & { \mathrm { S i n c e ~ } M _ { 2 } = - 1 , C ^ { * } ( x ) = \mathrm { c o n e } \{ M _ { i } ^ { \prime } \mid i \in I ^ { 0 } ( x ) \} = \mathrm { c o n e } \{ M _ { 2 } ^ { \prime } \} = \{ h \in \mathbb { R } \mid 0 \} } \\ & { h \leq 0 \} ; \mathrm { a l s o } } \end{array}$

$$\nabla_ {u} V (w, u _ {x} ^ {0} (w)) = - w + 2 u ^ {0} (w) = - w + 2 (2 - w / 2) = - 2 w + 4$$

so that $R _ { x } ^ { 0 }$ is defined by the following inequalities:

$$
\begin{array}{l} (1 / 2) w - 2 \leq - 1 \quad \text { or } w \leq 2 \\ (1 / 2) w - 2 \leq (1 / 2) w - 2 \text {   or   } w \in \mathbb {R} \\ (1 / 2) w - 2 \leq w - 2 \quad \text { or } w \geq 0 \\ 2 w - 4 \leq 0 \quad \text { or } w \leq 2 \\ \end{array}
$$

which reduces to $w \in [ 0 , 2 ]$ so $R _ { x } ^ { 0 } = [ 0 , 2 ]$ when $x = 1 ; [ 0 , 2 ]$ is the set $X _ { 2 }$ determined in Section 7.2. -

# 3.1 Introduction

The optimal control problem, with horizon N = 3, is

$$\mathbb {P} _ {3} (x): \quad V _ {3} ^ {0} (x) = \min _ {\mathbf {u} _ {3}} V _ {3} (x, \mathbf {u})$$

in which u = {u(0), u(1), u(2)}

$$V _ {3} (x, \mathbf {u}) := (1 / 2) \sum_ {i = 0} ^ {2} [ (x (i) ^ {2} + u (i) ^ {2}) ] + (1 / 2) x (3) ^ {2}$$

where, for each $i , x ( i ) = \phi ( i ; x , { \mathbf { u } } ) = x + u ( 0 ) + u ( 1 ) + \ldots + u ( i -$ 1), the solution of the difference equation $x ^ { + } ~ = ~ x + u$ at time i if the initial state is $x ( 0 ) = x$ and the control (input) sequence is ${ \textbf { u } } =$ $\{ u ( 0 ) , u ( 1 ) , u ( 2 ) \}$ ; in matrix operations u is taken to be the column vector $[ u ( 0 ) , u ( 1 ) , u ( 2 ) ] ^ { \prime }$ . Thus

$$
\begin{array}{l} V _ {3} (x, \mathbf {u}) = (1 / 2) \left[ x ^ {2} + (x + u (0)) ^ {2} + (x + u (0) + u (1)) ^ {2} + \right. \\ \left. (x + u (0) + u (1) + u (2)) ^ {2} + u (0) ^ {2} + u (1) ^ {2} + u (2) ^ {2} \right] \\ = (3 / 2) x ^ {2} + x \left[ \begin{array}{c c c} 3 & 2 & 1 \end{array} \right] \mathbf {u} + (1 / 2) \mathbf {u} ^ {\prime} P _ {3} \mathbf {u} \\ \end{array}
$$

in which

$$
P _ {3} = \left[ \begin{array}{l l l} 4 & 2 & 1 \\ 2 & 3 & 1 \\ 1 & 1 & 2 \end{array} \right]
$$

The vector form of the optimal open-loop control sequence for an initial state of x is, therefore,

$$
\mathbf {u} ^ {0} (x) = - P _ {3} ^ {- 1} \left[ \begin{array}{c c c} 3 & 2 & 1 \end{array} \right] ^ {\prime} x = - \left[ \begin{array}{c c c} 0. 6 1 5 & 0. 2 3 1 & 0. 0 7 7 \end{array} \right] ^ {\prime} x
$$

The optimal control and state sequences are, therefore,

$$\mathbf {u} ^ {0} (x) = \{- 0. 6 1 5 x, - 0. 2 3 1 x, - 0. 0 7 7 x \}\mathbf {x} ^ {0} (x) = \{x, 0. 3 8 5 x, 0. 1 5 4 x, 0. 0 7 7 x \}$$

To compute the optimal feedback control, we use the DP recursions

$$V _ {i} ^ {0} (x) = \min _ {u \in \mathbb {R}} \{x ^ {2} / 2 + u ^ {2} / 2 + V _ {i - 1} ^ {0} (x + u) \}\kappa_ {i} ^ {0} (x) = \arg \min _ {u \in \mathbb {R}} \{x ^ {2} / 2 + u ^ {2} / 2 + V _ {i - 1} ^ {0} (x + u) \}$$

with boundary condition

$$V _ {0} ^ {0} (x) = (1 / 2) x ^ {2}$$

This procedure gives the value function $V _ { i } ^ { 0 } ( \cdot )$ and the optimal control law $\kappa _ { i } ^ { 0 } ( \cdot )$ at each i where the subscript i denotes time to go. Solving the DP recursion, for all $x \in \mathbb { R }$ , all $i \in \{ 1 , 2 , 3 \}$ , yields

$$
\begin{array}{l} V _ {1} ^ {0} (x) = (3 / 4) x ^ {2} \quad \kappa_ {1} ^ {0} (x) = - (1 / 2) x \\ V _ {2} ^ {0} (x) = (4 / 5) x ^ {2} \quad \kappa_ {2} ^ {0} (x) = - (3 / 5) x \\ V _ {3} ^ {0} (x) = (2 1 / 2 6) x ^ {2} \quad \kappa_ {3} ^ {0} (x) = - (8 / 1 3) x \\ \end{array}
$$

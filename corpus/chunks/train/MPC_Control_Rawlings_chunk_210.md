for some $\lambda > 0 ;$ this is a standard condition of optimality. Since ${ \bf u } =$ $[ - 1 \textit { } \upsilon ] ^ { \prime }$ for some $\nu \in [ - 1 , 1 ]$ and since $\nabla _ { \bf u } V ( x , { \bf u } ) = H ( { \bf u } - a ( x ) ) =$ $H \mathbf { u } + c ( x )$ , the condition of optimality is

$$
\left[ \begin{array}{c c} 3 & 1 \\ 1 & 2 \end{array} \right] \left[ \begin{array}{c} - 1 \\ v \end{array} \right] + \left[ \begin{array}{c} 2 \\ 1 \end{array} \right] x - \left[ \begin{array}{c} \lambda \\ 0 \end{array} \right] = \left[ \begin{array}{c} 0 \\ 0 \end{array} \right]
$$

or

$$
\begin{array}{l} - 3 + \nu + 2 x - \lambda = 0 \\ - 1 + 2 \nu + x = 0 \\ \end{array}
$$

which, when solved, yields $\nu = ( 1 / 2 ) - ( 1 / 2 ) x \mathrm { a n d } \lambda = - ( 5 / 2 ) + ( 3 / 2 ) x$ . Hence,

$$
\mathbf {u} ^ {0} (x) = b _ {2} + K _ {2} x \qquad b _ {2} = \left[ \begin{array}{c} - 1 \\ (1 / 2) \end{array} \right] \qquad K _ {2} = \left[ \begin{array}{c} 0 \\ - (1 / 2) \end{array} \right]
$$

for all $x \in \mathbb { X } _ { 2 } = [ x _ { c 1 } , x _ { c 2 } ]$ where $x _ { c 2 } = 3$ since $\mathbf { u } ^ { 0 } ( x ) \in \mathcal { U } _ { 2 }$ for all x in this range. For all $x \in \mathbb { X } _ { 3 } = [ x _ { c _ { 2 } } , \infty ) , \mathbf { u } ^ { 0 } ( x ) = ( - 1 , - 1 ) ^ { \prime }$ . Summarizing:

$$x \in [ 0, (5 / 3) ] \implies \mathbf {u} ^ {0} (x) = K _ {1} xx \in [ (5 / 3), 3 ] \Rightarrow \mathbf {u} ^ {0} (x) = K _ {2} x + b _ {2}x \in [ 3, \infty) \implies \mathbf {u} ^ {0} (x) = b _ {3}$$

in which

$$
K _ {1} = \left[ \begin{array}{c} - (3 / 5) \\ - (1 / 5) \end{array} \right] \quad K _ {2} = \left[ \begin{array}{c} 0 \\ - (1 / 2) \end{array} \right] \quad b _ {2} = \left[ \begin{array}{c} - 1 \\ (1 / 2) \end{array} \right] \quad b _ {3} = \left[ \begin{array}{c} - 1 \\ - 1 \end{array} \right]
$$

The optimal control for $x \le 0$ may be obtained by symmetry; ${ \bf u } ^ { 0 } ( - x ) =$ $- \mathbf { u } ^ { 0 } ( x )$ for all $x \geq 0$ so that:

$$x \in [ 0, - (5 / 3) ] \Rightarrow \mathbf {u} ^ {0} (x) = - K _ {1} xx \in [ - (5 / 3), - 3 ] \implies \mathbf {u} ^ {0} (x) = - K _ {2} x - b _ {2}x \in [ - 3, - \infty) \implies \mathbf {u} ^ {0} (x) = - b _ {3}$$

It is easily checked that $\mathbf { u } ^ { 0 } ( \cdot )$ is continuous and satisfies the constraint for all $x \in \mathbb { R }$ . The MPC control law $\kappa _ { N } ( \cdot )$ is the first component of $ { \mathbf { u } } ^ { 0 } ( \cdot )$ and, therefore, is defined by:

$$\kappa_ {N} (x) = 1 \quad x \leq - 3\kappa_ {N} (x) = 1 \quad x \in [ - (5 / 3), - 3 ]\kappa_ {N} (x) = - (3 / 5) x \quad x \in [ - (5 / 3), (5 / 3) ]\kappa_ {N} (x) = - 1 \quad x \in [ (5 / 3), 3 ]\kappa_ {N} (x) = - 1 \quad x \geq 3$$

# Example 7.12: Explicit optimal control

We return to the MPC problem presented in Example 2.5 of Chapter 2

$$
\begin{array}{l} V ^ {0} (x, \mathbf {u}) = \min _ {\mathbf {u}} \{V (x, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} \} \\ V (x, \mathbf {u}) := (3 / 2) x ^ {2} + [ 2 x, x ] \mathbf {u} + (1 / 2) \mathbf {u} ^ {\prime} H \mathbf {u} \\ H := \left[ \begin{array}{c c} 3 & 1 \\ 1 & 2 \end{array} \right] \\ \mathcal {U} := \{\mathbf {u} \mid M \mathbf {u} \leq p \} \\ \end{array}
$$

where

$$
M := \left[ \begin{array}{c c} 1 & 0 \\ - 1 & 0 \\ 0 & 1 \\ 0 & - 1 \end{array} \right], \qquad p := \left[ \begin{array}{c} 1 \\ 1 \\ 1 \\ 1 \end{array} \right]
$$

It follows from the solution to Example 2.5 that

$$
u ^ {0} (2) = \left[ \begin{array}{c} - 1 \\ - (1 / 2) \end{array} \right]
$$

and $I ^ { 0 } ( x ) ~ = ~ \{ 2 \}$ . The equality constrained optimization problem at $x = 2$ is

$$V _ {x} ^ {0} (w) = \min _ {\mathbf {u}} \{(3 / 2) w ^ {2} + 2 w u _ {1} + w u _ {2} + (1 / 2) \mathbf {u} ^ {\prime} H \mathbf {u} \mid u _ {1} = - 1 \}$$

so that

$$
u _ {x} ^ {0} (w) = \left[ \begin{array}{c} - 1 \\ (1 / 2) - (1 / 2) w \end{array} \right]
$$

Hence $u _ { x } ^ { 0 } ( 2 ) = \left[ - 1 , - 1 / 2 \right] ^ { \prime } = u ^ { 0 } ( 2 )$ as expected. Since $M _ { x } ^ { 0 } = M _ { 2 } =$ $[ - 1 , 0 ] , C ^ { * } ( x , u ^ { 0 } ( x ) ) = \{ g \in \mathbb { R } ^ { 2 } \mid g _ { 1 } \leq 0 \}$ . Also

$$
\nabla_ {\mathbf {u}} V (w, \mathbf {u}) = \left[ \begin{array}{c} 2 w + 3 u _ {1} + u _ {2} \\ w + u _ {1} + 2 u _ {2} \end{array} \right]
$$

so that

$$
\nabla_ {\mathbf {u}} V (w, \mathbf {u} _ {x} ^ {0} (w)) = \left[ \begin{array}{c} (3 / 2) w - (5 / 2) \\ 0 \end{array} \right]
$$

Hence $R _ { x } ^ { 0 } , x = 2$ is the set of w satisfying the following inequalities

$$
\begin{array}{l} (1 / 2) - (1 / 2) w \leq 1 \quad \text {or} w \geq - 1 \\ (1 / 2) - (1 / 2) w \geq - 1 \text {or} w \leq 3 \\ - (3 / 2) w + (5 / 2) \leq 0 \quad \text { or } w \geq (5 / 3) \\ \end{array}
$$

which reduces to $w \in [ 5 / 3 , 3 ]$ ; hence $R _ { x } ^ { 0 } \ = \ [ 5 / 3 , 3 ]$ when $x \ = \ 2$ as shown in Example 2.5.

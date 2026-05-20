# Exercise 2.4: Computing the projection of Z onto $x _ { N }$

Given a polytope

$$\mathbb {Z} := \{(x, u) \in \mathbb {R} ^ {n} \times \mathbb {R} ^ {m} \mid G x + H u \leq \psi \}$$

write an Octave or MATLAB program to determine X, the projection of Z onto $\mathbb { R } ^ { n }$

$$\mathcal {X} = \{x \in \mathbb {R} ^ {n} \mid \exists u \in \mathbb {R} ^ {m} \text { such that } (x, u) \in \mathbb {Z} \}$$

Use algorithms 3.1 and 3.2 in Keerthi and Gilbert (1987).

To check your program, consider a system

$$
x ^ {+} = \left[ \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right] x + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u
$$

subject to the constraints $\mathbb { X } = \{ x \mid x _ { 1 } \leq 2 \}$ and $\mathbb { U } = \{ u \mid - 1 \leq u \leq 1 \}$ . Consider the MPC problem with $N = 2 , { \mathbf u } = ( u ( 0 ) , u ( 1 ) )$ , and the set Z given by

$$\mathbb {Z} = \{(x, \mathbf {u}) \mid x, \phi (1; x, \mathbf {u}), \phi (2; x, \mathbf {u}) \in \mathbb {X} \text { and } u (0), u (1) \in \mathbb {U} \}$$

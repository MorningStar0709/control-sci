Since $\phi ( 1 ; x , u ( 0 ) ) = f ( x , u ( 0 ) )$ , the function $( x , u ( 0 ) ) \mapsto \phi ( 1 ; x , u ( 0 ) )$ is continuous. Suppose the function $( x , \mathbf { u } _ { j - 1 } ) \mapsto \phi ( j ; x , \mathbf { u } _ { j - 1 } )$ is continuous and consider the function $( x , \mathbf { u } _ { j } ) \mapsto \phi ( j + 1 ; x , \mathbf { u } _ { j } )$ . Since

$$\phi (j + 1; x, \mathbf {u} _ {j}) = f (\phi (j; x, \mathbf {u} _ {j - 1}), u (j))$$

where $f ( \cdot )$ and $\phi ( j ; \cdot )$ are continuous and since $\phi ( j + 1 ; \cdot )$ is the composition of two continuous functions $f ( \cdot )$ and $\phi ( j ; \cdot \cdot )$ , it follows that $\phi ( j + 1 ; \cdot )$ is continuous. By induction $\phi ( k ; \cdot )$ is continuous for any positive integer k. 

The system (2.1) is subject to hard constraints which may take the form

$$u (k) \in \mathbb {U} \quad x (k) \in \mathbb {X} \quad \text { for all } k \in \mathbb {I} _ {\geq 0} \tag {2.2}$$

The constraint (2.2) does not couple $u ( k )$ or $x ( k )$ at different times; constraints that involve the control at several times are avoided by introducing extra states. Thus the common rate constraint $| u ( k ) - $ $u ( k - 1 ) | \leq c$ may be expressed as $| u ( k ) - z ( k ) | \leq c$ where z is an extra state variable satisfying the difference equation $z ^ { + } = u$ so that $z ( k ) = u ( k { - } 1 )$ . The constraint $| u - z | \leq c$ is an example of a mixed constraint, i.e., a constraint that involves both states and controls. Hence, a more general constraint formulation of the form

$$\mathcal {Y} (k) \in \mathbb {Y} \quad \text { for all } k \in \mathbb {I} _ {\geq 0} \tag {2.3}$$

in which the output y satisfies

$$y = h (x, u)$$

is sometimes required. A mixed constraint often is expressed in the form $F x + E u \le e$ , and may be regarded as a state dependent control constraint. Because the constraint (2.3) is more general, the constraint (2.2) may be expressed as $y ( k ) \in \mathbb { V }$ by an appropriate choice of the output function $h ( \cdot )$ and the output constraint set $\mathbb { Y } \left( y \right) = \left( x , u \right)$ and $\mathbb { Y } = \mathbb { X } \times \mathbb { U } )$ . We assume in this chapter that the state x is known; if the state x is estimated, uncertainty (state estimation error) is introduced and robust MPC, discussed in Chapter 3, is required.

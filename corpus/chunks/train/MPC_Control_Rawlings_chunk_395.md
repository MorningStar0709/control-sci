To analyze stability of the closed-loop system, we have to consider, since the controller is a dynamic system with state z, the composite system whose state is $( x , z )$ or the equivalent system whose state is $( e , z )$ . Since $( e , z )$ and $( x , z )$ are related by an invertible transformation

$$
\left[ \begin{array}{c} e \\ z \end{array} \right] = T \left[ \begin{array}{c} x \\ z \end{array} \right] \qquad T := \left[ \begin{array}{c c} I & - I \\ 0 & I \end{array} \right]
$$

the two systems are equivalent. The composite system whose state is $( x , z )$ satisfies, as shown previously

$$x ^ {+} = A x + B \kappa_ {N} (x, z) + w \tag {3.29}z ^ {+} = A z + B \bar {\kappa} _ {N} (z) \tag {3.30}$$

with initial state $( x ( 0 ) , z ( 0 ) ) = ( x , x )$ whereas the composite system whose state is $( e , z ) , e : = x - z$ , satisfies

$$e ^ {+} = A _ {K} e + w \tag {3.31}z ^ {+} = A z + B \bar {\kappa} _ {N} (z) \tag {3.32}$$

with initial state $( e ( 0 ) , z ( 0 ) ) \ = \ ( 0 , x )$ . The latter system is easier to analyze. So one way to proceed is to establish exponential stability of $S _ { K } ( \infty ) \times \{ 0 \}$ with region of attraction $S _ { K } ( \infty ) \times \mathcal { Z } _ { N }$ of the composite system described by (3.31) and (3.32); we leave this as Exercise 3.6.

Instead we consider the original system described by (3.29) and (3.30). We know, from the discussion above, that $e ( i ) ~ \in ~ S _ { K } ( \infty ) ~ \subseteq ~ S$ and $x ( i ) \in \{ z ( i ) \} \oplus S _ { K } ( \infty ) \subseteq \{ z ( i ) \} \oplus$ S for all $k \in \mathbb { I } _ { \geq 0 }$ if $e ( 0 ) \in S _ { K } ( \infty )$ , and K is such that $A _ { K }$ is stable. Also, we know from Chapter 2 that if the stability Assumptions 2.12 and 2.13 are satisfied for the nominal optimal control problem $\bar { \mathbb { P } } _ { N } ( z )$ , then the value function $\bar { V } _ { N } ^ { 0 } ( \cdot )$ satisfies

$$\bar {V} _ {N} ^ {0} (z) \geq \ell (z, \bar {\kappa} _ {N} (z)) \quad \forall z \in \mathcal {Z} _ {N} \tag {3.33}\Delta \bar {V} _ {N} ^ {0} (z) \leq - \ell (z, \bar {\kappa} _ {N} (z)) \quad \forall z \in \mathcal {Z} _ {N} \tag {3.34}\bar {V} _ {N} ^ {0} (z) \leq V _ {f} (z) \quad \forall z \in \mathbb {Z} _ {f} \tag {3.35}$$

in which $\Delta \bar { V } _ { N } ^ { 0 } ( z ) = \bar { V } _ { N } ^ { 0 } ( z ^ { + } ) - \bar { V } _ { N } ^ { 0 } ( z )$ with $z ^ { + } = A z + B \bar { \kappa } _ { N } ( z )$ .

# 3.4.4 Improved Tube-Based MPC of Linear Systems with Additive Disturbances

In this section we describe a version of the tube-based model predictive controller that has pleasing theoretical properties and that does not require computation of a nominal trajectory. It is, however, more difficult to implement since it requires knowledge of $S _ { K } ( \infty )$ or of a robust positive invariant outer approximation S. This section should therefore be omitted by readers interested only in easily implementable controllers.

We omitted, in Section 3.4.3, to make use of an additional degree of freedom available to the controller, namely $z ( 0 )$ , the initial state of the nominal system. Previously we set $z ( 0 ) = x ( 0 ) = x$ . It follows from the discussion at the end of Section 3.4.3 that every trajectory of the system $x ^ { + } = A x + B \nu + B K e + w$ emanating from an initial state x lies in the tube $X ( z , \mathbf { v } )$ , provided that the initial state x of the closed-loop system and the initial state z of the nominal system satisfy

$$x \in \{z \} \oplus S$$

in which S is either $S _ { K } ( \infty )$ or a robust positive invariant set for $e ^ { + } = { }$ $A _ { K } e + { w }$ that is an outer approximation of $S _ { K } ( \infty )$ . So, we may optimize the choice of the initial state z of the nominal system, provided we satisfy the constraints $x \in \{ z \} \oplus S$ and $z \in \mathbb { Z }$ . But we can go further. We can optimize the choice of z at every time i because, if the current state x of the closed-loop system and the current state z of the nominal system satisfy $x \in \{ z \} \oplus S$ , and the input to the system being controlled is $\nu + K ( x - z )$ where v is the input to the nominal system, then the subsequent states $x ^ { + }$ and $z ^ { + }$ satisfy $x ^ { + } \in \{ z ^ { + } \}$ ⊕ S. To this end, we define a new finite horizon optimal control problem $\mathbb { P } _ { N } ^ { * } ( x )$ , to be solved online, that reduces the cost $\bar { V } _ { N } ^ { 0 } ( z )$ obtained in Section 3.4.3

$$
\begin{array}{l} \mathbb {P} _ {N} ^ {*} (x): V _ {N} ^ {*} (x) = \min _ {z} \{\bar {V} _ {N} ^ {0} (z) \mid x \in \{z \} \oplus S, z \in \mathbb {Z} \} \\ = \min _ {\mathbf {v}, z} \{\bar {V} _ {N} (z, \mathbf {v}) \mid \mathbf {v} \in \mathcal {V} _ {N} (z), x \in \{z \} \oplus S, z \in \mathbb {Z} \} \\ \end{array}
$$

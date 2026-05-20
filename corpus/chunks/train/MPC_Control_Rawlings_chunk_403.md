Because of the extra freedom provided by varying z, the domain of the value function $V _ { N } ^ { * } ( \cdot )$ is $\mathcal { X } _ { N } : = \mathcal { Z } _ { N }$ ⊕ S where $\mathcal { Z } _ { N }$ is the domain of $\bar { V } _ { N } ^ { 0 } ( \cdot )$ . The solution to problem $\mathbb { P } _ { N } ^ { * } ( x )$ is $z ^ { * } ( x )$ and $\mathbf { v } ^ { * } ( x ) = \mathbf { v } ^ { 0 } ( z ^ { * } ( x ) ) ;$ ; optimizing with respect to z means that z in $\bar { \mathbb { P } } _ { N } ( z )$ is replaced by $z ^ { * } ( x )$ . It follows that

$$V _ {N} ^ {*} (x) = \bar {V} _ {N} ^ {0} (z ^ {*} (x)) \tag {3.39}$$

for all $x \in \mathcal { X } _ { N }$ . The control applied to the system $x ^ { + } = A x + B u + w$ at state x is $\kappa _ { N } ( { \boldsymbol { x } } )$ defined by

$$\kappa_ {N} (x) := \kappa_ {N} ^ {*} (x) + K (x - z ^ {*} (x))$$

in which $\kappa _ { N } ^ { * } ( x ) = \bar { \kappa } _ { N } ( z ^ { * } ( x ) )$ is the first element in the sequence $\mathbf { v } ^ { * } ( x ) =$ $\mathbf { v } ^ { 0 } ( z ^ { * } ( x ) )$ . The main change from the simple tube-based model predictive controller is that z is replaced by $z ^ { * } ( x )$ . A theoretical advantage is that the applied control $\kappa _ { N } ( x )$ depends only on the current state x and not on the composite state $( x , z )$ as in the simple controller.

It follows from (3.36), (3.37), (3.38) and (3.39) that the value function $V _ { N } ^ { * } ( \cdot )$ satisfies

$$V _ {N} ^ {*} (x) = \bar {V} _ {N} ^ {0} \left(z ^ {*} (x)\right) \geq c _ {1} \left| z ^ {*} (x) \right| ^ {2} \tag {3.40}V _ {N} ^ {*} (x) = \bar {V} _ {N} ^ {0} \left(z ^ {*} (x)\right) \leq c _ {2} \left| z ^ {*} (x) \right| ^ {2} \tag {3.41}\Delta V _ {N} ^ {*} (x, w) \leq \Delta \bar {V} _ {N} ^ {0} (z ^ {*} (x)) \leq - c _ {1} | z ^ {*} (x) | ^ {2} \tag {3.42}$$

for all $( x , w ) \in \mathcal { X } _ { N } \times \mathbb { W }$ in which the last line follows from the fact that

$$
\begin{array}{l} \Delta V _ {N} ^ {*} (x, w) := V _ {N} ^ {*} \left(x ^ {+}\right) - V _ {N} ^ {*} (x) = \bar {V} _ {N} ^ {0} \left(z ^ {*} \left(x ^ {+}\right)\right) - \bar {V} _ {N} ^ {0} \left(z ^ {*} (x)\right) \\ \leq \bar {V} _ {N} ^ {0} ((z ^ {*} (x)) ^ {+}) - \bar {V} _ {N} ^ {0} (z ^ {*} (x)) = \Delta \bar {V} _ {N} ^ {0} (z ^ {*} (x)) \leq - c _ {1} | z ^ {*} (x) | ^ {2} \\ \end{array}
$$

with $x ^ { + } = A x + B \kappa _ { N } ( x ) + w$ and $( z ^ { * } ( x ) ) ^ { + } = A z ^ { * } ( x ) + B \bar { \kappa } _ { N } ( z ^ { * } ( x ) )$ .

Next we note that

$$V _ {N} ^ {*} (x) = 0 \forall x \in S$$

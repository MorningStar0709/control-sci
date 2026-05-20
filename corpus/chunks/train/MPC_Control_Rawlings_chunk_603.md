It follows from Propositions 5.2 and 5.3, if Assumption 5.4 holds, that satisfaction of the constraints (5.21) and (5.22) by the nominal system ensures satisfaction of the constraints (5.10) by the original system. The nominal optimal control problem is, therefore,

$$\mathbb {P} _ {N} (z): \quad \bar {V} _ {N} ^ {0} (z) = \min _ {\mathbf {v}} \{\bar {V} _ {N} (z, \mathbf {v}) \mid \mathbf {v} \in \mathcal {V} _ {N} (z) \}$$

where the constraint set $\gamma _ { N } ( z )$ is defined by

$$\mathcal {V} _ {N} (z) := \{\mathbf {v} \mid v (k) \in \mathbb {V} \text { and } \bar {\phi} (k; z, \mathbf {v}) \in \mathbb {Z} \forall k \in \{0, 1, \dots , N - 1 \},\bar {\phi} (N; z, \mathbf {v}) \in \mathbb {Z} _ {f} \} \tag {5.23}$$

In (5.23), $\mathbb { Z } _ { f } \subseteq \mathbb { Z }$ is the terminal constraint set, and $\bar { \phi } ( k ; z , \mathbf { v } )$ denotes the solution of $z ^ { + } = A z + B \nu$ at time k if the initial state at time 0 is $z$ and the control sequence is $\mathbf { v } = \{ \nu ( 0 ) , \nu ( 1 ) , \dots , \nu ( N - 1 ) \}$ . Let $\mathbf { v } ^ { 0 } ( z )$ denote the minimizing control sequence; the stage cost $\ell ( \cdot )$ is chosen to ensure uniqueness of $\mathbf { v } ^ { 0 } ( z )$ . The implicit MPC control law for the nominal system is $\bar { \kappa } _ { N } ( \cdot )$ defined by

$$\bar {\kappa} _ {N} (z) := \nu^ {0} (0; z)$$

where $\upsilon ^ { 0 } ( 0 ; z )$ is the first element in the sequence $\mathbf { v } ^ { 0 } ( z )$ . The domain of $\bar { V } _ { N } ^ { 0 } ( \cdot )$ and $\mathbf { v } ^ { 0 } ( \cdot )$ , and, hence, of $\bar { \kappa } _ { N } ( \cdot )$ , is $\mathcal { Z } _ { N }$ defined by

$$\mathcal {Z} _ {N} := \{z \in \mathbb {Z} \mid \mathcal {V} _ {N} (z) \neq \emptyset \} \tag {5.24}$$

$\mathcal { Z } _ { N }$ is the set of initial states z that can be steered to $\mathbb { Z } _ { f }$ by an admissible control v that satisfies the state and control constraints, (5.21) and (5.22), and the terminal constraint. From (5.16), the implicit control law for the state estimator $\hat { x } ^ { + } = A \hat { x } + B u + \delta$ is $\kappa _ { N } ( \cdot )$ defined by

$$\kappa_ {N} (\hat {x}, z) := \bar {\kappa} _ {N} (z) + K (\hat {x} - z)$$

The controlled composite system with state $( \hat { x } , z )$ satisfies

$$\hat {x} ^ {+} = A \hat {x} + B \kappa_ {N} (\hat {x}, z) + \delta \tag {5.25}z ^ {+} = A z + B \bar {\kappa} _ {N} (z) \tag {5.26}$$

with initial state $( \hat { x } ( 0 ) , z ( 0 ) )$ satisfying $\hat { x } ( 0 ) \in \{ z ( 0 ) \} \oplus \mathbb { S } , z ( 0 ) \in \mathcal { Z } _ { N }$ . These constraints are satisfied if $z ( 0 ) = \hat { x } ( 0 ) \in \mathcal { Z } _ { N }$ . The control algorithm may be formally stated as follows:

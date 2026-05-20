MPC algorithm. The control objective is to steer the central state z to the target state $\bar { z } ( \hat { d } , \bar { r } )$ while satisfying the state and control constraints $x \in \mathbb { X }$ and $u \in \mathbb { V }$ . It is desirable that $z ( i )$ converges to $\bar { z } ( \hat { d } , \bar { r } )$ if $\hat { d }$ remains constant in which case $x ( i )$ converges to the set $\{ \bar { z } ( \hat { d } , \bar { r } ) \}$ ⊕Γ. To achieve this objective, we define the deterministic optimal control problem

$$\bar {\mathbb {P}} _ {N} (z, \hat {d}, \bar {r}): V _ {N} ^ {0} (z, \hat {d}, \bar {r}) := \min _ {\mathbf {v}} \{V _ {N} (z, \hat {d}, \bar {r}, \mathbf {v}) | \mathbf {v} \in \mathcal {V} _ {N} (z, \hat {d}, \bar {r}) \}$$

in which the cost $V _ { N } ( \cdot )$ and the constraint set $\mathcal { V } _ { N } ( z , \hat { d } , \bar { r } )$ are defined by

$$V _ {N} (z, \hat {d}, \bar {r}, \mathbf {v}) := \sum_ {i = 0} ^ {N - 1} \ell (z (i) - \bar {z} (\hat {d}, \bar {r}), v (i) - \bar {v} (\hat {d}, \bar {r})) + V _ {f} (z (N), \bar {z} (\hat {d}, \bar {r}))\mathcal {V} _ {N} (z, \hat {d}, \bar {r}) := \{\mathbf {v} \mid z (i) \in \mathbb {Z}, v (i) \in \mathbb {V} \forall i \in \mathbb {I} _ {0: N - 1}, z (N) \in \mathbb {Z} _ {f} (\bar {z} (\hat {d}, \bar {r})) \}$$

where, for each $i , z ( i ) = \bar { \phi } ( i ; z , \hat { d } , { \bf v } )$ , the solution of $z ^ { + } = A z + B _ { d } \hat { d } + B \nu$ when the initial state is z, the control sequence is $\mathbf { v } ,$ and the disturbance $\hat { d }$ is constant. The terminal cost is zero when the terminal state is equal to the target state and the target state lies in the center of the terminal constraint set. The solution to $\bar { \mathbb { P } } _ { N } ( z , \hat { d } , \bar { r } )$ is

$$\mathbf {v} ^ {0} (z, \hat {d}, \bar {r}) = \{\nu^ {0} (0; z, \hat {d}, \bar {r}), \nu^ {0} (1; z, \hat {d}, \bar {r}), \dots , \nu^ {0} (N - 1; z, \hat {d}, \bar {r}) \}$$

and the implicit model control law $\bar { \kappa } _ { N } ( \cdot )$ is defined by

$$\bar {\kappa} _ {N} (z, \hat {d}, \bar {r}) := v ^ {0} (0; z, \hat {d}, \bar {r})$$

where $\nu ^ { 0 } ( 0 ; z , \hat { d } , \bar { r } )$ is the first element in the sequence $\mathbf { v } ^ { 0 } ( z , \hat { d } , \bar { r } )$ . The control u applied to the plant and the observer is $u = \kappa _ { N } ( \hat { x } , z , \hat { d } , \bar { r } )$ where $\kappa _ { N } ( \cdot )$ is defined by

$$\kappa_ {N} (\hat {x}, z, \hat {d}, \bar {r}) := \bar {\kappa} _ {N} (z, \hat {d}, \bar {r}) + K (\hat {x} - z)$$

Although the optimal control problem $\bar { \mathbb { P } } _ { N } ( z , \hat { d } , \bar { r } )$ is deterministic, $\hat { d }$ is random, so that the sequence $\{ z ( i ) \}$ is random. The control algorithm may now be formally stated:

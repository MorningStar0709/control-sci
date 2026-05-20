In (3.26), $\mathbb { Z } _ { f } \subseteq \mathbb { Z }$ is the terminal constraint set. Solution of $\bar { \mathbb { P } } _ { N } ( z )$ yields the minimizing control sequence $\mathbf { v } ^ { 0 } ( z ) = \{ \nu ^ { 0 } ( 0 ; z ) , \nu ^ { 0 } ( 1 ; z ) , \ldots , \nu ^ { 0 } ( N -$ $1 ; z ) \}$ . The model predictive control applied to the nominal system at state $_ { z }$ is $\nu ^ { 0 } ( 0 ; z )$ , the first control action in the minimizing control sequence. The implicit nominal MPC control law is, therefore, $\bar { \kappa } _ { N } ( \cdot )$ , defined by

$$\bar {k} _ {N} (z) := \nu^ {0} (0; z)$$

Let $\mathcal { Z } _ { N }$ denote the domain of $\bar { V } _ { N } ^ { 0 } ( \cdot )$ , and of $\bar { \kappa } _ { N } ( \cdot )$ ,

$$\mathcal {Z} _ {N} := \{z \in \mathbb {Z} \mid \mathcal {V} _ {N} (z) \neq \emptyset \}$$

We propose to control the uncertain system $x ^ { + } = A x + B u + w$ by constraining it to lie in a tube whose center is the solution of the nominal system obtained using the implicit nominal MPC control law $\bar { \kappa } _ { N } ( \cdot )$ . The control applied to the system being controlled is $u = \kappa _ { N } ( x , z )$ in which $_ x$ is the current state of the system being controlled, $_ { z }$ is the current state of the nominal system, and $\kappa _ { N } ( \cdot )$ is defined by

$$\kappa_ {N} (x, z) := \bar {\kappa} _ {N} (z) + K (x - z)$$

The composite closed-loop system plus controller therefore satisfy

$$x ^ {+} = A x + B \kappa_ {N} (x, z) + w \tag {3.27}z ^ {+} = A z + B \bar {\kappa} _ {N} (z) \tag {3.28}$$

with initial state $( x , x )$ . The center of the tube is the sequence $\mathbf { z } =$ $\{ z ( 0 ) , z ( 1 ) , \ldots \}$ obtained by solving (3.28) with initial state $z ( 0 ) = x$ , i.e., for each $i \in \mathbb { I } _ { \ge 0 } , z ( i ) = \bar { \phi } ( i ; x , \bar { \kappa } _ { N } ( . ) )$ ). Since the difference equation $z ^ { + } = A z + B \bar { \kappa } _ { N } ( z )$ is autonomous, the solution z may be computed beforehand—at least up to a finite number of time steps. The control $u ( i )$ applied to the system at time i is, then

$$u (i) = \kappa_ {N} (x (i), z (i)) = v (i) + K [ x (i) - z (i) ]$$

in which $\nu ( i ) \ = \ \bar { \kappa } _ { N } ( z ( i ) )$ . The state sequence $\textbf { x } = \{ x ( 0 ) , x ( 1 ) , \ldots \}$ therefore satisfies

$$x (i + 1) = A x (i) + B \kappa_ {N} (x (i), z (i)) + w (i) \quad x (0) = x$$

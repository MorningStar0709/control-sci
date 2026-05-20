We suppose Assumption 3.14 holds in the sequel. An assumption like this is not uncommon in robust control; if W is too large, there is no possibility of satisfying the constraints for all realizations of the disturbance sequence w. Summarizing, the state and control constraints, $x ( i ) \in \mathbb { X }$ and $u ( i ) \in \mathbb { U }$ , are satisfied at each time i if the time-invariant control law $u = \nu + K ( x - z )$ , is employed, and the nominal system $z ^ { + } = A z + B \nu$ satisfies the tighter constraints

$$z (i) \in \mathbb {Z} := \mathbb {X} \ominus S \tag {3.23}\nu (i) \in \mathbb {V} := \mathbb {U} \ominus K S \tag {3.24}$$

for all relevant i and if, in addition,

$$x (0) \in \{z (0) \} \oplus S \quad e (0) \in S$$

in which S is robust positive invariant for $e ^ { + } \ = \ A _ { K } e \ + \ w , \ w \ \in \ \mathbb { W } .$ . Satisfaction of the state constraint at time N, i.e., satisfaction of $x ( N ) \in$ X, is ensured if the nominal system satisfies the terminal constraint

$$z (N) \in \mathbb {Z} _ {f} \quad \mathbb {Z} _ {f} \subseteq \mathbb {Z} \tag {3.25}$$

Tube-based robust predictive controller. The first requirement for the simple tube-based model predictive controller is a suitable nominal trajectory. To obtain this, we define a finite horizon optimal control $\bar { \mathbb { P } } _ { N } ( z )$ in which z is the current state of the nominal system. The optimal control problem is minimization of a cost function $\bar { V } _ { N } ( z , { \bf v } )$ in which

$$\bar {V} _ {N} (z, \mathbf {v}) := \sum_ {k = 0} ^ {N - 1} \ell (z (k), v (k)) + V _ {f} (z (N))$$

subject to satisfaction, by the state sequence $\mathbf { z } = \{ z ( 0 ) , z ( 1 ) , \ldots , z ( N ) \}$ and the control sequence $\mathbf { v } = \{ \nu ( 0 ) , \nu ( 1 ) , \ldots , \nu ( N - 1 ) \}$ , of the nominal difference equation $z ^ { + } = A z + B \nu$ and the constraints (3.23)–(3.25). The nominal optimal control problem is, therefore

$$\bar {\mathbb {P}} _ {N} (z): \quad \bar {V} _ {N} ^ {0} (z) = \min _ {\mathbf {v}} \{\bar {V} _ {N} (z, \mathbf {v}) \mid \mathbf {v} \in \mathcal {V} _ {N} (z) \}$$

in which the constraint set $\gamma _ { N } ( z )$ , which depends, as the notation implies, on the parameter $z ,$ is defined by

$$
\begin{array}{l} \mathcal {V} _ {N} (z) := \{\mathbf {v} \mid v (k) \in \mathbb {V}, \quad \bar {\phi} (k; z, \mathbf {v}) \in \mathbb {Z} \forall k \in \{0, 1, \dots , N - 1 \}, \\ \bar {\phi} (N; z, \mathbf {v}) \in \mathbb {Z} _ {f} \} \tag {3.26} \\ \end{array}
$$

# Bisection Algorithm

Lemma 4.5 suggests the following bisection algorithm to compute $\mathcal { R L } _ { \infty }$ norm:

(a) Select an upper bound $\gamma _ { u }$ and a lower bound $\gamma _ { l }$ such that $\gamma _ { l } \leq \| G \| _ { \infty } \leq \gamma _ { u } ;$   
(b) If $( \gamma _ { u } - \gamma _ { l } ) / \gamma _ { l }$ ≤specified level, stop; $\lVert G \rVert \approx ( \gamma _ { u } + \gamma _ { l } ) / 2$ . Otherwise go to the next step;   
(c) Set $\gamma = ( \gamma _ { l } + \gamma _ { u } ) / 2$ ;   
(d) Test $\operatorname { i f } \ \| G \| _ { \infty } < \gamma$ by calculating the eigenvalues of H for the given $\gamma ;$   
(e) If H has an eigenvalue on $j \mathbb { R }$ , set $\gamma _ { l } = \gamma ;$ otherwise set $\gamma _ { u } = \gamma ; \mathrm { g o }$ back to step (b).

Of course, the above algorithm applies to $\mathcal { H } _ { \infty }$ norm computation as well. Thus $\mathcal { L } _ { \infty }$ norm computation requires a search, over either γ or $\omega ,$ in contrast to ${ \mathcal { L } } _ { 2 } \ ( { \mathcal { H } } _ { 2 } )$ norm computation, which does not. A somewhat analogous situation occurs for constant matrices with the norms $\| M \| _ { 2 } ^ { 2 } = \mathrm { t r a c e } ( M ^ { * } M )$ and $\| M \| _ { \infty } = \overline { { \sigma } } [ M ]$ . In principle, $\| M \| _ { 2 } ^ { 2 }$ can be computed exactly with a finite number of operations, as can the test for whether $\overline { { \sigma } } ( M ) < \gamma \ ( \mathrm { e . g . } , \gamma ^ { 2 } I - M ^ { * } M > 0 )$ , but the value of $\overline { { \sigma } } ( M )$ cannot. To compute $\overline { { \sigma } } ( M )$ , we must use some type of iterative algorithm.

Remark 4.2 It is clear that $\left\| G \right\| _ { \infty } < \gamma \ \mathrm { i f f } \ \left\| \gamma ^ { - 1 } G \right\| _ { \infty } < 1$ . Hence, there is no loss of generality in assuming $\gamma = 1$ ∞ . This assumption will often be made in the remainder of this book. It is also noted that there are other fast algorithms to carry out the preceding norm computation; nevertheless, this bisection algorithm is the simplest. ✸

Additional interpretations can be given for the $\mathcal { H } _ { \infty }$ norm of a stable matrix transfer function. When $G ( s )$ is a single-input and single-output system, the $\mathcal { H } _ { \infty }$ norm of the $G ( s )$ can be regarded as the largest possible amplification factor of the system’s steadystate response to sinusoidal excitations. For example, the steady-state response of the system with respect to a sinusoidal input $u ( t ) = U \sin ( \omega _ { 0 } t + \phi )$ is

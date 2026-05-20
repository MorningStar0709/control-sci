for some admissible disturbance sequence $\textbf { w } = \{ w ( 0 ) , w ( 1 ) , \ldots \}$ in which $w ( i ) \in \mathbb { W }$ for all i. Using (3.22), which implies $V _ { N } ^ { 0 } ( x ( i + 1 ) ) \ s$ $V _ { N } ^ { 0 } ( x ( i ) ) - \ell ( x ( i ) , \kappa _ { N } ( x ( i ) ) , w ( i ) )$ ) for all i, we deduce that for any positive integer $M > 0$

$$V _ {N} ^ {0} (x (M)) \leq V _ {N} ^ {0} (x (0)) - \sum_ {i = 0} ^ {M - 1} \ell (x (i), \kappa_ {N} (x (i)), w (i))$$

If we express $\ell ( \cdot )$ in the form

$$
\ell (x, u, w) = (1 / 2) | y | ^ {2} - (\rho^ {2} / 2) w ^ {2} \qquad y := \left[ \begin{array}{c} C x \\ D u \end{array} \right]
$$

in which $Q = C ^ { \prime } C$ and $R = D ^ { \prime } D$ , we obtain

$$\sum_ {i = 0} ^ {M - 1} | y (i) | ^ {2} \leq \rho^ {2} \sum_ {i = 0} ^ {M - 1} | w (i) | ^ {2} + 2 V _ {N} ^ {0} (x)$$

for any positive integer M. If $\begin{array} { r } { \mathbf { w } \in \ell _ { 2 } ( \sum _ { i = 1 } ^ { \infty } | w ( i ) | ^ { 2 } < \infty ) } \end{array}$ , then

$$\sum_ {i = 0} ^ {\infty} | y (i) | ^ {2} \leq \rho^ {2} \sum_ {i = 0} ^ {\infty} | w (i) | ^ {2} + 2 V _ {N} ^ {0} (x)$$

and the closed-loop system $x ^ { + } = f ( x , \kappa _ { N } ( x ) , w )$ has finite $\ell _ { 2 }$ gain from w to $_ y$ .

We showed above that there exist $\mathcal { K } _ { \infty }$ functions $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ such that

$$
\begin{array}{l} V _ {N} ^ {0} (x) \geq \alpha_ {1} (| x |) \\ V _ {N} ^ {0} (x) \leq \alpha_ {2} (| x |) \\ \Delta V _ {N} ^ {0} (f (x, \kappa_ {N} (x), w)) \leq - \alpha_ {1} (| x |) + (\rho^ {2} / 2) | w | ^ {2} \\ \end{array}
$$

for all $\boldsymbol { x } \in \mathcal { X } _ { N }$ , if $x _ { N }$ is bounded, and all $w \in \mathbb { W }$ . Since $w \mapsto ( \rho ^ { 2 } / 2 ) | w | ^ { 2 }$ is a $\mathcal { K } _ { \infty }$ function, the closed-loop system $x ^ { + } = f ( x , \kappa _ { N } ( x ) , w )$ is also ISS with w as the input as discussed in Lemma B.38.

Asymptotic stability of the origin. As noted previously, the presence of a bounded disturbance prevents trajectories of the closed-loop system $x ^ { + } = f ( x , \kappa _ { N } ( x ) , w )$ from converging to the origin. We show next that asymptotic stability of the origin is possible, however, if the controller $\kappa _ { N } ( \cdot )$ is determined on the basis that the disturbance is bounded $( w \in \mathbb { W } )$ , but the disturbance is either zero or converges to zero as the state tends to the origin.

We showed previously that the value function $V _ { N } ^ { 0 } ( \cdot )$ obtained on the basis that $w \in \mathbb { W }$ satisfies

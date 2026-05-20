# 10.3.3 Two-Block µ: Robust Performance Revisited

Suppose that the uncertainty block is given by

$$
\Delta = \left[ \begin{array}{c c} \Delta_ {1} & \\ & \Delta_ {2} \end{array} \right] \in \mathcal {R H} _ {\infty}
$$

with $\| \Delta \| _ { \infty } < 1$ and that the interconnection model G is given by

$$
G (s) = \left[ \begin{array}{c c} G _ {1 1} (s) & G _ {1 2} (s) \\ G _ {2 1} (s) & G _ {2 2} (s) \end{array} \right] \in \mathcal {R H} _ {\infty}.
$$

Then the closed-loop system is well-posed and internally stable iff $\begin{array} { r } { \operatorname* { s u p } _ { \omega } \mu _ { \pmb { \Delta } } ( G ( j \omega ) ) \le 1 } \end{array}$ Let

$$
D _ {\omega} = \left[ \begin{array}{c c} d _ {\omega} I & \\ & I \end{array} \right], d _ {\omega} \in \mathbb {R} _ {+}.
$$

Then

$$
D _ {\omega} G (j \omega) D _ {\omega} ^ {- 1} = \left[ \begin{array}{c c} G _ {1 1} (j \omega) & d _ {\omega} G _ {1 2} (j \omega) \\ \frac {1}{d _ {\omega}} G _ {2 1} (j \omega) & G _ {2 2} (j \omega) \end{array} \right].
$$

Hence, by Theorem 10.4, at each frequency ω

$$
\mu_ {\boldsymbol {\Delta}} (G (j \omega)) = \inf _ {d _ {\omega} \in \mathbb {R} _ {+}} \overline {{\sigma}} \left(\left[ \begin{array}{c c} G _ {1 1} (j \omega) & d _ {\omega} G _ {1 2} (j \omega) \\ \frac {1}{d _ {\omega}} G _ {2 1} (j \omega) & G _ {2 2} (j \omega) \end{array} \right]\right). \tag {10.20}
$$

Since the minimization is convex in log $\cdot d _ { \omega }$ (see, Doyle [1982]), the optimal $d _ { \omega }$ can be found by a search; however, two approximations to $d _ { \omega }$ can be obtained easily by approximating the right-hand side of equation (10.20):

(1) Note that

$$
\begin{array}{l} \mu_ {\boldsymbol {\Delta}} (G (j \omega)) \leq \inf _ {d _ {\omega} \in \mathbb {R} _ {+}} \overline {{\sigma}} \left(\left[ \begin{array}{c c} \| G _ {1 1} (j \omega) \| & d _ {\omega}   \| G _ {1 2} (j \omega) \| \\ \frac {1}{d _ {\omega}}   \| G _ {2 1} (j \omega) \| & \| G _ {2 2} (j \omega) \| \end{array} \right]\right) \\ \leq \sqrt {\inf _ {d _ {\omega} \in \mathbb {R} _ {+}} \left(\| G _ {1 1} (j \omega) \| ^ {2} + d _ {\omega} ^ {2} \| G _ {1 2} (j \omega) \| ^ {2} + \frac {1}{d _ {\omega} ^ {2}} \| G _ {2 1} (j \omega) \| ^ {2} + \| G _ {2 2} (j \omega) \| ^ {2}\right)} \\ \end{array}
{ = } \sqrt { \| G _ { 1 1 } ( j \omega ) \| ^ { 2 } + \| G _ { 2 2 } ( j \omega ) \| ^ { 2 } + 2 \| G _ { 1 2 } ( j \omega ) \| \| G _ { 2 1 } ( j \omega ) \| }
$$

with the minimizing $d _ { \omega }$ given by

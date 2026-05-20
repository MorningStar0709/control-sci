$$
\begin{array}{l} \| G f \| _ {2} ^ {2} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} f ^ {*} (j \omega) G ^ {*} (j \omega) G (j \omega) f (j \omega) d \omega \\ \leq \| G \| _ {\infty} ^ {2} \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \| f (j \omega) \| ^ {2} d \omega \\ = \| G \| _ {\infty} ^ {2} \| f \| _ {2} ^ {2}. \\ \end{array}
$$

To show that $\| G \| _ { \infty }$ is the least upper bound, first choose a frequency ω0 where ${ \overline { { \sigma } } } \left[ G ( j \omega ) \right]$ is maximum; that is,

$$\overline {{{\sigma}}} \left[ G (j \omega_ {0}) \right] = \| G \| _ {\infty},$$

and denote the singular value decomposition of $G ( j \omega _ { 0 } )$ by

$$G (j \omega_ {0}) = \overline {{\sigma}} u _ {1} (j \omega_ {0}) v _ {1} ^ {*} (j \omega_ {0}) + \sum_ {i = 2} ^ {r} \sigma_ {i} u _ {i} (j \omega_ {0}) v _ {i} ^ {*} (j \omega_ {0})$$

where r is the rank of $G ( j \omega _ { 0 } )$ and $u _ { i } , v _ { i }$ have unit length.

Next we assume that $G ( s )$ has real coefficients and we shall construct a function $f ( s ) \in \mathcal { H } _ { 2 }$ with real coefficients so that the norm is approximately achieved. [It will be clear in the following that the proof is much simpler if $f$ is allowed to have complex coefficients, which is necessary when $G ( s )$ has complex coefficients.]

If $\omega _ { 0 } < \infty ,$ write $v _ { 1 } ( j \omega _ { 0 } )$ as

$$
v _ {1} (j \omega_ {0}) = \left[ \begin{array}{c} \alpha_ {1} e ^ {j \theta_ {1}} \\ \alpha_ {2} e ^ {j \theta_ {2}} \\ \vdots \\ \alpha_ {q} e ^ {j \theta_ {q}} \end{array} \right]
$$

where $\alpha _ { i } \in \mathbb { R }$ is such that $\theta _ { i } \in ( - \pi , 0 ]$ and $q$ is the column dimension of G. Now let $0 \leq \beta _ { i } \leq \infty$ be such that

$$\theta_ {i} = \angle \left(\frac {\beta_ {i} - j \omega_ {0}}{\beta_ {i} + j \omega_ {0}}\right)$$

(with $\beta _ { i } \to \infty { \mathrm { ~ i f ~ } } \theta _ { i } = 0 )$ and let $f$ be given by

$$
f (s) = \left[ \begin{array}{c} \alpha_ {1} \frac {\beta_ {1} - s}{\beta_ {1} + s} \\ \alpha_ {2} \frac {\beta_ {2} - s}{\beta_ {2} + s} \\ \vdots \\ \alpha_ {q} \frac {\beta_ {q} - s}{\beta_ {q} + s} \end{array} \right] \hat {f} (s)
$$

$\frac { \beta _ { i } - s } { \beta _ { i } + s } \mathrm { ~ i f ~ } \theta _ { i } = 0 )$ $\hat { f }$

$$
| \hat {f} (j \omega) | = \left\{ \begin{array}{l l} c & \text {if} | \omega - \omega_ {0} | <   \epsilon \text {or} | \omega + \omega_ {0} | <   \epsilon \\ 0 & \text {otherwise} \end{array} \right.
$$

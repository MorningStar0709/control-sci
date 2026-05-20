(Necessity) This will be shown by contradiction. Suppose $\| M \| _ { \infty } \geq 1$ . We will show that there exists a $\Delta \in \mathcal { R } \mathcal { H } _ { \infty }$ with $\| \Delta \| _ { \infty } \leq 1$ such that det $( I - M ( s ) \Delta ( s ) )$ has a zero on the imaginary axis, so the system is unstable. Suppose ω0 $\in \mathbb { R } _ { + } \cup \{ \infty \}$ is such that $\bar { \sigma } ( M ( j \omega _ { 0 } ) ) \geq 1$ . Let $M ( j \omega _ { 0 } ) = U ( j \omega _ { 0 } ) \Sigma ( j \omega _ { 0 } ) V ^ { * } ( j \omega _ { 0 } )$ be a singular value decomposition with

$$
U (j \omega_ {0}) = \left[ \begin{array}{l l l l} u _ {1} & u _ {2} & \dots & u _ {p} \end{array} \right]

V (j \omega_ {0}) = \left[ \begin{array}{l l l l} v _ {1} & v _ {2} & \dots & v _ {q} \end{array} \right]

\Sigma (j \omega_ {0}) = \left[ \begin{array}{c c c} \sigma_ {1} & & \\ & \sigma_ {2} & \\ & & \ddots \end{array} \right]
$$

To obtain a contradiction, it now suffices to construct a $\Delta \in \mathcal { R } \mathcal { H } _ { \infty }$ such that $\Delta ( j \omega _ { 0 } ) =$ $\scriptstyle { \frac { 1 } { \sigma _ { 1 } } } v _ { 1 } u _ { 1 } ^ { * }$ and $\| \Delta \| _ { \infty } \leq 1$ . Indeed, for such $\Delta ( s )$ ,

$$\det (I - M (j \omega_ {0}) \Delta (j \omega_ {0})) = \det (I - U \Sigma V ^ {*} v _ {1} u _ {1} ^ {*} / \sigma_ {1}) = 1 - u _ {1} ^ {*} U \Sigma V ^ {*} v _ {1} / \sigma_ {1} = 0$$

and thus the closed-loop system is either not well-posed $( \mathrm { i f } \ \omega _ { 0 } = \infty )$ or unstable (if $\omega \in \mathbb { R } )$ . There are two different cases:

(1) $\omega _ { 0 } = 0$ or ∞: then U and V are real matrices. In this case, $\Delta ( s )$ can be chosen as

$$\Delta = \frac {1}{\sigma_ {1}} v _ {1} u _ {1} ^ {*} \in \mathbb {R} ^ {q \times p}$$

(2) $0 < \omega _ { 0 } < \infty \colon$ write $u _ { 1 }$ and $v _ { 1 }$ in the following form:

$$
u _ {1} ^ {*} = \left[ \begin{array}{c c c c} u _ {1 1} e ^ {j \theta_ {1}} & u _ {1 2} e ^ {j \theta_ {2}} & \dots & u _ {1 p} e ^ {j \theta_ {p}} \end{array} \right], \quad v _ {1} = \left[ \begin{array}{c} v _ {1 1} e ^ {j \phi_ {1}} \\ v _ {1 2} e ^ {j \phi_ {2}} \\ \vdots \\ v _ {1 q} e ^ {j \phi_ {q}} \end{array} \right]
$$

where $u _ { 1 i } \in \mathbb { R }$ and $v _ { 1 j } \in \mathbb { R }$ are chosen so that $\theta _ { i } , \phi _ { j } \in [ - \pi , 0 )$ for all $i , j$ .

Choose $\beta _ { i } \geq 0$ and $\alpha _ { j } \geq 0$ so that

$$\angle \left(\frac {\beta_ {i} - j \omega_ {0}}{\beta_ {i} + j \omega_ {0}}\right) = \theta_ {i}, \quad \angle \left(\frac {\alpha_ {j} - j \omega_ {0}}{\alpha_ {j} + j \omega_ {0}}\right) = \phi_ {j}$$

for $i = 1 , 2 , \dotsc , p$ and $j = 1 , 2 , \dots , q .$ Let

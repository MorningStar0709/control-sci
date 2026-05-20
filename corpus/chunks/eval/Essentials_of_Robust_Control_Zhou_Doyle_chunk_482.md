$$
\left[ \begin{array}{c} y _ {0} \\ y _ {1} \\ \vdots \\ y _ {l - 1} \end{array} \right] = \left[ \begin{array}{c c c c} h _ {0} & 0 & \dots & 0 \\ h _ {1} & h _ {0} & \ddots & 0 \\ \vdots & \vdots & \ddots & 0 \\ h _ {l - 1} & h _ {l - 2} & \dots & h _ {0} \end{array} \right] \left[ \begin{array}{c} u _ {0} \\ u _ {1} \\ \vdots \\ u _ {l - 1} \end{array} \right].
$$

This equation shows that, for $u _ { 0 } \neq 0$ and $\mathrm { S I S O ~ } \Delta .$ , the inputs and outputs uniquely determine the first \` Markov parameters of the transfer function $\Delta ( z )$ . The model is validated (or more accurately not invalidated) if the remaining Markov parameters can be chosen so that $\Delta ( z ) \in \Delta$ . The existence of such a choice is the classical tangential Carath´eodory-Fej´er interpolation problem, for which a solution to the MIMO case can be found in Foias and Frazho [1990, page 195]. We shall state this result in the following theorem. But we shall define some notation first.

Let $( v _ { 0 } , v _ { 1 } , \ldots , v _ { \ell - 1 } , v _ { \ell } , v _ { \ell + 1 } , \ldots )$ be a sequence and let $\pi _ { \ell }$ denote the truncation operator such that

$$\pi_ {\ell} (v _ {0}, v _ {1}, \dots , v _ {\ell - 1}, v _ {\ell}, v _ {\ell + 1}, \dots) = (v _ {0}, v _ {1}, \dots , v _ {\ell - 1}).$$

Let $v = ( v _ { 0 } , v _ { 1 } , \dots , v _ { \ell - 1 } )$ be a sequence of vectors and denote

$$
T _ {v} := \left[ \begin{array}{c c c c} v _ {0} & 0 & \dots & 0 \\ v _ {1} & v _ {0} & \ddots & 0 \\ \vdots & \vdots & \ddots & 0 \\ v _ {l - 1} & v _ {l - 2} & \dots & v _ {0} \end{array} \right].
$$

Theorem 18.1 Given $u = ( u _ { 0 } , u _ { 1 } , \dotsc , u _ { l - 1 } )$ and $y = ( y _ { 0 } , y _ { 1 } , \dotsc , y _ { l - 1 } )$ , there exists a $\Delta \in \mathcal { H } _ { \infty } , \| \Delta \| _ { \infty } \leq 1$ such that

$$y = \pi_ {\ell} \Delta u$$

if and only if $T _ { y } ^ { \ast } T _ { y } \leq T _ { u } ^ { \ast } T _ { u }$ .

Note that the output of $\Delta$ after time $t = \ell - 1$ is irrelevant to the test. The condition $T _ { y } ^ { \ast } T _ { y } \leq T _ { u } ^ { \ast } T _ { u }$ is equivalent to

$$\sum_ {j = 1} ^ {i} \| y _ {j} \| ^ {2} \leq \sum_ {j = 1} ^ {i} \| u _ {j} \| ^ {2}, i = 0, 1, \dots , \ell - 1$$

or

$$\left\| \pi_ {i} y \right\| _ {2} \leq \left\| \pi_ {i} u \right\| _ {2}, i = 0, 1, \dots , \ell - 1,$$

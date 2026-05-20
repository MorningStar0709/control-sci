Note that $\begin{array} { r } { \int _ { 0 } ^ { T } e ^ { \mathbf { A } \tau } \mathbf { B } \mathbf { u } ( T - \tau ) } \end{array}$ can be expressed as the sum ofdt $\mathbf { A } ^ { i } \mathbf { B } _ { j }$ ; that is,

$$\int_ {0} ^ {T} e ^ {\mathbf {A} \tau} \mathbf {B u} (T - \tau) d \tau = \sum_ {i = 0} ^ {p - 1} \sum_ {j = 1} ^ {r} \gamma_ {i j} \mathbf {A} ^ {i} \mathbf {B} _ {j}$$

where

$$\gamma_ {i j} = \int_ {0} ^ {T} \alpha_ {i} (\tau) u _ {j} (T - \tau) d \tau = \text { scalar }$$

and $\alpha _ { i } ( \tau )$ satisfies

$$e ^ {\mathbf {A} \tau} = \sum_ {i = 0} ^ {p - 1} \alpha_ {i} (\tau) \mathbf {A} ^ {i} \quad (p: \text { degree of the minimal polynomial of } \mathbf {A})$$

and $\mathbf { B } _ { j }$ is the jth column of B. Therefore, we can write $\mathbf { C } e ^ { \mathbf { A } T } \mathbf { x } ( 0 )$ as

$$\mathbf {C} e ^ {\mathbf {A} T} \mathbf {x} (0) = - \sum_ {i = 0} ^ {p - 1} \sum_ {j = 1} ^ {r} \gamma_ {i j} \mathbf {C A} ^ {i} \mathbf {B} _ {j}$$

From this last equation, we see that $\mathbf { C } e ^ { \mathbf { A } T } \mathbf { x } ( 0 )$ is a linear combination of $\mathbf { C A } ^ { i } \mathbf { B } _ { j } ( i = 0 , 1 , 2 , \ldots$ , $p \mathrm { ~ - ~ } 1 ; j = 1 , 2 , \ldots , r )$ . Note that if the rank of Q, where

$$
\mathbf {Q} = \left[ \begin{array}{c c c c c c} \mathbf {C B} & \mathbf {C A B} & \mathbf {C A ^ {2} B} & \dots & \mathbf {C A ^ {p - 1} B} \end{array} \right] \quad (p \leq n)
$$

is m, then so is the rank of P, and vice versa. [This is obvious if $p = n$ . If $p < n ,$ , then the $\mathbf { C A } ^ { h } \mathbf { B } _ { i }$ (where $p \leq h \leq n - 1 )$ are linearly dependent on $\mathbf { C B } _ { j } , \mathbf { C A B } _ { j } , \ldots , \mathbf { C A } ^ { p - 1 } \mathbf { B } _ { j }$ . Hence, the rank of

P is equal to that of $\mathbf { Q . } ]$ If the rank of P is $m ,$ , then $\mathbf { C } e ^ { \mathbf { A } T } \mathbf { x } ( 0 )$ spans the m-dimensional output space. This means that if the rank of P is $m ,$ then $\mathbf { C x } ( 0 )$ also spans the m-dimensional output space and the system is completely output controllable.

Conversely, suppose that the system is completely output controllable, but the rank of P is k, where $k < m$ . Then the set of all initial outputs that can be transferred to the origin is of k-dimensional space. Hence, the dimension of this set is less than m. This contradicts the assumption that the system is completely output controllable. This completes the proof.

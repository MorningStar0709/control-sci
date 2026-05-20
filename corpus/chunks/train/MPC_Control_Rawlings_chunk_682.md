$$
\begin{array}{l} \left[ \begin{array}{c} x _ {2} (1) \\ x _ {2} (2) \\ \vdots \\ x _ {2} (N) \end{array} \right] = \left[ \begin{array}{c} A _ {2} \\ A _ {2} ^ {2} \\ \vdots \\ A _ {2} ^ {N} \end{array} \right] x _ {2} (0) + \left[ \begin{array}{c c c c} \overline {{B}} _ {2 1} & & & \\ A _ {2} \overline {{B}} _ {2 1} & \overline {{B}} _ {2 1} & & \\ \vdots & \vdots & \ddots & \\ A _ {2} ^ {N - 1} \overline {{B}} _ {2 1} & A _ {2} ^ {N - 2} \overline {{B}} _ {2 1} & \dots & \overline {{B}} _ {2 1} \end{array} \right] \left[ \begin{array}{c} u _ {1} (0) \\ u _ {1} (1) \\ \vdots \\ u _ {1} (N - 1) \end{array} \right] + \\ \left[ \begin{array}{c c c c} \overline {{B}} _ {2 2} & & & \\ A _ {2} \overline {{B}} _ {2 2} & \overline {{B}} _ {2 2} & & \\ \vdots & \vdots & \ddots & \\ A _ {2} ^ {N - 1} \overline {{B}} _ {2 2} & A _ {2} ^ {N - 2} \overline {{B}} _ {2 2} & \ldots & \overline {{B}} _ {2 2} \end{array} \right] \left[ \begin{array}{c} u _ {2} (0) \\ u _ {2} (1) \\ \vdots \\ u _ {2} (N - 1) \end{array} \right] \\ \end{array}
$$

Using more compact notation, we have

$$\mathbf {x} _ {2} = \mathcal {A} _ {2} x _ {2} (0) + \mathcal {B} _ {2 1} \mathbf {u} _ {1} + \mathcal {B} _ {2 2} \mathbf {u} _ {2}$$

We can use this relation to replace the cost contribution of $\mathbf { X } _ { 2 }$ with linear and quadratic terms in $\mathbf { u } _ { 1 }$ as follows

$$
\begin{array}{l} \sum_ {k = 0} ^ {N - 1} x _ {2} (k) ^ {\prime} Q _ {2} x _ {2} (k) + x _ {2} (N) ^ {\prime} P _ {2 f} x _ {2} (N) = \\ \mathbf {u} _ {1} ^ {\prime} \left[ \mathcal {B} _ {2 1} ^ {\prime} \mathcal {Q} _ {2} \mathcal {B} _ {2 1} \right] \mathbf {u} _ {1} + 2 \left[ x _ {2} (0) ^ {\prime} \mathcal {A} _ {2} ^ {\prime} + \mathbf {u} _ {2} ^ {\prime} \mathcal {B} _ {2 2} ^ {\prime} \right] \mathcal {Q} _ {2} \mathcal {B} _ {2 1} \mathbf {u} _ {1} + \text { constant } \\ \end{array}
$$

in which

$$
\mathcal {Q} _ {2} = \operatorname{diag} \left(\left[ \begin{array}{c c c c} Q _ {2} & Q _ {2} & \dots & P _ {2 f} \end{array} \right]\right) \quad N n _ {2} \times N n _ {2} \text {   matrix }
$$

and the constant term contains products of $x _ { 2 } ( 0 )$ and $\mathbf { u } _ { 2 }$ , which are constant with respect to player $\mathrm { o n e ^ { \prime } s }$ decision variables and can therefore be neglected.

Next we insert the new terms created by eliminating $\mathbf { X } 2$ into the cost function. Assembling the cost function gives

$$\min _ {\mathbf {z}} (1 / 2) \mathbf {z} ^ {\prime} \tilde {H} \mathbf {z} + h ^ {\prime} \mathbf {z}\mathrm{s.t.} D \mathbf {z} = d$$

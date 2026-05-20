$$\min _ {\sigma \in [ 0, \sigma_ {0} ]} \| M (\sigma + j \omega_ {0}) \| \geq \gamma$$

and

$$\sqrt {\frac {\omega_ {0} ^ {2} + (\sigma_ {0} + \alpha) ^ {2}}{\omega_ {0} ^ {2} + (\sigma_ {0} - \alpha) ^ {2}}} \sqrt {\frac {\omega_ {0} ^ {2} + (\sigma_ {0} + \beta) ^ {2}}{\omega_ {0} ^ {2} + (\sigma_ {0} - \beta) ^ {2}}} < \gamma$$

for any $\alpha \geq 0$ and $\beta \geq 0$

Now let $\sigma \in [ 0 , \sigma _ { 0 } ]$ and let $M ( \sigma + j \omega _ { 0 } ) = U \Sigma V ^ { * }$ be a singular value decomposition with

$$
U = \left[ \begin{array}{l l l l} u _ {1} & u _ {2} & \dots & u _ {p} \end{array} \right]

V = \left[ \begin{array}{l l l l} v _ {1} & v _ {2} & \dots & v _ {q} \end{array} \right]

\Sigma = \left[ \begin{array}{c c c} \sigma_ {1} & & \\ & \sigma_ {2} & \\ & & \ddots \end{array} \right].
$$

Write $u _ { 1 }$ and $v _ { 1 }$ in the following form:

$$
u _ {1} ^ {*} = \left[ \begin{array}{c c c c} u _ {1 1} e ^ {j \theta_ {1}} & u _ {1 2} e ^ {j \theta_ {2}} & \dots & u _ {1 p} e ^ {j \theta_ {p}} \end{array} \right], \quad v _ {1} = \left[ \begin{array}{c} v _ {1 1} e ^ {j \phi_ {1}} \\ v _ {1 2} e ^ {j \phi_ {2}} \\ \vdots \\ v _ {1 q} e ^ {j \phi_ {q}} \end{array} \right]
$$

where $u _ { 1 i } \in \mathbb { R }$ and $v _ { 1 j } \in \mathbb { R }$ are chosen so that $\theta _ { i } , \phi _ { j } \in [ - \pi , 0 )$ for all $i , j .$ .

Choose $\beta _ { i } \geq 0$ and $\alpha _ { j } \geq 0$ so that

$$\angle \left(\frac {\beta_ {i} - \sigma - j \omega_ {0}}{\beta_ {i} + \sigma + j \omega_ {0}}\right) = \theta_ {i}, \quad \angle \left(\frac {\alpha_ {j} - \sigma - j \omega_ {0}}{\alpha_ {j} + \sigma + j \omega_ {0}}\right) = \phi_ {j}$$

for $i = 1 , 2 , \dotsc , p$ and $j = 1 , 2 , \dots , q .$ . Let

$$
\Delta (s) = \frac {1}{\sigma_ {1}} \left[ \begin{array}{c} \tilde {\alpha} _ {1} v _ {1 1} \frac {\alpha_ {1} - s}{\alpha_ {1} + s} \\ \vdots \\ \tilde {\alpha} _ {q} v _ {1 q} \frac {\alpha_ {q} - s}{\alpha_ {q} + s} \end{array} \right] \left[ \begin{array}{c c c} \tilde {\beta} _ {1} u _ {1 1} \frac {\beta_ {1} - s}{\beta_ {1} + s} & \dots & \tilde {\beta} _ {p} u _ {1 p} \frac {\beta_ {p} - s}{\beta_ {p} + s} \end{array} \right] \in \mathcal {R H} _ {\infty}
$$

where

$$\tilde {\beta} _ {i} := \sqrt {\frac {\omega_ {0} ^ {2} + (\sigma + \beta_ {i}) ^ {2}}{\omega_ {0} ^ {2} + (\sigma - \beta_ {i}) ^ {2}}}, \tilde {\alpha} _ {j} := \sqrt {\frac {\omega_ {0} ^ {2} + (\sigma + \alpha_ {j}) ^ {2}}{\omega_ {0} ^ {2} + (\sigma - \alpha_ {j}) ^ {2}}}$$

Then

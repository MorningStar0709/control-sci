# 5.10.1 Error Analysis

Equations (5.43a), (5.43b), and (5.43c) can be written symbolically for a 3DOF trajectory in the form

$$\frac {d ^ {2} \mathbf {r}}{d t ^ {2}} = \mathbf {f} (t, \mathbf {r}, \dot {\mathbf {r}}, \mathbf {p}), \tag {5.46}$$

where

$$\mathbf {r} ^ {T} \equiv [ x y z ],\mathbf {f} ^ {T} \equiv [ f _ {x} f _ {y} f _ {z} ],\mathbf {p} ^ {T} \equiv [ \mathbf {r} _ {o} ^ {T} \dot {\mathbf {r}} _ {o} ^ {T} t _ {o} \mathbf {D} ^ {T} \mathbf {W} ^ {T} ].$$

The first seven parameters of the $3 \times M$ vector p are the initial conditions and initial time. The drag (D) and wind $( \mathbf { W } )$ parameters occur in the input tables for $C _ { D }$ (Mach number) and ${ \mathbf W } ( x , y , h )$ . The $t _ { o }$ parameter allows the error analysis to include a sensitivity for release error time.

Letting $p ( p = 1 , \ldots , M )$ denote any member of the set $\mathbf { p } ^ { T }$ above, the sensitivity $3 \times M$ vector may be defined as

$$\mathbf {S} (t) \equiv (\partial \mathbf {r} / \partial p), \frac {d \mathbf {S} (t)}{d t} \equiv (\partial \dot {\mathbf {r}} / \partial p) = \left(\frac {d}{d t}\right) (\partial \mathbf {r} / \partial p).$$

Differentiating (5.31) partially with respect to p and interchanging the order of $d / d t$ and $\partial / \partial p$ (since $p$ is a constant), results in a $3 \times 1$ sensitivity differential equation of the form

$$\frac {d ^ {2} \mathbf {S} (t)}{d t ^ {2}} = \mathbf {A} (t) + B (t) \mathbf {S} + C (t) \left(\frac {d \mathbf {S} (t)}{d t}\right), \tag {5.47}$$

where

$$\mathbf {A} \equiv (\partial \mathbf {f} / \partial p), B \equiv (\partial \mathbf {f} / \partial \mathbf {r} ^ {T}), C \equiv (\partial \mathbf {f} / \partial \mathbf {r} ^ {T}).$$

(Note that $\mathbf { A } \equiv 0$ for $\begin{array} { r } { p = x _ { 0 } , y _ { 0 } , z _ { 0 } , ( d x _ { 0 } / d t ) , ( d y _ { 0 } / d t ) , ( d z _ { 0 } / d t ) , t _ { o } } \end{array}$ and is nonzero for the D and W parameters, that is, holding r and $d \mathbf { r } / d t$ constant in differentiating f partially with respect to explicit dependence on $p . )$

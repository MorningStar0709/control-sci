Since $G _ { f }$ and $V$ are also orthogonal by Lemma 13.6, we have

$$
\begin{array}{l} \| T _ {z w} \| _ {2} ^ {2} = \| G _ {c} B _ {1} \| _ {2} ^ {2} + \left\| R _ {1} ^ {1 / 2} F _ {2} G _ {f} - R _ {1} ^ {1 / 2} Q R _ {2} ^ {1 / 2} V \right\| _ {2} ^ {2} \\ { = } { \| G _ { c } B _ { 1 } \| _ { 2 } ^ { 2 } + \left\| R _ { 1 } ^ { 1 / 2 } F _ { 2 } G _ { f } \right\| _ { 2 } ^ { 2 } + \left\| R _ { 1 } ^ { 1 / 2 } Q R _ { 2 } ^ { 1 / 2 } \right\| _ { 2 } ^ { 2 } . } \\ \end{array}
$$

This shows clearly that $Q = 0$ gives the unique optimal control, so $K = \mathcal { F } _ { \ell } ( M _ { 2 } , 0 )$ is the unique optimal controller. ✷

The optimal $\mathcal { H } _ { 2 }$ controller, $K _ { \mathrm { o p t } }$ , and the closed-loop transfer matrix, $T _ { z w } ,$ can be obtained by the following Matlab program:

$$\gg [ \mathbf {K}, \mathbf {T} _ {\mathbf {z w}} ] = \mathrm{h2syn} (\mathbf {G}, \mathbf {n} _ {\mathbf {y}}, \mathbf {n} _ {\mathbf {u}})$$

where $n _ { y }$ and $n _ { u }$ are the dimensions of y and u, respectively.

Related MATLAB Commands: lqg, lqr, lqr2, lqry, reg, lqe

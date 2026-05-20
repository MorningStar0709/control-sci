$$(A _ {1 1} - j \omega I) \Sigma_ {1} + \Sigma_ {1} (A _ {1 1} ^ {*} + j \omega I) + B _ {1} B _ {1} ^ {*} = 0 \tag {7.14}\Sigma_ {1} (A _ {1 1} - j \omega I) + (A _ {1 1} ^ {*} + j \omega I) \Sigma_ {1} + C _ {1} ^ {*} C _ {1} = 0. \tag {7.15}$$

Multiplication of equation (7.15) from the right by $V$ and from the left by $V ^ { * }$ gives $V ^ { * } C _ { 1 } ^ { * } C _ { 1 } V = 0$ , which is equivalent to

$$C _ {1} V = 0.$$

Multiplication of equation (7.15) from the right by $V$ now gives

$$(A _ {1 1} ^ {*} + j \omega I) \Sigma_ {1} V = 0.$$

Analogously, first multiply equation (7.14) from the right by $\Sigma _ { 1 } V$ and from the left by $V ^ { * } \Sigma _ { 1 }$ to obtain

$$B _ {1} ^ {*} \Sigma_ {1} V = 0.$$

Then multiply equation (7.14) from the right by $\Sigma _ { 1 } V$ to get

$$(A _ {1 1} - j \omega I) \Sigma_ {1} ^ {2} V = 0.$$

It follows that the columns of $\Sigma _ { 1 } ^ { 2 } V$ are in $\operatorname { K e r } ( A _ { 1 1 } - j \omega I )$ . Therefore, there exists a matrix $\bar { \Sigma } _ { 1 }$ such that

$$\Sigma_ {1} ^ {2} V = V \bar {\Sigma} _ {1} ^ {2}.$$

Since $\bar { \Sigma } _ { 1 } ^ { 2 }$ is the restriction of $\Sigma _ { 1 } ^ { 2 }$ to the space spanned by $V ,$ it follows that it is possible to choose $V$ such that $\bar { \Sigma } _ { 1 } ^ { 2 }$ is diagonal. It is then also possible to choose $\bar { \Sigma } _ { 1 }$ diagonal and such that the diagonal entries of $\bar { \Sigma } _ { 1 }$ are a subset of the diagonal entries of $\Sigma _ { 1 }$ .

Multiply equation (7.9) from the right by $\Sigma _ { 1 } V$ and equation (7.10) by $V$ to get

$$A _ {2 1} \Sigma_ {1} ^ {2} V + \Sigma_ {2} A _ {1 2} ^ {*} \Sigma_ {1} V = 0\Sigma_ {2} A _ {2 1} V + A _ {1 2} ^ {*} \Sigma_ {1} V = 0,$$

which gives

$$(A _ {2 1} V) \bar {\Sigma} _ {1} ^ {2} = \Sigma_ {2} ^ {2} (A _ {2 1} V).$$

This is a Sylvester equation in $( A _ { 2 1 } V )$ . Because ${ { \bar { \Sigma } } _ { 1 } } ^ { 2 }$ and $\Sigma _ { 2 } ^ { 2 }$ have no diagonal entries in common, it follows that

$$A _ {2 1} V = 0 \tag {7.16}$$

is the unique solution. Now equations (7.16) and (7.13) imply that

$$
\left[ \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] \left[ \begin{array}{c} V \\ 0 \end{array} \right] = j \omega \left[ \begin{array}{c} V \\ 0 \end{array} \right],
$$

which means that the A-matrix of the original system has an eigenvalue at $j \omega .$ . This contradicts the fact that the original system is asymptotically stable. Therefore, $A _ { 1 1 }$ must be asymptotically stable. ✷

Corollary 7.10 If Σ has distinct singular values, then every subsystem is asymptotically stable.

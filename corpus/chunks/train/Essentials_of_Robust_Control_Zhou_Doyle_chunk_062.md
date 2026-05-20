$$U ^ {*} A V = \Sigma .$$

This completes the proof.

![](image/6360dd157bd95a22906531209ae43166a0dfccb49df0b9d600c707c38728e9f0.jpg)

The $\sigma _ { i }$ is the ith singular value of $A ,$ and the vectors $u _ { i }$ and $v _ { j }$ are, respectively, the ith left singular vector and the jth right singular vector. It is easy to verify that

$$A v _ {i} = \sigma_ {i} u _ {i}A ^ {*} u _ {i} = \sigma_ {i} v _ {i}.$$

The preceding equations can also be written as

$$A ^ {*} A v _ {i} = \sigma_ {i} ^ {2} v _ {i}A A ^ {*} u _ {i} = \sigma_ {i} ^ {2} u _ {i}.$$

Hence $\sigma _ { i } ^ { 2 }$ is an eigenvalue of $A A ^ { * }$ or $A ^ { * } A , u _ { i }$ is an eigenvector of $A A ^ { * }$ , and $v _ { i }$ is an eigenvector of $A ^ { * } A$ .

The following notations for singular values are often adopted:

$$\overline {{\sigma}} (A) = \sigma_ {\max} (A) = \sigma_ {1} = \text { the largest singular value of } A;$$

and

$$\underline {{\sigma}} (A) = \sigma_ {\min} (A) = \sigma_ {p} = \text { the smallest singular value of } A.$$

Geometrically, the singular values of a matrix A are precisely the lengths of the semiaxes of the hyperellipsoid E defined by

$$E = \{y: y = A x, x \in \mathbb {C} ^ {n}, \| x \| = 1 \}.$$

Thus $v _ { 1 }$ is the direction in which kyk is largest for all $\lVert x \rVert = 1 ;$ ; while $v _ { n }$ is the direction in which $\| y \|$ is smallest for all $\| { \boldsymbol x } \| = 1$ . From the input/output point of view, $v _ { 1 } \ \left( v _ { n } \right)$ is the highest (lowest) gain input (or control) direction, while $u _ { 1 } ~ ( u _ { m } )$ is the highest (lowest) gain output (or observing) direction. This can be illustrated by the following $2 \times 2$ matrix:

$$
A = \left[ \begin{array}{c c} \cos \theta_ {1} & - \sin \theta_ {1} \\ \sin \theta_ {1} & \cos \theta_ {1} \end{array} \right] \left[ \begin{array}{c c} \sigma_ {1} & \\ & \sigma_ {2} \end{array} \right] \left[ \begin{array}{c c} \cos \theta_ {2} & - \sin \theta_ {2} \\ \sin \theta_ {2} & \cos \theta_ {2} \end{array} \right].
$$

It is easy to see that A maps a unit circle to an ellipsoid with semiaxes of $\sigma _ { 1 }$ and $\sigma _ { 2 }$ .

Hence it is often convenient to introduce the following alternative definitions for the largest singular value σ:

$$\overline {{\sigma}} (A) := \max _ {\| x \| = 1} \| A x \|$$

and for the smallest singular value $\underline { { \sigma } }$ of a tall matrix:

$$\underline {{\sigma}} (A) := \min _ {\| x \| = 1} \| A x \|.$$

Lemma 2.5 Suppose A and $\Delta$ are square matrices. Then

(i) $| \underline { { \sigma } } ( A + \Delta ) - \underline { { \sigma } } ( A ) | \leq \overline { { \sigma } } ( \Delta )$ ;

(ii) $\underline { { \sigma } } ( A \Delta ) \geq \underline { { \sigma } } ( A ) \underline { { \sigma } } ( \Delta )$ ;

(iii) ${ \overline { { \sigma } } } ( A ^ { - 1 } ) = { \frac { 1 } { \underline { { \sigma } } ( A ) } } \ i f \ A$ is invertible.

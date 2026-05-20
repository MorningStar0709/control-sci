# Diagonal

A diagonal matrix has elements along its diagonal and zeroes elsewhere (e.g., the identity matrix). Let $\mathbf { x } = \left[ x _ { 1 } \quad \ldots \quad x _ { n } \right] ^ { \mathsf { T } }$ .

$$
\operatorname{diag} (\mathbf {x}) = \operatorname{diag} (x _ {1}, \ldots , x _ {n}) = \left[ \begin{array}{c c c c} x _ {1} & 0 & \dots & 0 \\ 0 & x _ {2} & & \vdots \\ \vdots & & \ddots & 0 \\ 0 & \dots & 0 & x _ {n} \end{array} \right]
$$

A block diagonal matrix has matrices along its diagonal. diag() works similarly for constructing one. Let $\mathbf { A } = \left[ \begin{array} { l } { 1 } { 2 } \\ { 3 } \end{array} \right]$ and $\mathbf { B } = \left[ { \begin{array} { l l } { 1 \mathrm { ~ 2 ~ 3 ~ } } \\ { 4 \mathrm { ~ 5 ~ 6 ~ } } \\ { 7 \mathrm { ~ 8 ~ 9 ~ } } \end{array} } \right]$ i.

$$
\operatorname{diag} (\mathbf {A}, \mathbf {B}) = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ \mathbf {0} & \mathbf {B} \end{array} \right] = \left[ \begin{array}{c c c c c} 1 & 2 & 0 & 0 & 0 \\ 3 & 4 & 0 & 0 & 0 \\ 0 & 0 & 1 & 2 & 3 \\ 0 & 0 & 4 & 5 & 6 \\ 0 & 0 & 7 & 8 & 9 \end{array} \right]
$$

Operations on the diag() argument are applied element-wise.

$$
\operatorname{diag} \left(\frac {1}{\mathbf {x} ^ {2}}\right) = \left[ \begin{array}{c c c c} \frac {1}{x _ {1} ^ {2}} & 0 & \dots & 0 \\ 0 & \frac {1}{x _ {2} ^ {2}} & & \vdots \\ \vdots & & \ddots & 0 \\ 0 & \dots & 0 & \frac {1}{x _ {n} ^ {2}} \end{array} \right]
$$

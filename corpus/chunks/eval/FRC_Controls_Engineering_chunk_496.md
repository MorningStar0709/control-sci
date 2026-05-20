$$\mathbf {u} _ {k} = - \mathbf {K x} _ {k + L / T}
\mathbf {u} _ {k} = \left\{ \begin{array}{l l} - \mathbf {K} (\mathbf {A} - \mathbf {B K}) ^ {k} \mathbf {A} ^ {\frac {L}{T} - k} \mathbf {x} _ {k} & \text { if } 0 \leq k <   \frac {L}{T} \\ - \mathbf {K} (\mathbf {A} - \mathbf {B K}) ^ {\frac {L}{T}} \mathbf {x} _ {k} & \text { if } k \geq \frac {L}{T} \end{array} \right. \tag {B.13}
$$

If the delay L isn’t a multiple of the sample period T in equation (B.13), we have to evaluate fractional matrix powers, which can be tricky. Eigen (a C++ library) supports fractional powers with the pow() member function provided by

<unsupported/Eigen/MatrixFunctions>. SciPy (a Python library) supports fractional powers with the free function

scipy.linalg.fractional\_matrix\_power(). If the language you’re using doesn’t provide such a function, you can try the following approach instead.

Let there be a matrix M raised to a fractional power n. If M is diagonalizable, we can obtain an exact answer for ${ \bf M } ^ { n }$ by decomposing M into $\mathbf { P D P ^ { - 1 } }$ where D is a diagonal matrix, computing $\mathbf { D } ^ { n }$ as each diagonal element raised to n, then recomposing ${ \bf M } ^ { n }$ as $\mathbf { P D } ^ { n } \mathbf { P } ^ { - 1 }$ .

If a matrix raised to a fractional power in equation (B.13) isn’t diagonalizable, we have to approximate by rounding $\textstyle { \frac { L } { T } }$ to the nearest integer. This approximation gets worse as L mod T approaches $\textstyle { \frac { T } { 2 } }$ .

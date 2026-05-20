$$
\begin{array}{l} \operatorname{tr} \left(\mathbf {P} _ {k + 1} ^ {+}\right) = \operatorname{tr} \left(\mathbf {P} _ {k + 1} ^ {-}\right) - \operatorname{tr} \left(\left(\mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {- \top}\right) ^ {\top}\right) - \operatorname{tr} \left(\mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-}\right) \\ + \mathrm{tr} (\mathbf {K} _ {k + 1} \mathbf {S} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top}) \\ \end{array}
$$

$\mathbf { P } _ { k + 1 } ^ { - }$ is symmetric, so we can drop the transpose.

$$
\begin{array}{l} \operatorname{tr} \left(\mathbf {P} _ {k + 1} ^ {+}\right) = \operatorname{tr} \left(\mathbf {P} _ {k + 1} ^ {-}\right) - \operatorname{tr} \left(\left(\mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-}\right) ^ {\top}\right) - \operatorname{tr} \left(\mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-}\right) \\ + \operatorname{tr} (\mathbf {K} _ {k + 1} \mathbf {S} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top}) \\ \end{array}
$$

The trace of a matrix is equal to the trace of its transpose since the elements used in the trace are on the diagonal.

$$
\begin{array}{l} \operatorname{tr} \left(\mathbf {P} _ {k + 1} ^ {+}\right) = \operatorname{tr} \left(\mathbf {P} _ {k + 1} ^ {-}\right) - \operatorname{tr} \left(\mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-}\right) - \operatorname{tr} \left(\mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-}\right) \\ + \operatorname{tr} (\mathbf {K} _ {k + 1} \mathbf {S} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top}) \\ \end{array}
\operatorname{tr} \left(\mathbf {P} _ {k + 1} ^ {+}\right) = \operatorname{tr} \left(\mathbf {P} _ {k + 1} ^ {-}\right) - 2 \operatorname{tr} \left(\mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-}\right) + \operatorname{tr} \left(\mathbf {K} _ {k + 1} \mathbf {S} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top}\right)
$$

Given theorems 9.6.1 and 9.6.2

Theorem 9.6.1 $\begin{array} { r } { { \frac { \partial } { \partial { \bf A } } } \operatorname { t r } ( { \bf A } { \bf B } { \bf A } ^ { \top } ) = 2 { \bf A } { \bf B } } \end{array}$ where B is symmetric.

Theorem 9.6.2 $\begin{array} { r } { { \frac { \partial } { \partial { \bf A } } } \operatorname { t r } ( { \bf A C } ) = { \bf C } ^ { \top } } \end{array}$

find the minimum of the trace of $\mathbf { P } _ { k + 1 } ^ { + }$ by taking the partial derivative with respect to K and setting the result to 0.

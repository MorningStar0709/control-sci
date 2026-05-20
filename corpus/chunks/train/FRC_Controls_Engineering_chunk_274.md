# 9.3.7 Independence

Two random variables are independent if the following relation is true.

$$p (x, y) = p (x) p (y)$$

This means that the values of x do not correlate with the values of y. That is, the outcome of one random variable does not affect another’s outcome. If we assume

independence,

$$
\begin{array}{l} E [ x y ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} x y p (x, y) d x d y \\ E [ x y ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} x y p (x) p (y) d x d y \\ E [ x y ] = \int_ {- \infty} ^ {\infty} x p (x) d x \int_ {- \infty} ^ {\infty} y p (y) d y \\ E [ x y ] = E [ x ] E [ y ] \\ E [ x y ] = \overline {{{x}}} \overline {{{y}}} \\ \end{array}

\begin{array}{l} \operatorname{cov} (x, y) = E [ (x - \overline {{x}}) (y - \overline {{y}}) ] \\ \operatorname{cov} (x, y) = E [ (x - \overline {{x}}) ] E [ (y - \overline {{y}}) ] \\ \operatorname{cov} (x, y) = 0 \cdot 0 \\ \end{array}
$$

Therefore, the covariance $\Sigma _ { x y }$ is zero, as expected. Furthermore, $\rho ( x , y ) = 0$ , which means they are uncorrelated.

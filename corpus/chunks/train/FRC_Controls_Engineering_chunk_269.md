# 9.3.2 Expected value

Expected value or expectation is a weighted average of the values the PDF can produce where the weight for each value is the probability of that value occurring. This can be

written mathematically as

$$\overline {{{{x}}}} = E [ x ] = \int_ {- \infty} ^ {\infty} x p (x) d x$$

The expectation can be applied to random functions as well as random variables.

$$E [ f (x) ] = \int_ {- \infty} ^ {\infty} f (x) p (x) d x$$

The mean of a random variable is denoted by an overbar $( \mathrm { e } . \mathrm { g } . , \overline { { x } } )$ pronounced x-bar. The expectation of the difference between a random variable and its mean $x - { \overline { { x } } }$ converges to zero. In other words, the expectation of a random variable is its mean. Here’s a proof.

$$
\begin{array}{l} E [ x - \bar {x} ] = \int_ {- \infty} ^ {\infty} (x - \bar {x}) p (x) d x \\ E [ x - \overline {{x}} ] = \int_ {- \infty} ^ {\infty} x   p (x)   d x - \int_ {- \infty} ^ {\infty} \overline {{x}}   p (x)   d x \\ E [ x - \overline {{x}} ] = \int_ {- \infty} ^ {\infty} x p (x) d x - \overline {{x}} \int_ {- \infty} ^ {\infty} p (x) d x \\ E [ x - \overline {{x}} ] = \overline {{x}} - \overline {{x}} \cdot 1 \\ E [ x - \overline {{x}} ] = 0 \\ \end{array}
$$

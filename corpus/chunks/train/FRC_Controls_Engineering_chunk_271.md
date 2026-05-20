# 9.3.4 Joint probability density functions

Probability density functions can also include more than one variable. Let x and y be random variables. The joint probability density function $p ( x , y )$ defines the probability $p ( x , y )$ dx $d y$ , so that x and y are in the intervals $x \in [ x , x + d x ] , y \in [ y , y + d y ]$ . In other words, the probability is the volume under a region of the PDF manifold (see figure 9.2 for an example of a joint PDF).

Joint probability density functions also require that no probabilities are negative and that the sum of all probabilities is 1.

$$p (x, y) \geq 0, \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} p (x, y) d x d y = 1$$

The expected values for joint PDFs are as follows.

$$E [ x ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} x p (x, y) d x d yE [ y ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} y p (x, y) d x d yE [ f (x, y) ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} f (x, y) p (x, y) d x d y$$

The variance of a joint PDF measures how a variable correlates with itself (we’ll cover variances with respect to other variables shortly).

$$\operatorname{var} (x) = \Sigma_ {x x} = E [ (x - \bar {x}) ^ {2} ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} (x - \bar {x}) ^ {2} p (x, y) d x d y\mathrm{var} (y) = \Sigma_ {y y} = E [ (y - \overline {{y}}) ^ {2} ] = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} (y - \overline {{y}}) ^ {2} p (x, y) d x d y$$

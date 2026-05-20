# Example A.45: More normal conditional densities

Let the joint conditional of random variables a and b given c be a normal distribution with

$$
p (a, b \mid c) \sim N \left(\left[ \begin{array}{l} m _ {a} \\ m _ {b} \end{array} \right], \left[ \begin{array}{c c} P _ {a} & P _ {a b} \\ P _ {b a} & P _ {b} \end{array} \right]\right) \tag {A.39}
$$

Then the conditional density of a given b and c is also normal

$$p (a | b, c) \sim N (m, P)$$

in which the mean is

$$m = m _ {a} + P _ {a b} P _ {b} ^ {- 1} (b - m _ {b})$$

and the covariance is

$$P = P _ {a} - P _ {a b} P _ {b} ^ {- 1} P _ {b a}$$

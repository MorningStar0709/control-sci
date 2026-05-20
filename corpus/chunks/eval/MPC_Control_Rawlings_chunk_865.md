$$p _ {\xi} (x) = \frac {1}{(2 \pi) ^ {n _ {x} / 2} (\det (P) \det (\tilde {P} _ {y})) ^ {1 / 2}} \exp \left(- (1 / 2) \bar {x} ^ {\prime} (\tilde {P} _ {x} - \tilde {P} _ {y x} ^ {\prime} \tilde {P} _ {y} ^ {- 1} \tilde {P} _ {y x}) \bar {x}\right)$$

From the matrix inversion formula we conclude

$$\tilde {P} _ {x} - \tilde {P} _ {x y} ^ {\prime} \tilde {P} _ {y} ^ {- 1} \tilde {P} _ {y x} = P _ {x} ^ {- 1}$$

and

$$\det (P) = \det (P _ {x}) \det (P _ {y} - P _ {y x} P _ {x} ^ {- 1} P _ {x y}) = \det P _ {x} \det \tilde {P} _ {y} ^ {- 1} = \frac {\det P _ {x}}{\det \tilde {P} _ {y}}$$

Substituting these results into the previous equation gives

$$p _ {\xi} (x) = \frac {1}{(2 \pi) ^ {n _ {x} / 2} (\det P _ {x}) ^ {1 / 2}} \exp \left(- (1 / 2) \bar {x} ^ {\prime} P _ {x} ^ {- 1} \bar {x}\right)$$

Therefore

$$\xi \sim N (m _ {x}, P _ {x})$$

\-

![](image/773b742c40361bd9db42fd269b3e35374227452731cee85dff8c825eb158bd51.jpg)  
Figure A.11: A nearly singular normal density in two dimensions.

Functions of random variables. In stochastic dynamical systems we need to know how the density of a random variable is related to the density of a function of that random variable. Let $f : \mathbb { R } ^ { n } \to \mathbb { R } ^ { n }$ be a mapping of the random variable $\xi$ into the random variable η and assume that the inverse mapping also exits

$$\eta = f (\xi), \quad \xi = f ^ {- 1} (\eta)$$

Given the density of $\xi , p _ { \xi } ( x )$ , we wish to compute the density of $\eta .$ , $p _ { \eta } ( y )$ , induced by the function $f .$ . Let S denote an arbitrary region of the field of the random variable $\xi$ and define the set $S ^ { \prime }$ as the transform of this set under the function f

$$S ^ {\prime} = \{y | y = f (x), x \in S \}$$

Then we seek a function $p _ { \eta } ( y )$ such that

$$\int_ {S} p _ {\xi} (x) d x = \int_ {S ^ {\prime}} p _ {\eta} (y) d y \tag {A.27}$$

for every admissible set S. Using the rules of calculus for transforming a variable of integration we can write

$$\int_ {S} p _ {\xi} (x) d x = \int_ {S ^ {\prime}} p _ {\xi} (f ^ {- 1} (y)) \left| \det \left(\frac {\partial f ^ {- 1} (y)}{\partial y}\right) \right| d y \tag {A.28}$$

in which $\left| { \operatorname* { d e t } ( \partial f ^ { - 1 } ( y ) / \partial y } ) \right|$ is the absolute value of the determinant of the Jacobian matrix of the transformation from η to $\xi .$ . Subtracting (A.28) from (A.27) gives

$$\int_ {S ^ {\prime}} \left(p _ {\eta} (y) - p _ {\xi} (f ^ {- 1} (y)) \left| \det (\partial f ^ {- 1} (y) / \partial y) \right|\right) d y = 0 \tag {A.29}$$

Because (A.29) must be true for any set $S ^ { \prime }$ , we conclude (a proof by contradiction is immediate)8

$$\boxed {p _ {\eta} (y) = p _ {\xi} \left(f ^ {- 1} (y)\right) \left| \det \left(\partial f ^ {- 1} (y) / \partial y\right) \right|} \tag {A.30}$$

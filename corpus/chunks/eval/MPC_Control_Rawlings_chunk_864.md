# Solution

As a first approach to establish (A.25), we directly integrate the $_ y$ variables. Let ${ \bar { x } } = x - m _ { x }$ and $\bar { y } = y - m _ { y }$ , and $n _ { x }$ and $n _ { y }$ be the dimension of the $\xi$ and $\eta$ variables, respectively, and $n = n _ { x } + n _ { y }$ . Then the definition of the marginal density gives

$$
p _ {\xi} (x) = \frac {1}{(2 \pi) ^ {n / 2} (\det P) ^ {1 / 2}} \int_ {- \infty} ^ {\infty} \exp \left[ - \frac {1}{2} \left[ \begin{array}{c} \bar {x} \\ \bar {y} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} P _ {x} & P _ {x y} \\ P _ {y x} & P _ {y} \end{array} \right] ^ {- 1} \left[ \begin{array}{c} \bar {x} \\ \bar {y} \end{array} \right] \right] d \bar {y}
$$

Let the inverse of P be denoted as $\tilde { P }$ and partition $\tilde { P }$ as follows

$$
\left[ \begin{array}{l l} P _ {x} & P _ {x y} \\ P _ {y x} & P _ {y} \end{array} \right] ^ {- 1} = \left[ \begin{array}{l l} \tilde {P} _ {x} & \tilde {P} _ {x y} \\ \tilde {P} _ {y x} & \tilde {P} _ {y} \end{array} \right] \tag {A.26}
$$

Substituting (A.26) into the definition of the marginal density and expanding the quadratic form in the exponential yields

$$(2 \pi) ^ {n / 2} (\det P) ^ {1 / 2} p _ {\xi} (x) =\exp \left(- (1 / 2) \bar {x} ^ {\prime} \tilde {P} _ {x} \bar {x}\right) \int_ {- \infty} ^ {\infty} \exp \left(- (1 / 2) (2 \bar {y} ^ {\prime} \tilde {P} _ {y x} \bar {x} + \bar {y} ^ {\prime} \tilde {P} _ {y} \bar {y})\right) d \bar {y}$$

We complete the square on the term in the integral by noting that

$$(\bar {y} + \tilde {P} _ {y} ^ {- 1} \tilde {P} _ {y x} \bar {x}) ^ {\prime} \tilde {P} _ {y} (\bar {y} + \tilde {P} _ {y} ^ {- 1} \tilde {P} _ {y x} \bar {x}) = \bar {y} ^ {\prime} \tilde {P} _ {y} \bar {y} + 2 \bar {y} ^ {\prime} \tilde {P} _ {y x} \bar {x} + \bar {x} ^ {\prime} \tilde {P} _ {y x} ^ {\prime} \tilde {P} _ {y} ^ {- 1} \tilde {P} _ {y x} \bar {x}$$

Substituting this relation into the previous equation gives

$$(2 \pi) ^ {n / 2} (\det P) ^ {1 / 2} p _ {\xi} (x) = \exp \left(- (1 / 2) \bar {x} ^ {\prime} (\tilde {P} _ {x} - \tilde {P} _ {y x} ^ {\prime} \tilde {P} _ {y} ^ {- 1} \tilde {P} _ {y x}) \bar {x}\right)\int_ {- \infty} ^ {\infty} \exp \left(- (1 / 2) (\bar {y} + a) ^ {\prime} \tilde {P} _ {y} (\bar {y} + a)\right) d \bar {y}$$

in which $a = \widetilde { P } _ { y } ^ { - 1 } \widetilde { P } _ { y x } \bar { x }$ . Using (A.22) to evaluate the integral gives

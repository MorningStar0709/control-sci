$$Q = X (I + Y X) ^ {- 1}$$

where $X = X ^ { * } \geq 0$ is the stabilizing solution to

$$X A + A ^ {*} X - X B B ^ {*} X + C ^ {*} C = 0.$$

Hence balancing Y and $Q$ is equivalent to balancing X and $Y .$ . This is called Riccati balancing; see Jonckheere and Silverman [1983].)

Problem 16.14 Apply the controller reduction methods in the last three problems, $G ( s ) = \left[ { \frac { A \mid B } { C \mid 0 } } \right]$ A respectively, to a satellite system where

$$
A = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & - 1. 5 3 9 ^ {2} & - 2 \times 0. 0 0 3 \times 1. 5 3 9 \end{array} \right], \quad B = \left[ \begin{array}{c} 0 \\ 1. 7 3 1 9 \times 1 0 ^ {- 5} \\ 0 \\ 3. 7 8 5 9 \times 1 0 ^ {- 4} \end{array} \right],

C = \left[ \begin{array}{l l l l} 1 & 0 & 1 & 0 \end{array} \right], \quad D = 0.
$$

Compare the results (see McFarlane and Glover [1990] for further details).

Problem 16.15 Let $f ( s )$ be analytic in the closed right-half plane and suppose

$$\lim _ {r \to \infty} \max _ {\theta \in [ - \pi / 2, \pi / 2 ]} \frac {| f (r e ^ {j \theta})}{r} = 0.$$

Then the Poisson integral formula (see, for example, Freudenberg and Looze [1988], page 37) says that $f ( s )$ at any point $s = x + j y$ in the open right-half plane can be recovered from $f ( j \omega )$ via the integral relation:

$$f (s) = \frac {1}{\pi} \int_ {- \infty} ^ {\infty} f (j \omega) \frac {x}{x ^ {2} + (y - \omega) ^ {2}} d \omega .$$

Let $s = r e ^ { j \theta } \ ( { \mathrm { i . e . , } } \ x = r$ cos θ and $y = r \sin \theta )$ with $r > 0$ and $- \pi / 2 < \theta < \pi / 2$ . Suppose $f ( j \omega ) = f ( - j \omega )$ . Show that

$$f (r e ^ {j \theta}) = \int_ {- \infty} ^ {\infty} f (j \omega) K _ {\theta} (\omega / r) d (\ln \omega)$$

where

$$K _ {\theta} (\omega / r) = \frac {1}{\pi} \frac {2 (\omega / r) [ 1 + (\omega / r) ^ {2} ] \cos \theta}{[ 1 - (\omega / r) ^ {2} ] ^ {2} + 4 (\omega / r) ^ {2} \cos^ {2} \theta}$$

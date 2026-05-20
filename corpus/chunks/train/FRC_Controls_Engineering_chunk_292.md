# 9.5.1 Two noisy (independent) observations

Variable $z _ { 1 }$ is the noisy measurement of the variable x. The value of the noisy measurement is the random variable defined by the probability density function $p ( z _ { 1 } | x )$ .

Variable $z _ { 2 }$ is the noisy measurement of the same variable x and independent of $z _ { 1 }$ . If we know the property of our sensor (measurement noise), then the probability density function of the measurement is $p ( z _ { 2 } | x )$ .

We are interested in the probability density function of x given the measurements $z _ { 1 }$ and $z _ { 2 }$ .

$$p (x | z _ {1}, z _ {2}) = \frac {p (x , z _ {1} , z _ {2})}{p (z _ {1} , z _ {2})} = \frac {p (z _ {1} , z _ {2} | x) p (x)}{p (z _ {1} , z _ {2})} = \frac {p (z _ {1} | x) p (z _ {2} | x) p (x)}{p (z _ {1} , z _ {2})}$$

where $\begin{array} { r } { p ( z _ { 1 } , z _ { 2 } ) = \int _ { X } p ( z _ { 1 } | x ) p ( z _ { 2 } | x ) } \end{array}$ dx, but $z _ { 1 }$ and $z _ { 2 }$ are given and we can write

$$p (x | z _ {1}, z _ {2}) = \frac {1}{C} p (z _ {1} | x) p (z _ {2} | x) p (x) \quad \mathrm{or} \quad p (x | z _ {1}, z _ {2}) \sim p (z _ {1} | x) p (z _ {2} | x) p (x)$$

where C is a normalizing constant providing that $\begin{array} { r } { \int _ { X } p ( x | z _ { 1 } , z _ { 2 } ) d x = 1 } \end{array}$ . The probability density $p ( x | z _ { 1 } , z _ { 2 } )$ summarizes our complete knowledge about x.

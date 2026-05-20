# A.15 Random Variables and the Probability Density

Let $\xi$ be a random variable taking values in the field of real numbers and the function $F _ { \xi } ( x )$ denote the probability distribution function of the random variable so that

$$F _ {\xi} (x) = \operatorname * {P r} (\xi \leq x)$$

i.e., $F _ { \xi } ( x )$ is the probability that the random variable $\xi$ takes on a value less than or equal to x. $F _ { \xi }$ is obviously a nonnegative, nondecreasing function and has the following properties due to the axioms of probability

$$F _ {\xi} (x _ {1}) \leq F _ {\xi} (x _ {2}) \quad \text { if } x _ {1} < x _ {2}\lim _ {x \rightarrow - \infty} F _ {\xi} (x) = 0\lim _ {x \to \infty} F _ {\xi} (x) = 1$$

We next define the probability density function, denoted $p _ { \xi } ( x )$ , such that

$$F _ {\xi} (x) = \int_ {- \infty} ^ {x} p _ {\xi} (s) d s, \quad - \infty < x < \infty \tag {A.20}$$

We can allow discontinuous $F _ { \xi }$ if we are willing to accept generalized functions (delta functions and the like) for $p _ { \xi }$ . Also, we can define the density function for discrete as well as continuous random variables if we allow delta functions. Alternatively, we can replace the integral in (A.20) with a sum over a discrete density function. The random variable may be a coin toss or a dice game, which takes on values from a discrete set contrasted to a temperature or concentration measurement, which takes on a values from a continuous set. The density function has the following properties

$$p _ {\xi} (x) \geq 0\int_ {- \infty} ^ {\infty} p _ {\xi} (x) d x = 1$$

and the interpretation in terms of probability

$$\operatorname * {P r} (x _ {1} \leq \xi \leq x _ {2}) = \int_ {x _ {1}} ^ {x _ {2}} p _ {\xi} (x) d x$$

The mean or expectation of a random variable $\xi$ is defined as

$$\mathcal {E} (\xi) = \int_ {- \infty} ^ {\infty} x p _ {\xi} (x) d x$$

The moments of a random variable are defined by

$$\mathcal {E} (\xi^ {n}) = \int_ {- \infty} ^ {\infty} x ^ {n} p _ {\xi} (x) d x$$

and it is clear that the mean is the zeroth moment. Moments of $\xi$ about the mean are defined by

$$\mathcal {E} ((\xi - \mathcal {E} (\xi)) ^ {n}) = \int_ {- \infty} ^ {\infty} (x - \mathcal {E} (\xi)) ^ {n} p _ {\xi} (x) d x$$

and the variance is defined as the second moment about the mean

$$\operatorname{var} (\xi) = \mathcal {E} ((\xi - \mathcal {E} (\xi)) ^ {2}) = \mathcal {E} (\xi^ {2}) - \mathcal {E} ^ {2} (\xi)$$

The standard deviation is the square root of the variance

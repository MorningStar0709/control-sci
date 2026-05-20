# 4.7.3 Resampling

Consider a set of samples at $x = x _ { i } , i = 1 , \dots s$ and associated normalized weights wi, $w _ { i } \geq 0 , \sum _ { i = 1 } ^ { s } w _ { i } = 1$ . Define a probability density using these samples and weights by

$$p (x) = \sum_ {i = 1} ^ {s} w _ {i} \delta (x - x _ {i})$$

Consider any function $f ( x )$ defined on a set that contains the samples, $x _ { i }$ . Then the integral of f using the defined density is

$$\int f (x) p (x) d x = \sum_ {i = 1} ^ {s} w _ {i} f (x _ {i}) = \sum_ {i = 1} ^ {s} w _ {i} f _ {i}$$

in which $f _ { i } = f ( x _ { i } )$ . We now consider a resampling procedure that produces a new set of samples $\tilde { x } _ { i }$ with new weights $\tilde { \boldsymbol { w } } _ { i }$ . The resampling procedure is depicted in Figure 4.20 for the case $s = 3$ . We partition the interval [0, 1] into s intervals using the original sample weights, $w _ { i }$ , as shown in Figure 4.20, in which the ith interval has width $w _ { i }$ . To choose s resamples, we generate s random numbers from a uniform distribution on [0, 1]. Denote these random numbers as $u _ { i } , i = 1 , \ldots , s$ . For each i, we find the interval in which the drawn random number falls. Denote the interval number as m(i), defined by the relation

$$0 \leq w _ {1} + w _ {2} + \dots + w _ {m (i) - 1} \leq u _ {i} \leq w _ {1} + w _ {2} + \dots + w _ {m (i)} \leq 1$$

We then choose as resamples

$$\tilde {x} _ {i} = x _ {m (i)} \qquad i = 1, \ldots s$$

The resampling selects the new sample locations $\tilde { x }$ in regions of high density. We set all the $\tilde { { w } }$ weights equal to $1 / s .$ . The result illustrated in Figure 4.20 is summarized in the following table

<table><tr><td colspan="2">Original sample</td><td colspan="2">Resample</td></tr><tr><td>State</td><td>Weight</td><td>State</td><td>Weight</td></tr><tr><td> $x_{1}$ </td><td> $w_{1} = \frac{3}{10}$ </td><td> $\tilde{x}_{1} = x_{1}$ </td><td> $\tilde{w}_{1} = \frac{1}{3}$ </td></tr><tr><td> $x_{2}$ </td><td> $w_{2} = \frac{1}{10}$ </td><td> $\tilde{x}_{2} = x_{3}$ </td><td> $\tilde{w}_{2} = \frac{1}{3}$ </td></tr><tr><td> $x_{3}$ </td><td> $w_{3} = \frac{6}{10}$ </td><td> $\tilde{x}_{3} = x_{3}$ </td><td> $\tilde{w}_{3} = \frac{1}{3}$ </td></tr></table>

The properties of the resamples are summarized by

$$
p _ {\mathrm{re}} (\tilde {x} _ {i}) = \left\{ \begin{array}{l l} w _ {j} & \tilde {x} _ {i} = x _ {j} \\ 0 & \tilde {x} _ {i} \neq x _ {j} \end{array} \right.
\tilde {w} _ {i} = 1 / s \quad \mathrm{all} i
$$

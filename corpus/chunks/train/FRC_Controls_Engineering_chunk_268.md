# 9.3.1 Random variables

A random variable is a variable whose values are the outcomes of a random phenomenon, like dice rolls or noisy process measurements. As such, a random variable is defined as a function that maps the outcomes of an unpredictable process to numerical quantities. A particular output of this function is called a sample. The sample space is the set of possible values taken by the random variable.

![](image/35bdf082c0654c98796b74dbcd441438177a1723c6e820f0fdbdf3df3a8fc1d0.jpg)

<details>
<summary>line</summary>

| x | p(x) |
| --- | --- |
| 0.0 | 0.200 |
| 2.5 | 0.180 |
| 5.0 | 0.050 |
| 7.5 | 0.010 |
| 10.0 | 0.000 |
</details>

Figure 9.1: Probability density function

A probability density function (PDF) is a function of the random variable whose value at a given sample (measured value) in the sample space (the range of possible measured values) is the probability of that sample occurring. The area under the function over a range gives the probability that the sample falls within that range. Let x be a random variable, and let $p ( x )$ denote the probability density function of x. The probability that the value of x will be in the interval $x \in [ x _ { 1 } , x _ { 1 } + d x ] { \mathrm { ~ i s ~ } } p ( x _ { 1 } )$ dx. In other words, the probability is the area under the PDF within the region $[ x _ { 1 } , x _ { 1 } + d x ]$ (see figure 9.1).

A probability of zero means that the sample will not occur and a probability of one means that the sample will always occur. Probability density functions require that no probabilities are negative and that the sum of all probabilities is 1. If the probabilities sum to 1, that means one of those outcomes must happen. In other words,

$$p (x) \geq 0, \int_ {- \infty} ^ {\infty} p (x) d x = 1$$

or given that the probability of a given sample is greater than or equal to zero, the sum of probabilities for all possible input values is equal to one.

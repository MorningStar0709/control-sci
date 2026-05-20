$$
\begin{array}{l} p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \frac {\sigma_ {0} ^ {2} + \sigma^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}}} \bigg (x ^ {2} - 2 \mu x + \mu^ {2} - \mu^ {2} + \frac {\sigma_ {0} ^ {2} z _ {1} ^ {2} + \sigma^ {2} x _ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} \bigg) \\ p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \frac {\sigma_ {0} ^ {2} + \sigma^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} \left((x - \mu) ^ {2} - \mu^ {2} + \frac {\sigma_ {0} ^ {2} z _ {1} ^ {2} + \sigma^ {2} x _ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}}\right)} \\ \end{array}
$$

Pull out all constant terms in the exponent and combine them with $C _ { 1 }$ to make a new constant $C _ { 2 }$ . We’re basically doing $c _ { 1 } e ^ { x + a }  c _ { 1 } e ^ { a } e ^ { x }  c _ { 2 } e ^ { x }$ .

$$p (x | z _ {1}) = \frac {1}{C _ {2}} e ^ {- \frac {1}{2} \frac {\sigma_ {0} ^ {2} + \sigma^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} (x - \mu) ^ {2}}$$

This means that if we’re given an initial estimate $x _ { 0 }$ and a measurement $z _ { 1 }$ with associated means and variances represented by Gaussian distributions, this information can be combined into a third Gaussian distribution with its own mean value and variance. The expected value of x given $z _ { 1 }$ is

$$E [ x | z _ {1} ] = \mu = \frac {\sigma_ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} z _ {1} + \frac {\sigma^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} x _ {0} \tag {9.11}$$

The variance of x given $z _ { 1 }$ is

$$E [ (x - \mu) ^ {2} | z _ {1} ] = \frac {\sigma^ {2} \sigma_ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} \tag {9.12}$$

The expected value, which is also the maximum likelihood value, is the linear combination of the prior expected (maximum likelihood) value and the measurement. The expected value is a reasonable estimator of x.

$$\hat {x} = E [ x | z _ {1} ] = \frac {\sigma_ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} z _ {1} + \frac {\sigma^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} x _ {0} \tag {9.13}\hat {x} = w _ {1} z _ {1} + w _ {2} x _ {0}$$

Note that the weights $w _ { 1 }$ and $w _ { 2 }$ sum to 1. When the prior (i.e., prior knowledge of state) is uninformative (a large variance),

$$w _ {1} = \lim _ {\sigma_ {0} ^ {2} \rightarrow \infty} \frac {\sigma_ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} = 1 \tag {9.14}w _ {2} = \lim _ {\sigma_ {0} ^ {2} \rightarrow \infty} \frac {\sigma^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} = 0 \tag {9.15}$$

and $\hat { x } = z _ { 1 }$ . That is, the weight is on the observations and the estimate is equal to the measurement.

Let us assume we have a model providing an almost exact prior for x. In that case, $\sigma _ { 0 } ^ { 2 }$ approaches 0 and

$$w _ {1} = \lim _ {\sigma_ {0} ^ {2} \rightarrow 0} \frac {\sigma_ {0} ^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} = 0 \tag {9.16}w _ {2} = \lim _ {\sigma_ {0} ^ {2} \rightarrow 0} \frac {\sigma^ {2}}{\sigma_ {0} ^ {2} + \sigma^ {2}} = 1 \tag {9.17}$$

The Kalman filter uses this optimal fusion as the basis for its operation.

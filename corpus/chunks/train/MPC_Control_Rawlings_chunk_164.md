in which $\overline { { \theta } }$ and $P _ { 0 }$ are chosen by the user. In Bayesian estimation, we call $\overline { { \theta } }$ and $P _ { 0 }$ the prior information, and often assume that the prior density of θ (without measurements) is normal

$$\theta \sim N (\overline {{\theta}}, P _ {0})$$

The solution to this modified least squares estimation problem is

$$\widehat {\theta} = \overline {{{\theta}}} + (X ^ {\prime} X + P _ {0} ^ {- 1}) ^ {- 1} X ^ {\prime} (\mathcal {Y} - X \overline {{{\theta}}}) \tag {1.64}$$

Devise a means to recursively estimate θ so that:

1. We never store more than one measurement at a time in memory.

2. After processing all the measurements, we obtain the same least squares estimate given in (1.64).

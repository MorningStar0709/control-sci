# Example 2.8 Simple paper-machine model

Determine the zero-order-hold sampling of the system (see Example A.4).

$$\frac {d x (t)}{d t} = - x (t) + u (t - 2. 6)$$

with sampling interval $h = 1$ . In this case $d = 3$ and $\tau' = 0.6$ , and (2.12) becomes

$$x (k + 1) = \Phi x (k) + \Gamma_ {0} u (k - 2) + \Gamma_ {1} u (k - 3)$$

where

$$\Phi = e ^ {- 1} = 0. 3 6 7 9\Gamma_ {0} = \int_ {0} ^ {0. 4} e ^ {- s} d s = 1 - e ^ {- 0. 4} = 0. 3 2 9 7\Gamma_ {1} = e ^ {- 0. 4} \int_ {0} ^ {0. 6} e ^ {- s} d s = e ^ {- 0. 4} - e ^ {- 1} = 0. 3 0 2 4$$

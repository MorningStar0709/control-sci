$$
\begin{array}{l} - \int_ {\omega_ {h}} ^ {\infty} \ln \left(1 - \frac {M _ {h}}{\omega^ {1 + \beta}}\right) d \omega = \sum_ {i = 1} ^ {\infty} \int_ {\omega_ {h}} ^ {\infty} \frac {1}{i} \left(\frac {M _ {h}}{\omega^ {1 + \beta}}\right) ^ {i} d \omega \\ = \sum_ {i = 1} ^ {\infty} \frac {1}{i} \frac {\omega_ {h}}{i (1 + \beta) - 1} \left(\frac {M _ {h}}{\omega_ {h} ^ {1 + \beta}}\right) ^ {i} \\ \leq \frac {\omega_ {h}}{\beta} \sum_ {i = 1} ^ {\infty} \frac {1}{i} \left(\frac {M _ {h}}{\omega_ {h} ^ {1 + \beta}}\right) ^ {i} = - \frac {\omega_ {h}}{\beta} \ln \left(1 - \frac {M _ {h}}{\omega_ {h} ^ {1 + \beta}}\right) \\ \leq - \frac {\omega_ {h}}{\beta} \ln (1 - \tilde {\epsilon}). \\ \end{array}
$$

Then

$$\pi \sum_ {i = 1} ^ {m} \operatorname{Re} (p _ {i}) = \int_ {0} ^ {\infty} \ln | S (j \omega) | d \omega= \int_ {0} ^ {\omega_ {l}} \ln | S (j \omega) | d \omega + \int_ {\omega_ {l}} ^ {\omega_ {h}} \ln | S (j \omega) | d \omega + \int_ {\omega_ {h}} ^ {\infty} \ln | S (j \omega) | d \omega\leq \omega_ {l} \ln \epsilon + (\omega_ {h} - \omega_ {l}) \max _ {\omega \in [ \omega_ {l}, \omega_ {h} ]} \ln | S (j \omega) | - \int_ {\omega_ {h}} ^ {\infty} \ln \left(1 - \frac {M _ {h}}{\omega^ {1 + \beta}}\right) d \omega\leq \omega_ {l} \ln \epsilon + (\omega_ {h} - \omega_ {l}) \max _ {\omega \in [ \omega_ {l}, \omega_ {h} ]} \ln | S (j \omega) | - \frac {\omega_ {h}}{\beta} \ln (1 - \tilde {\epsilon}),$$

which gives

$$\max _ {\omega \in [ \omega_ {l}, \omega_ {h} ]} | S (j \omega) | \geq e ^ {\alpha} \left(\frac {1}{\epsilon}\right) ^ {\frac {\omega_ {l}}{\omega_ {h} - \omega_ {l}}} (1 - \tilde {\epsilon}) ^ {\frac {\omega_ {h}}{\beta (\omega_ {h} - \omega_ {l})}}$$

where

$$\alpha = \frac {\pi \sum_ {i = 1} ^ {m} \mathrm{Re} (p _ {i})}{\omega_ {h} - \omega_ {l}}.$$

The above lower bound shows that the sensitivity can be very significant in the transition band.

Next, using the Poisson integral relation, we investigate the design constraints on sensitivity properties imposed by open-loop nonminimum phase zeros. Suppose L has at least one more poles than zeros and suppose $z = x _ { 0 } + j y _ { 0 }$ with $x _ { 0 } > 0$ is a right-half plane zero of L. Then

$$\int_ {- \infty} ^ {\infty} \ln | S (j \omega) | \frac {x _ {0}}{x _ {0} ^ {2} + (\omega - y _ {0}) ^ {2}} d \omega = \pi \ln \prod_ {i = 1} ^ {m} \left| \frac {z + p _ {i}}{z - p _ {i}} \right| \tag {6.17}$$

# 14.4 Minimum Entropy Controller

Let T be a transfer matrix with $\| T \| _ { \infty } < \gamma$ . Then the entropy of $T ( s )$ is defined by

$$I (T, \gamma) = - \frac {\gamma^ {2}}{2 \pi} \int_ {- \infty} ^ {\infty} \ln \left| \det \left(I - \gamma^ {- 2} T ^ {*} (j \omega) T (j \omega)\right) \right| d \omega .$$

It is easy to see that

$$I (T, \gamma) = - \frac {\gamma^ {2}}{2 \pi} \int_ {- \infty} ^ {\infty} \sum_ {i} \ln \left| 1 - \gamma^ {- 2} \sigma_ {i} ^ {2} (T (j \omega)) \right| d \omega$$

and $I ( T , \gamma ) \geq 0$ , where $\sigma _ { i } \left( T ( j \omega ) \right)$ is the ith singular value of $T ( j \omega )$ . It is also easy to show that

$$\lim _ {\gamma \to \infty} I (T, \gamma) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \sum_ {i} \sigma_ {i} ^ {2} \left(T (j \omega)\right) d \omega = \| T \| _ {2} ^ {2}.$$

Thus the entropy $I ( T , \gamma )$ is, in fact , a performance index measuring the tradeoff between the $\mathcal { H } _ { \infty }$ optimality $( \gamma \to \| T \| _ { \infty } )$ and the $\mathcal { H } _ { 2 }$ optimality $( \gamma \to \infty )$ .

It has been shown in Glover and Mustafa [1989] that the suboptimal controller given in Theorem 14.1 is actually the controller that satisfies the norm condition $\| T _ { z w } \| _ { \infty } < \gamma$ and minimizes the following entropy:

$$- \frac {\gamma^ {2}}{2 \pi} \int_ {- \infty} ^ {\infty} \ln \left| \det \left(I - \gamma^ {- 2} T _ {z w} ^ {*} (j \omega) T _ {z w} (j \omega)\right) \right| d \omega .$$

Therefore, the given suboptimal controller is also called the minimum entropy controller [maximum entropy controller if the entropy is defined as $\tilde { I } ( T , \gamma ) = - I ( T , \gamma ) ]$ .

Related MATLAB Commands: hinfsyne, hinffi

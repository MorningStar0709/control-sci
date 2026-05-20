# LEMMA 6.4 Gronwall-Bellman lemma: Discrete time

If $u, v \geq 0$ , if $c_{1}$ is a positive constant, and if

$$u (t) \leq c _ {1} \sum_ {k = 0} ^ {t - 1} u (k) v (k) \tag {6.47}$$

then

$$u (t) \leq c _ {1} \exp \left(\sum_ {k = 0} ^ {t - 1} v (k)\right)$$

□

By using the Gronwall-Bellman lemma, many direct adaptive algorithms can be analyzed in the following way:

• Show that growth conditions such as Eq. (6.46) or Eq. (6.47) hold.   
- Show properties analogous to Eq. (6.44) for the signals $u$ and $v$ .   
- Use the Gronwall-Bellman lemma to get stability.

These steps can be used as a template for proving convergence and stability for adaptive algorithms.

# Exercise 1.53: Arrival cost with noise-shaping matrix G

Consider the deterministic, full information state estimation optimization problem

$$\min _ {x (0), \mathbf {w}, \mathbf {v}} \frac {1}{2} \left(| x (0) - \bar {x} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2} + \sum_ {i = 0} ^ {T - 1} | w (i) | _ {Q ^ {- 1}} ^ {2} + | v (i) | _ {R ^ {- 1}} ^ {2}\right)$$

subject to

$$x ^ {+} = A x + G wy = C x + v \tag {1.68}$$

in which the sequence of measurements y are known values. Using the result of the second part of Exercise 1.51, show that this problem also is equivalent to the following problem

$$\min _ {x (T - N), \mathbf {w}, \mathbf {v}} V _ {T - N} ^ {-} (x (T - N)) + \frac {1}{2} \left(\sum_ {i = T - N} ^ {T - 1} | w (i) | _ {Q ^ {- 1}} ^ {2} + | v (i) | _ {R ^ {- 1}} ^ {2}\right)$$

subject to (1.68). The arrival cost is defined as

$$V _ {N} ^ {-} (a) := \min _ {x (0), \mathbf {w}, \mathbf {v}} \frac {1}{2} \left(| x (0) - \overline {{x}} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2} + \sum_ {i = 0} ^ {N - 1} | w (i) | _ {Q ^ {- 1}} ^ {2} + | v (i) | _ {R ^ {- 1}} ^ {2}\right)$$

subject to (1.68) and $x ( N ) = a$ . Notice that any value of $N , 0 \leq N \leq T$ , can be used to split the cost function using the arrival cost.

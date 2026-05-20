# Exercise 1.52: On-time arrival

Consider the deterministic, full information state estimation optimization problem

$$\min _ {x (0), \mathbf {w}, \mathbf {v}} \frac {1}{2} \left(| x (0) - \overline {{{x}}} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2} + \sum_ {i = 0} ^ {T - 1} | w (i) | _ {Q ^ {- 1}} ^ {2} + | v (i) | _ {R ^ {- 1}} ^ {2}\right) \tag {1.66}$$

subject to

$$x ^ {+} = A x + wy = C x + v \tag {1.67}$$

in which the sequence of measurements $\mathbf { y } ( T )$ are known values. Notice we assume the noise-shaping matrix, $G ,$ is an identity matrix here. See Exercise 1.53 for the general case. Using the result of the first part of Exercise 1.51, show that this problem is equivalent to the following problem

$$\min _ {x (T - N), \mathbf {w}, \mathbf {v}} V _ {T - N} ^ {-} (x (T - N)) + \frac {1}{2} \sum_ {i = T - N} ^ {T - 1} | w (i) | _ {Q ^ {- 1}} ^ {2} + | v (i) | _ {R ^ {- 1}} ^ {2}$$

subject to (1.67). The arrival cost is defined as

$$V _ {N} ^ {-} (a) := \min _ {x (0), \mathbf {w}, \mathbf {v}} \frac {1}{2} \left(| x (0) - \overline {{x}} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2} + \sum_ {i = 0} ^ {N - 1} | w (i) | _ {Q ^ {- 1}} ^ {2} + | v (i) | _ {R ^ {- 1}} ^ {2}\right)$$

subject to (1.67) and $x ( N ) = a$ . Notice that any value of $N , 0 \leq N \leq T$ , can be used to split the cost function using the arrival cost.

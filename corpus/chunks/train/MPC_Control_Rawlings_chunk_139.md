# Exercise 1.21: Time-varying linear quadratic problem

Consider the time-varying version of the LQ problem solved in the chapter. The system model is

$$x (k + 1) = A (k) x (k) + B (k) u (k)$$

The objective function also contains time-varying penalties

$$\min _ {\mathbf {u}} V (x (0), \mathbf {u}) = \frac {1}{2} \left(\sum_ {k = 0} ^ {N - 1} \left(x (k) ^ {\prime} Q (k) x (k) + u (k) ^ {\prime} R (k) u (k)\right) + x (N) ^ {\prime} Q (N) x (N)\right)$$

subject to the model. Notice the penalty on the final state is now simply $Q ( N )$ instead of $P _ { f }$ .

Apply the DP argument to this problem and determine the optimal input sequence and cost. Can this problem also be solved in closed form like the time-invariant case?

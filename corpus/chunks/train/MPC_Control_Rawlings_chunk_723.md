# Exercise 6.2: LQ as least squares

Consider the standard LQ problem

$$\min _ {\mathbf {u}} V = \frac {1}{2} \sum_ {k = 0} ^ {N - 1} \left(x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k)\right) + (1 / 2) x (N) ^ {\prime} P _ {f} x (N)$$

subject to

$$x ^ {+} = A x + B u$$

(a) Set up the dense Hessian least squares problem for the LQ problem with a horizon of three, N = 3. Eliminate the state equations and write out the objective function in terms of only the decision variables u(0), u(1), u(2).

(b) What are the conditions for an optimum, i.e., what linear algebra problem do you solve to compute u(0), u(1), u(2)?

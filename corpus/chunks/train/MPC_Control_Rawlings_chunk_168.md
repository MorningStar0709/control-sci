# Exercise 1.44: Two stages are not better than one

We often can decompose an estimation problem into stages. Consider the following case in which we wish to estimate x from measurements of z, but we have the model between x and an intermediate variable, y, and the model between y and z

$$y = A x + e _ {1} \quad \operatorname{cov} (e _ {1}) = Q _ {1}z = B y + e _ {2} \quad \operatorname{cov} (e _ {2}) = Q _ {2}$$

(a) Write down the optimal least squares problem to solve for $\hat { y }$ given the $z$ measurements and the second model. Given $\hat { y } _ { ; }$ , write down the optimal least squares problem for $\hat { x }$ in terms of $\hat { y }$ . Combine these two results together and write the resulting estimate of xˆ given measurements of z. Call this the two-stage estimate of x.

(b) Combine the two models together into a single model and show that the relationship between z and x is

$$z = B A x + e _ {3} \qquad \operatorname{cov} (e _ {3}) = Q _ {3}$$

Express $Q _ { 3 }$ in terms of $Q _ { 1 } , Q _ { 2 }$ and the models A, B. What is the optimal least squares estimate of $\hat { x }$ given measurements of z and the one-stage model? Call this the one-stage estimate of x.

(c) Are the one-stage and two-stage estimates of x the same? If yes, prove it. If no, provide a counterexample. Do you have to make any assumptions about the models A, B?

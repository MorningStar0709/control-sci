# Exercise 1.8: Finite difference formula and approximating the exponential

Instead of computing the exact conversion of a continuous time to a discrete time system as in Exercise 1.5, assume instead one simply approximates the time derivative with a first-order finite difference formula

$$\frac {d x}{d t} \approx \frac {x (t _ {k + 1}) - x (t _ {k})}{\Delta}$$

with step size equal to the sample time, ∆. For this approximation of the continuous time system, compute $\tilde { \boldsymbol { A } }$ and $\tilde { B }$ so that the discrete time system agrees with the approximate continuous time system at the sample times. Comparing these answers to the exact solution, what approximation of $e ^ { A \Delta }$ results from the finite difference approximation? When is this a good approximation of $e ^ { A \Delta _ { 2 } }$

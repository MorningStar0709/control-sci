4.11 Consider the process in Example 4.5. Investigate through simulation what values of $\hat{r}_0$ can be used. Make the simulations with and without bounds on the control signal. How sensitive is the choice of initial values in the algorithm?

4.12 Consider the system (4.62) with $e(t) = 0$ and

$$
\begin{array}{l} A ^ {*} (q ^ {- 1}) = 1 - 4 q ^ {- 1} + 4 q ^ {- 2} = (1 - 2 q ^ {- 1}) ^ {2} \\ B ^ {*} (q ^ {- 1}) = q ^ {1} - 1. 9 9 9 q ^ {- 2} \\ \end{array}
$$

The open-loop process is unstable, and there is a near pole-zero cancellation. Assume that $\rho = 0.1$ and compute the generalized predictive controller that minimizes Eq. (4.65) for different values of $N$ . How large must $N$ be to get a stable closed-loop system? (The problem is adopted from Bitmead et al. (1990).) (Hint: Don't give up until $N > 25$ .)

4.13 Consider the system in Problem 1.9.

(a) Sample the system and assume that e is discrete-time measurement noise. Determine the minimum-variance controller for the system.   
(b) Simulate a self-tuning moving-average controller for different prediction horizons.

4.14 Make the same investigation as in Problem 4.12 but for the process in Problem 1.10.

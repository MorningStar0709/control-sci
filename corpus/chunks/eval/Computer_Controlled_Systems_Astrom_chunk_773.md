(a) The process has an unstable zero $z = b > 1$ .   
(b) The process has an unstable pole $z = a > 1$ .

12.26 Consider the system in Problem 12.23 with an extra time delay of 1 s. Determine the minimum-variance as a function of the sampling period.

12.27 Consider the system in Problem 12.23. Determine the output variance as a function of the input covariance for different sampling periods.

12.28 Consider the system

$$y (k) = \frac {1}{q - 0 . 9 9 9} u (k) + \frac {q}{q - 0 . 7} e (k)$$

Determine the minimum-variance control law for the system. Compare it with a proportional feedback that gives a corresponding response rate. Discuss the relative merits of the control laws by calculating their loop gains and return differences. Explain why the minimum-variance control is inferior. (Hint: A bad optimization problem gives a bad optimal regulator.)

12.29 Given the system

$$
\begin{array}{l} y (k) = 1. 4 y (k - 1) - 0. 6 5 y (k - 2) + u (k - 1) - 0. 2 u (k - 2) \\ + e (k) + 0. 4 e (k - 1) \\ \end{array}
$$

where $e \in N(0,2)$

(a) Determine the minimum-variance controller.   
(b) Determine the deadbeat controller.   
(c) Compute the variance of y when the controllers in (a) and (b), respectively, are used.

12.30 Consider the system

$$y (k) + a y (k - 1) = u (k - 1) + e (k) + c e (k - 1)$$

where $e \in N(0,1)$ . We want to determine the minimum-variance controller for the process but the value of $c$ is unknown.

(a) Assume in the design that $c = 0$ and determine the minimum-variance controller for the system

$$y (k) + a y (k - 1) = u (k - 1) + e (k)$$

How large will the output variance be if this controller is used on the true system?

(b) Assume instead that $c = \hat{c}$ and redo the calculations in (a).

12.31 Consider the stochastic process

$$y (k + 2) - 1. 1 y (k + 1) + 0. 3 y (k) = e (k + 2) - 1. 2 5 e (k + 1)$$

where $e \in N(0,1)$ .

(a) Determine the two-step-ahead predictor for $y(k)$ .   
(b) Calculate the variance of the prediction error.

12.32 Given the system

$$A (q) y (k) = B (q) u (k) + C (q) e (k)$$

where

$$
\begin{array}{l} A (q) = q ^ {3} - 1. 7 q ^ {2} + 0. 8 q - 0. 1 \\ B (q) = 2 (q - 0. 9) \\ C (q) = q ^ {2} (q - 0. 1) \\ \end{array}
$$

and $e(k) \in N(0,1)$ .

(a) Determine the minimum-variance controller for the system.   
(b) Determine the variance of the output when controlling the system with the controller in (a).   
(c) Redo the calculations in (a) and (b) when

$$B (q) = 2 (0. 9 q - 1)$$

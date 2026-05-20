(a) Determine the minimum-variance controller.   
(b) Discuss the special case $a = 0$ .

12.8 Given the system

$$y (k) - 1. 7 y (k - 1) + 0. 7 y (k - 2) = u (k - d) + 0. 5 u (k - d - 1)+ e (k) + 1. 5 e (k - 1) + 0. 9 e (k - 2)$$

(a) Determine the minimum-variance controller and the variance of the output for d = 1 and 2.   
(b) Simulate the open-loop system and the system controlled with the minimum-variance controller. Compare the output and the control signal for the different cases.

12.9 Consider the process in Fig. 12.11. The disturbance z has the spectral density

$$\phi_ {z} (\omega) = \frac {1}{2 \pi} \cdot \frac {1}{1 . 3 6 + 1 . 2 \cos \omega}$$

(a) Determine a pulse-transfer function $H(z)$ that gives an output with spectral density $\phi$ when driven by zero-mean white noise with unit variance.

(b) What is the steady-state variance of $y$ when

$$u (k) = - K y (k)$$

for K = 1?

(c) What is the minimum achievable variance for a proportional controller and how large is the corresponding value of $K$ ?   
(d) How large is the variance of $y$ when a minimum-variance controller is used?

12.10 Given the system

$$y (k) - 0. 2 5 y (k - 1) + 0. 5 y (k - 2) = u (k - 1) + e (k) + 0. 5 e (k - 1)$$

where $e(k)$ is white noise with unit variance. Assume that the process is controlled with the proportional controller

$$u (k) = - K y (k)$$

(a) Show that the variance of the output is

$$\frac {2 . 1 2 5 - K}{0 . 5 (1 . 7 5 - \overline {{{K}}}) (1 . 2 5 + \overline {{{K}}})}$$

and that the lowest variance is obtained for $K = 1$ , which gives the variance $4/3$ .

(h) The expression above is zero for $K = 2.125$ . Explain the paradox.   
(c) Compute the minimum-variance controller and the resulting output variance.

12.11 Given the process

$$y (k) - 1. 5 y (k - 1) + 0. 7 y (k - 2) = u (k - 2) - 0. 5 u (k - 3) + v (k)$$

(a) Assume that $v(k) = 0$ and compute the deadbeat controller for the system.   
(h) Assume that

$$v (k) = e (k) - 0. 2 e (k - 1)$$

where $e(k)$ is white noise. Compute the minimum-variance control law.

(c) What is the steady-state variance of $y$ when the deadbeat and the minimum-variance controllers are used on the system when $v$ is as in b)?   
(d) Simulate the system using the different controllers. Study the output and the accumulated loss, that is, the sum of the square of the output.

12.12 Consider the dynamic system

$$y (k) = \frac {B (q)}{A (q)} u (k) + \lambda \frac {C (q)}{D (q)} e (k)$$

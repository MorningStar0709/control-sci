where the matrix $A$ is

$$
A = \left( \begin{array}{c c c c c} - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} & - a _ {n} \\ 1 & 0 & & 0 & 0 \\ \vdots & & \ddots & & \\ 0 & 0 & & 1 & 0 \end{array} \right)
$$

and Q is a symmetric positive definite matrix. Show that the system of equations for solving $p_{1}$ , $p_{2}$ , and $p_{3}$ in Example 5.6 has a unique solution only if all the eigenvalues of A are in the left half-plane.

5.8 Show that the transfer function

$$G (s) = 1 + s$$

is SPR and ISP but not OSP.

5.9 Show that the transfer function

$$G (s) = \frac {1}{s + 1}$$

is SPR and OSP but not ISP.

5.10 Show that the transfer function

$$G (s) = \frac {s ^ {2} + 1}{(s + 1) ^ {2}}$$

is OSP and ISP but not SPR.

5.11 Consider the system

$$G (s) = G _ {1} (s) G _ {2} (s)$$

where

$$G _ {1} (s) = \frac {b}{s + a}G _ {2} (s) = \frac {c}{s + d}$$

where a and b are unknown parameters and c and d are known. Discuss how to make an MRAS based on the gradient approach. (Compare Problem 3.3.) Let the desired model be described by

$$G _ {m} (s) = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}}$$

5.12 A process has the transfer function

$$G (s) = \frac {b}{s (s + 1)}$$

where b is a time-varying parameter. The system is controlled by a proportional controller

$$u (t) = k \left(u _ {c} (t) - y (t)\right)$$

It is desirable to choose the feedback gain so that the closed-loop system has the transfer function

$$G (s) = \frac {1}{s ^ {2} + s + 1}$$

Design an MRAS that gives the desired result, and investigate the system by simulation. (Compare Problem 3.4.)

5.13 The general MRAS procedure in Section 5.8 was derived for known instantaneous gain $b_0$ . If $b_0$ is unknown, we may use the following augmented error:

$$\varepsilon = \frac {Q}{A _ {0} A _ {m}} \left(\left(b _ {0} - \hat {b} _ {0}\right) \left(\varphi^ {T} \theta + \frac {u}{P _ {1}}\right) + b _ {0} \varphi^ {T} \left(\theta - \theta^ {0}\right)\right)$$

where $\hat{b}_{0}$ is the estimate of $b_{0}$ . Discuss how this augmented error can be obtained and how it may be used to update the parameters $b_{0}$ and $\theta$ .

5.14 Study the parameter adjustment law in Example 5.2. Make a simulation program that implements the adaptive system. Repeat the simulation in Fig. 5.5. Investigate the behavior of the parameters and the error. Explore how the behavior is influenced by the adaptation gain $\gamma$ .

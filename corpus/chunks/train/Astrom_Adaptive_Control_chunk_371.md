5.15 Repeat the simulation in Problem 5.4 for different types of input signals. Change the amplitude and the nature of the signals. Can you find values of the adaptation gain that work well for different inputs?

5.16 Consider the system in Example 5.5. Assume that $u_{c}$ is a step that implies that $y_{m}$ will be time-varying. Investigate by analysis or simulate the stability limit and compare with the limit obtained in the example, in which $u_{c}$ and $y_{m}$ were constant.

5.17 Consider a first-order system with the transfer function

$$G (s) = \frac {b}{s + a}$$

where $a$ and $b$ are unknown parameters. Assume that the system is controlled by the control law

$$u = \theta_ {1} u _ {c} - \theta_ {2} y$$

Compare by simulation the properties of the systems obtained with the MIT rule and the one derived from Lyapunov theory. Use the same parameter values as in Example 5.2. (Hint: The algorithms are given in Examples 5.2 and 5.7.)

5.18 Investigate the properties of the system in Example 5.7 by simulation.

5.19 Investigate through simulation the convergence rate of the parameters in Example 5.2 when the control law of Eqs. (5.9) is used. How will the parameter adjustment change if an adaptation rule based on stability theory is used? For instance, plot the phase plane for the parameters.

5.20 Consider the process

$$G (s) = \frac {5 0}{s (s + 4)}$$

and the criterion

$$\int_ {0} ^ {\infty} \left((y - u _ {c}) ^ {2} + \rho u ^ {2}\right) d t$$

Let the control law have the form

$$u (t) = - s _ {o} \left(y - u _ {\mathrm{c}}\right)$$

or

$$u (t) = - \frac {s _ {0} p + s _ {1}}{p + r _ {1}} (y - u _ {c})$$

Determine the controller parameters through explicit minimization of the criterion, and let the gradients be obtained from an estimated model of the process. (Hint: See Trulsson and Ljung, 1985.)

5.21 Consider the system in Example 5.14. Figure 5.22(c) shows the rapid decrease in the error, while the parameters converge much more slowly. Explain the slow parameter convergence by analyzing the sensitivity of the closed-loop poles with respect to the estimated parameters.

5.22 Consider a system described by

$$G (s) = \frac {b}{s ^ {2} + a}$$

where a and b are unknown parameters. Find a simple control law that can control the plant well, and derive an adaptive algorithm that gives good performance.

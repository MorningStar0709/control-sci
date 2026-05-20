$$
\begin{array}{l} A (q) = q ^ {2} - 1. 5 q + 0. 7 \\ B (q) = q + 0. 5 \\ C (q) = q ^ {2} - q + 0. 2 4 \\ \end{array}
$$

Compare with the controller obtained through the identity in (12.17).

12.20 Determine for which systems a digital PID-controller has the same structure as the optimal minimum-variance controller.

12.21 Consider a system described by

$$y (k) = \frac {1}{q - a} (b u (k) + \varepsilon (k)) + \frac {1}{q - 1} w (k)$$

where $\varepsilon$ and w are white-noise processes with zero mean and standard deviations $\sigma_{\varepsilon}$ and $\sigma_{w}$ , respectively.

(a) Reduce the system to standard form and determine the minimum-variance controller.   
(h) Interpret the controller in (a) as a PI-controller and determine how the gain and the reset time depend on the ratio $\sigma_w^2 / \sigma_r^2$ .

12.22 Consider the minimum-variance control law of (12.31) for a system with an unstable inverse. The output of the closed-loop system is given by

$$y (k) = \frac {F (q)}{q ^ {d - 1} B ^ {- *} (q)} e (k)$$

Show that the function $F/B^{-*}$ has the series expansion

$$\frac {F (q)}{B ^ {- *} (q)} = q ^ {d - 1} + f _ {1} q ^ {d - 2} + \dots + f _ {d - 1} + \frac {F _ {2} (q)}{B ^ {- *} (q)}$$

where $\deg F_2(q) < \deg B^{-\bullet}$ and

$$F _ {1} (q) = q ^ {d - 1} + f _ {1} q ^ {d - 2} + \dots + f _ {d - 1}$$

is the quotient of $q^{d-1}C(q)$ and $A(q)$ . Give a convenient way of computing $F_{2}$ . Use the results of the problem to determine the increase of the minimum-variance due to unstable system zeros.

12.23 Determine the intersample ripple of the loss function when the process

$$
\begin{array}{l} d x _ {1} = x _ {2} d t \\ d x _ {2} = u d t + d v \\ y (t _ {k}) = x _ {1} (t _ {k}) + \varepsilon (t _ {k}) \\ \end{array}
$$

is controlled by the minimum-variance regulator. The process $v(t)$ is a Wiener process with incremental covariance $\sigma_{v}^{2}dt$ , and $\varepsilon(t_{k})$ is white measurement noise with zero mean and variance $\sigma_{\epsilon}^{2}$ .

12.24 Consider the process in Example 12.16. Determine the control law with sampling period h that minimizes

$$\lim _ {T \rightarrow \infty} \mathrm{E} \frac {1}{T} \int_ {0} ^ {T} x ^ {2} (s) d s$$

and compare it with the minimum-variance control.

12.25 Consider a process subject to a disturbance that is characterized as a Wiener process with incremental covariance dt. Determine the prediction error of the minimum-variance in each case. Use different prediction horizons and sampling periods.

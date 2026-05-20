# Solution

(a) The samples and 95% conditional density contour are shown in Figure 4.22. The particles are located properly at k = 0 and about 95% of them are inside the state’s initial density. But notice that the particles spread out quickly and few particles remain inside the 95% contour of the true conditional density after a few time steps.   
(b) The true conditional density is the normal density given by the time-varying Kalman filter recursion. The conditional density of the particle location is given by (4.52) and the samples are identi-

cally distributed

$$
\begin{array}{l} p (x (k) | \mathbf {y} (k)) \sim N (\hat {x} (k), P (k)) \\ \hat {x} (k + 1) = A \hat {x} (k) + B u (k) + L (k) (y (k) - C (A \hat {x} (k) + B u (k))) \\ P (k + 1) = A P (k) A ^ {\prime} + G Q G ^ {\prime} - L (k + 1) C (A P (k) A ^ {\prime} + G Q G ^ {\prime}) \\ p \left(x _ {i} (k) | \mathbf {y} (k)\right) \sim N (\overline {{x}} (k), \overline {{P}} (k)), \quad i = 1, \dots , s \\ \overline {{x}} (k + 1) = A \overline {{x}} (k) + B u (k) \\ \overline {{P}} (k + 1) = A \overline {{P}} (k) A ^ {\prime} + G Q G ^ {\prime} \\ \end{array}
$$

The major differences are underlined. Notice that the mean of the particle samples is independent of y(k), which causes the samples to drift away from the conditional density’s mean with time. Notice that the covariance does not have the reduction term present in the Kalman filter, which causes the variance of the particles to increase with time. Therefore, due to the missing underlined terms, the mean of the samples drifts and the variance increases with time. The particle weights cannot compensate for the inaccurate placement of the particles, and the state estimates from the simplest particle filter are not useful after a few time iterations.

![](image/003fa04c1d139493a811f654c30f425a13f609858e4bb10828c17c9d9ed0e3de.jpg)

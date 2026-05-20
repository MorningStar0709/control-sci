# EXAMPLE 11.1 The effect of the anti-aliasing filter

Consider a process described by

$$G (s) = \frac {1}{s (s + 1)}$$

A pole placement controller is designed to give a closed-loop system whose dominant poles are given by $\omega_{m} = 1$ rad/s and $\zeta_{m} = 0.7$ . The digital controller has a sampling period of h = 0.5. To illustrate the effect of aliasing, we assume that the output of the system is disturbed by a sinusoidal signal; that is, the measured signal is

$$y _ {m} (t) = y (t) + a _ {d} \sin (\omega_ {d} t)$$

with $a_{d}=0.1$ . This signal is filtered through a fourth-order Bessel filter with bandwidth $\omega_{B}$ . Figure 11.2 shows a number of simulations of the system that illustrate the effects of aliasing and filtering. Figure 11.2(a) shows setpoint, process output, and control signal. Since the bandwidth of the filter is $\omega_{B} = 25$ , the measured signal is not attenuated much by the filter. The disturbance with frequency $\omega_{d} = 11.3$ is aliased to 1.3 rad/s because of the sampling with Nyquist frequency $\omega_{N} = 2\pi$ . The aliased disturbance is clearly visible in the process input and output. In Fig. 11.2(b) the bandwidth of the prefilter is reduced to $\omega_{B} = 6.28$ rad/s. This bandwidth is not sufficiently small to give a substantial reduction of the disturbance. Notice also that the overshoot has increased a little because of the delay in the prefilter. In Fig. 11.2(c) the dynamics of the prefilter have been taken into account by adding a time delay of $0.7h$ in the model. The overshoot is then reduced, but the effect of the disturbance is similar to Fig. 11.2(b). In Fig. 11.2(d) the filter bandwidth has been reduced to $\omega_{B} = 2.51$ . The disturbance is now reduced significantly. We have also taken the dynamics of the filter into account as a time delay of $1.7h$ in designing the controller. The aliased disturbance is now barely noticeable in the figure.

(a)   
![](image/03ee0a58f75120a82f685fde4ac5b8afd3c13490edb2d70e88dd7c283080c047.jpg)

<details>
<summary>line</summary>

| Time | u | y |
| --- | --- | --- |
| 0 | 0.0 | 1.0 |
| 5 | 0.0 | 1.0 |
| 10 | 0.0 | 1.0 |
| 15 | 0.0 | 1.0 |
| 20 | 0.0 | 1.0 |
</details>

(b)   
![](image/2ca2c12b17226bcbe706d6a4bf65062607b5bfcf22c957b512c8fd8a5c98ea85.jpg)

<details>
<summary>line</summary>

| Time | u_c | y | u |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 5 | 1.0 | 0.0 | 0.0 |
| 10 | 1.0 | 0.0 | 0.0 |
| 15 | 1.0 | 0.0 | 0.0 |
| 20 | 1.0 | 0.0 | 0.0 |
</details>

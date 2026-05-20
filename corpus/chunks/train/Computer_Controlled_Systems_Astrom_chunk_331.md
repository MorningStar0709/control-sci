# Nominal Design

The design parameters that the user has to choose are the polynomials $A_{c}$ and $A_{o}$ , which specify the closed-loop poles, and the sampling period h. The closed-loop poles are parameterized in terms of $\zeta$ , $\omega$ , and $\alpha$ , that is, in terms of continuous-time equivalents. The nominal parameter values are chosen as $\zeta = 0.707$ , $\omega = 0.2$ , $\alpha = 2$ , and h = 1. This choice means that the observer poles are an order of magnitude faster than the dominant poles. The sampling rate is chosen so that $\omega h = 0.2$ , according to the recommendation in Sec. 5.6. This choice, however, does not take the observer dynamics into account. With the chosen sampling period we have $e^{-\alpha h} = 0.135$ . The sampled observer poles are thus close to the origin. A simulation experiment is performed to illustrate the properties of the nominal design. The experiment is chosen to show responses to command signals, load disturbances, and measurement noise. A unit-step command signal is first applied to the process. A load disturbance in the form of a negative step with amplitude 0.05 at the plant input is then applied at time 50. Finally, a high-frequency sinusoidal measurement error $e(k) = 0.01 \sin 2t$ is introduced at time 100 to show the response to high-frequency measurement noise. The results are shown in Fig. 5.10. Notice that frequency folding is clearly noticeable in the control signal. The Nyquist frequency is 0.5 Hz = π rad/s and the measurement noise has a frequency of 2 rad/s. In a practical case it would thus be important to use a proper prefilter. This is discussed in more detail in the example in the next section.

![](image/9d81ff2ddc39502735f74aae100c55a008ac40d6dec6a26bc9a8ffe52b4ed0da.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 0 |
| 50 | 1 | 0 |
| 100 | 1 | 0.05 |
| 150 | 1 | 0.05 |
</details>

Figure 5.10 Simulation of the nominal design, which has parameters $\omega = 0.2$ , $\zeta = 0.707$ , $\alpha = 2$ , and $h = 1$ .

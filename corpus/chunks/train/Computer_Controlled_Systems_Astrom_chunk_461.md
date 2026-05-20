# The Idea of Lifting

The notion of lifting is an elegant way to deal with periodically sampled systems. The idea is to represent a finite-dimensional sampled system as a time-invariant infinite-dimensional discrete system. In this way it is possible to define a notion of frequency response properly. It is also possible to give a nice description of intersample behavior.

Consider a system described by Eq. (2.1). Assume that the system is sampled with a period h, and that the input signal and the states are in $L_{2}$ . We introduce the discrete signal $u_{k} \in L_{2}(0, h)$ defined by

$$u _ {k} (\tau) = u (k h + \tau) \quad 0 < \tau < h \tag {7.30}$$

and the signals $x_{k}$ and $y_{k}$ , which are defined analogously. Define the discrete signal $x_{k}$ is the same way. It follows from Eq. (2.1) that

$$x _ {k + 1} (\tau) = \varphi (\tau) x _ {k} (h) + \int_ {0} ^ {\tau} \psi (\tau - s) B u _ {k} (s) d s \tag {7.31}y _ {k} (\tau) = C x _ {k} (\tau)$$

where

$$\varphi (\tau) = e ^ {A \tau}\psi (\tau) = e ^ {A (\tau)} B$$

This system is a time-invariant discrete-time system. Equation (7.31) gives a complete description of the intersample behavior because the function $y_{k}(\tau)$ , which is defined for $0 \leq \tau \leq h$ , is the output in the interval $kh \leq t \leq kh + h$ . The description thus includes the phenomenon of aliasing. Notice, however, that $u_{k}, x_{k}$ , and $y_{k}$ are elements of function spaces. Because the system is linear and time-invariant, the frequency response can be defined as $H(e^{i\omega h})$ , where $H$ is

![](image/8bf57b15a4423d8f1fb6c72fe46a059c200d1ab63a953983e5214958493b4ffe.jpg)

<details>
<summary>scatter</summary>

| FREQUENCY RATIO, r/r_s | REDUCTION IN AMPLITUDE - dB |
| --- | --- |
| 0.001 | ~0 |
| 0.01 | ~20 |
| 0.1 | ~40 |
| 1.0 | ~60 |
| 10 | ~80 |
</details>

Figure 7.27 Measured frequency response for a diesel engine. The frequencies are normalized with respect to the sampling frequency. [Redrawn from D. E. Bowns, "The Dynamic Transfer Characteristics of Reciprocating Engines," Proc. Mech. Eng., 185. (1971) with permission.]

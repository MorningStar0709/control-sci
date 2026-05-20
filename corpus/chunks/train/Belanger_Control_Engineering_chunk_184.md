Figure 4.7 illustrates frequency-domain specifications on $|H_d(j\omega)|$ and $|H_w(j\omega)|$ (or $|1 - H_d(j\omega)|$ ). The hatched areas are the permissible values. The dotted curve in Figure 4.7a dictates not only that $|H_d(j\omega)| \to 0$ , but how rapidly it does so. It is often defined as a straight line on a Bode plot, and the magnitude of its slope is called the rolloff rate, expressed in decibels (db) per decade.

In addition to the limits of Figure 4.7, the value at $\omega = 0$ ( $s = 0$ ) is often given. For a unit step in $y_d(t)$ , $y_d(s) = 1/s$ and

$$\lim _ {t \rightarrow \infty} y (t) = \lim _ {s \rightarrow 0} s H _ {d} (s) \cdot \frac {1}{s} = H _ {d} (0).$$

If $H_{d}(0) = 1$ , then $y(t) \to 1$ and the steady-state error $e_{ss}$ is zero; it is usually desirable to specify the behavior of $H_{d}$ at frequencies near zero.

It is often helpful to use a rational transfer function as a target shape for the frequency response $H_{d}(j\omega)$ . The ideal response—unity in the passband and zero elsewhere—cannot be achieved by any causal system, let alone one described by a transfer function [1]. Various rational approximations have been derived by researchers in filter design [2]. One set is the Butterworth family, described by all-pole transfer functions of unit magnitude at s = 0. The poles of a kth-order Butterworth low-pass filter are located as shown in Figure 4.8, where $\phi_{k} = \frac{180^{\circ}}{k}$ . The first three Butterworth transfer functions are

$$
\begin{array}{l} B _ {1} (s) = \frac {\omega_ {0}}{s + \omega_ {0}} \\ B _ {2} (s) = \frac {\omega_ {0} ^ {2}}{(s + \frac {\sqrt {2}}{2} \omega_ {2} + j \frac {\sqrt {2}}{2} \omega_ {0}) (s + \frac {\sqrt {2}}{2} \omega_ {0} - j \frac {\sqrt {2}}{2} \omega_ {0})} \\ = \frac {\omega_ {0} ^ {2}}{s ^ {2} + \sqrt {2} \omega_ {0} s + \omega_ {0} ^ {2}} \\ B _ {3} (s) = \frac {\omega_ {0} ^ {3}}{(s + \omega_ {0}) (s + \frac {1}{2} \omega_ {0} + j \frac {\sqrt {3}}{2} \omega_ {0}) (s + \frac {1}{2} \omega_ {0} - j \frac {\sqrt {3}}{2} \omega_ {0})}. \\ \end{array}
$$

![](image/1e778fef1b87af987cda79a6910f27f8bdb039e745db20ad234b49eb58ac01cc.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | Magnitude (db) |
| --- | --- |
| 0.1 | -10 |
| 1 | 0 |
| 10 | -30 |
| 100 | -90 |
</details>

(a)

![](image/f6384c4ca2303d8497d68120a2a9827a278b6159fcd5e3979e91d4ef8ac1012e.jpg)

<details>
<summary>line</summary>

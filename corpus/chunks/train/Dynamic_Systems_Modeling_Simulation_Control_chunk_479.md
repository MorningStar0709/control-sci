# Example 9.3

Figure 9.9 shows the one-degree-of-freedom (1-DOF) rotational mechanical system from Example 7.8. If the system is initially at rest, $\theta ( 0 ) = { \dot { \theta } } ( 0 ) = 0$ , and the input torque is a sine function $T _ { \mathrm { i n } } ( t ) = 1 . 5$ sin 18t N-m, compute the frequency response $\theta _ { \mathrm { s s } } ( t )$ of the mechanical system using analytical and numerical methods.

Using the parameters in Fig. 9.9 the mathematical model of the rotational mechanical system is

$$0. 2 \ddot {\theta} + 1. 6 \dot {\theta} + 6 5 \theta = T _ {\mathrm{in}} (t) \tag {9.29}$$

Therefore, the transfer function is

$$G (s) = \frac {1}{0 . 2 s ^ {2} + 1 . 6 s + 6 5} = \frac {\Theta (s)}{T _ {\mathrm{in}} (s)} \tag {9.30}$$

![](image/37db93a5db5135616a8a648fcde87dac1c42e2fde1ade38c951c26cc8807d57b.jpg)

<details>
<summary>text_image</summary>

T_in(t) = 1.5 sin18t N-m
J = 0.2 kg-m²
Flexible shaft,
k = 65 N-m/rad
θ
</details>

$\mathsf { F r i c t i o n } , b = 1 . 6 \mathrm { N } \mathrm { - m } \mathrm { - s } / \mathrm { r a d }$   
Figure 9.9 1-DOF rotational mechanical system for Example 9.3.

Using Eq. (9.17) with input amplitude $U _ { 0 } = 1 . 5 \mathrm { N - m }$ and frequency ?? = 18 rad/s the frequency response of the mechanical system is

$$\theta_ {\mathrm{ss}} (t) = | G (j \omega) | 1. 5 \sin (1 8 t + \phi) \tag {9.31}$$

Consequently, we need to evaluate the magnitude and phase of the sinusoidal transfer function $G ( j \omega )$ at frequency $\omega = 1 8 \mathrm { r a d / s } .$ . Substituting $s = j \omega$ in the transfer function (9.30) yields

$$G (j \omega) = \frac {1}{0 . 2 (j \omega) ^ {2} + 1 . 6 (j \omega) + 6 5} \tag {9.32}$$

Substituting $j ^ { 2 } = - 1$ into Eq. (9.32) we obtain

$$G (j \omega) = \frac {1}{6 5 - 0 . 2 \omega^ {2} + j 1 . 6 \omega}$$

or, evaluating G( j??) at input frequency ?? = 18 rad/s yields

$$G (j 1 8) = \frac {1}{0 . 2 + j 2 8 . 8}$$

The magnitude of G( j18) is

$$| G (j 1 8) | = \frac {\sqrt {1 ^ {2} + 0 ^ {2}}}{\sqrt {0 . 2 ^ {2} + 2 8 . 8 ^ {2}}} = 0. 0 3 4 7$$

The phase angle of G( j18) is the phase of its numerator minus the phase of its denominator

$$
\begin{array}{l} \phi = \angle G (j 1 8) = \angle (1 + j 0) - \angle (0. 2 + j 2 8. 8) \\ = \tan^ {- 1} \left(\frac {0}{1}\right) - \tan^ {- 1} \left(\frac {2 8 . 8}{0 . 2}\right) = 0 - 1. 5 6 3 9 \mathrm{rad} \\ \end{array}
$$

Finally, substituting the magnitude and phase of $G ( j \omega )$ into Eq. (9.31) gives us the frequency response

$$\theta_ {\mathrm{ss}} (t) = 0. 0 5 2 1 \sin (1 8 t - 1. 5 6 3 9) \text { rad } \tag {9.33}$$

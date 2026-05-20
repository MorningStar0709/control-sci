Note that the smaller the time constant T, the faster the system response. Another important characteristic of the exponential response curve is that the slope of the tangent line at t=0 is $1 / T$ , since

$$\left. \frac {d c}{d t} \right| _ {t = 0} = \frac {1}{T} e ^ {- t / T} \bigg | _ {t = 0} = \frac {1}{T} \tag {5-4}$$

The output would reach the final value at t=T if it maintained its initial speed of response. From Equation (5–4) we see that the slope of the response curve c(t) decreases monotonically from $1 / T$ at $t = 0$ to zero at $t = \infty$ .

The exponential response curve c(t) given by Equation (5–3) is shown in Figure 5–2. In one time constant, the exponential response curve has gone from 0 to 63.2% of the final value. In two time constants, the response reaches 86.5% of the final value.At $t = 3 T , 4 T ,$ , and 5T, the response reaches 95%, 98.2%, and 99.3%, respectively, of the final value.Thus, for $t \geq 4 T$ , the response remains within 2% of the final value. As seen from Equation (5–3), the steady state is reached mathematically only after an infinite time. In practice, however, a reasonable estimate of the response time is the length of time the response curve needs to reach and stay within the 2% line of the final value, or four time constants.

Unit-Ramp Response of First-Order Systems. Since the Laplace transform of the unit-ramp function is $1 / s ^ { 2 } .$ , we obtain the output of the system of Figure 5–1(a) as

$$C (s) = \frac {1}{T s + 1} \frac {1}{s ^ {2}}$$

Expanding C(s) into partial fractions gives

$$C (s) = \frac {1}{s ^ {2}} - \frac {T}{s} + \frac {T ^ {2}}{T s + 1} \tag {5-5}$$

Taking the inverse Laplace transform of Equation (5–5), we obtain

$$c (t) = t - T + T e ^ {- t / T}, \quad \text { for } t \geq 0 \tag {5-6}$$

The error signal e(t) is then

$$
\begin{array}{l} e (t) = r (t) - c (t) \\ = T \left(1 - e ^ {- t / T}\right) \\ \end{array}
$$

Figure 5–3 Unit-ramp response of the system shown in Figure 5–1(a).   
![](image/321749fa03757c3cd86e45bb601597d4ddaf919b279aa204fb378d9c3d6da87d.jpg)

<details>
<summary>line</summary>

| t | c(t) | r(t) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 2T | ~1.5 | r(t) = t |
| 4T | ~3.0 | r(t) = t |
| 6T | ~4.5 | r(t) = t |
| Steady-state error | ~5.5 | r(t) = t |
</details>

As t approaches infinity, $e ^ { - t / T }$ approaches zero, and thus the error signal e(t) approaches T or

$$e (\infty) = T$$

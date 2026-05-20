# EXAMPLE 3.6 Continuous-time self-tuner

Consider the system in Example 3.3, in which the process has the transfer function

$$G (s) = \frac {b}{s (s + a)}$$

with a = 1 and b = 1. Notice that the process has only two unknown parameters, a and b. The regressor filters in the estimator are chosen to be

$$H _ {f} (s) = \frac {1}{A _ {m} (s)}$$

Furthermore, we use an estimator without forgetting, that is, $\alpha = 0$ . Assume that it is desired to obtain a closed-loop system with the transfer function

$$G _ {m} (s) = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}}$$

The observer polynomial is chosen to be $A_{o}(s) = s + a_{o}$ with $a_{o} = 2$ . The specifications are the same as in Example 3.4, that is, $\zeta = 0.7$ and $\omega = 1$ . In Example 3.3 we solved the design problem when the parameters a and b are known. We found that the controller has the form

$$u (t) = - \frac {s _ {0} p + s _ {1}}{p + r _ {1}} y (t) + \frac {t _ {0} (p + a _ {o})}{p + r _ {1}} u _ {c} (t)$$

![](image/dd108896ca7c6bace6c8eba4681a4bd0a2ed1bae7c1f3553ba348c4fb5cc3b64.jpg)

<details>
<summary>line</summary>

| Time | u_c | y |
| --- | --- | --- |
| 0 | 1 | -1 |
| 25 | -1 | -1 |
| 50 | -1 | 1 |
| 75 | -1 | -1 |
| 100 | -1 | -1 |
</details>

![](image/0dcc8c8dd14c8187d5762e818902f991da82ed6f67e700137d6162acc6dd056f.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | 2.0 |
| 20 | 0.0 |
| 30 | -2.0 |
| 40 | 0.0 |
| 50 | 2.0 |
| 60 | 0.0 |
| 70 | -2.0 |
| 80 | 0.0 |
| 90 | 0.0 |
| 100 | 0.0 |
</details>

Figure 3.8 Output and input when using a continuous-time indirect self-tuning regulator to control the process in Example 3.6.

![](image/fcc28f3c97bb1590b892bf685b50270bfcfaf0efda72c56dd7cf1c6a35f90265.jpg)

<details>
<summary>line</summary>

| Time | â | Ê |
| --- | --- | --- |
| 0 | 2.0 | 2.0 |
| 5 | 1.0 | 1.0 |
| 10 | 1.0 | 1.0 |
| 20 | 1.0 | 1.0 |
| 50 | 1.0 | 1.0 |
| 100 | 1.0 | 1.0 |
| 200 | 1.0 | 1.0 |
</details>

Figure 3.9 Continuous-time parameter estimates corresponding to the simulation in Fig. 3.8. The lower part shows the estimates in an extended time scale.

where the controller parameters are given by

$$
\begin{array}{l} r _ {1} = 2 \zeta \omega + a _ {0} - a \\ s _ {0} = \frac {a _ {o} 2 \zeta \omega + \omega^ {2} - a r _ {1}}{b} \\ s _ {1} = \frac {\omega^ {2} a _ {o}}{b} \\ t _ {0} = \frac {\omega^ {2}}{b} \\ \end{array}
$$

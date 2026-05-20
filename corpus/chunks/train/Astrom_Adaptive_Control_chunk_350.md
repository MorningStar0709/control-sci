# EXAMPLE 5.14 Second-order MRAS

The performance of the general MRAS is illustrated by a second-order example, given the system

$$G (s) = \frac {k}{s (s + a)}$$

and the model

$$G _ {m} (s) = \frac {B _ {m}}{A _ {m}} = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}}$$

The polynomials $A_{v}$ , R, S, and T can be chosen to be

$$
\begin{array}{l} A _ {o} (s) = s + a _ {o} \\ R (s) = s + r _ {1} \\ S (s) = s _ {0} s + s _ {1} \\ T (s) = t _ {0} s + t _ {1} \\ \end{array}
$$

The Diophantine equation (Eq. 5.67) gives the solution

$$r _ {1} = 2 \zeta \omega + a _ {0} - as _ {0} = (2 \zeta \omega a _ {o} + \omega^ {2} - a r _ {1}) / ks _ {1} = a _ {o} \omega^ {2} / kt _ {0} = \omega^ {2} / kt _ {1} = a _ {0} \omega^ {2} / k$$

For simplicity we choose

$$Q (s) = A _ {o} (s) A _ {m} (s)P _ {1} (s) = A _ {m} (s)P _ {2} (s) = A _ {o} (s)$$

Figure 5.22 shows a simulation of the system with $\gamma = 1$ , $\zeta = 0.7$ , $\omega = 1$ , $a_{o} = 2$ , $a = 1$ , and $k = 2$ . In the simulation it is assumed that $\hat{b}_0 = b_0$ . The used values of the filters $P_1, P_2, Q$ , and $A_o$ give a fairly rapid convergence of $y$ to $y_m$ . The parameter estimates at the end of the simulation are still far from the optimal values, but the error is small (see Fig. 5.22c). The controller parameters are shown in Fig. 5.23. The control law at $t = 150$ gives a closed-loop system with a pole in $-1.95$ and two complex poles corresponding to

![](image/74562b4449ef7abccfaca9bbc5e11c1b4250aa1ed2bb73ccc5442be3e1bc17ab.jpg)

![](image/4b0ea1e2816fb03b379ac535c53b45b4208bb78e61444f8f04465400363ed8f1.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | ~0 |
| 50 | ~-1 |
| 100 | ~-1 |
| 150 | ~-1 |
</details>

![](image/5351c7bc95a53ef630b9e881d4ed70b720f224460f4d1bb90c62ef8f019e7c46.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 0 |
| 50 | -1 |
| 100 | 0 |
| 150 | 0 |
</details>

Figure 5.22 Simulation of the system in Example 5.14. (a) The process output (solid line) and the model output (dashed line). (b) The control signal. (c) The error $e = y - y_{m}$ .

![](image/f8ec41e52af9f0fa7a95e2d7bfd258bbfa96510a44f024bbc20dfc8e5780b878.jpg)

<details>
<summary>line</summary>

| Time | t₁ | s₁ | t₀ | s₀ | r₁' |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 |
| 50 | 0.7 | 0.6 | 0.5 | 0.45 | 0.2 |
| 100 | 0.7 | 0.6 | 0.5 | 0.45 | 0.2 |
| 150 | 0.7 | 0.6 | 0.5 | 0.45 | 0.2 |
</details>

Figure 5.23 The controller parameters in the simulation of the system in Example 5.14.

$\omega = 0.84$ and $\zeta = 0.78$ , which should be compared to the roots of $A_{o}A_{m}$ , which are in $-2$ , and complex poles corresponding to $\omega = 1$ and $\zeta = 0.7$ .

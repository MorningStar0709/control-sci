# EXAMPLE 8–1

Consider the control system shown in Figure 8–6 in which a PID controller is used to control the system. The PID controller has the transfer function

$$G _ {c} (s) = K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right)$$

Although many analytical methods are available for the design of a PID controller for the present system, let us apply a Ziegler–Nichols tuning rule for the determination of the values of parameters $K _ { p } , T _ { i }$ and, $T _ { d } .$ Then obtain a unit-step response curve and check to see if the designed. system exhibits approximately 25% maximum overshoot. If the maximum overshoot is excessive (40% or more), make a fine tuning and reduce the amount of the maximum overshoot to approximately 25% or less.

Since the plant has an integrator, we use the second method of Ziegler–Nichols tuning rules. By setting $T _ { i } = \infty$ and $T _ { d } = 0 .$ we obtain the closed-loop transfer function as follows:,

$$\frac {C (s)}{R (s)} = \frac {K _ {p}}{s (s + 1) (s + 5) + K _ {p}}$$

The value of $K _ { p }$ that makes the system marginally stable so that sustained oscillation occurs can be obtained by use of Routh’s stability criterion. Since the characteristic equation for the closed-loop system is

$$s ^ {3} + 6 s ^ {2} + 5 s + K _ {p} = 0$$

the Routh array becomes as follows:

$$
\begin{array}{l} \begin{array}{c c c c} s ^ {3} & 1 & 5 \\ s ^ {2} & 6 & K _ {p} \end{array} \\ s ^ {1} \quad \frac {3 0 - K _ {p}}{6} \\ s ^ {0} \qquad K _ {p} \\ \end{array}
$$

Figure 8–6 PID-controlled system.   
![](image/1105b6dbe8fe266f798f86d46341bde257475109a34d0f9d93937e1d55a13bae.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["Gc(s)"]
    C --> D["1/(s(s+1)(s+5))"]
    D --> E["C(s)"]
    E --> F["PID controller"]
    F --> B
```
</details>

Examining the coefficients of the first column of the Routh table, we find that sustained oscillation will occur if $K _ { p } = 3 0$ Thus, the critical gain. $K _ { \mathrm { c r } }$ is

$$K _ {\mathrm{cr}} = 3 0$$

With gain $K _ { p }$ set equal to $K _ { \mathrm { c r } } ( = 3 0 )$ the characteristic equation becomes,

$$s ^ {3} + 6 s ^ {2} + 5 s + 3 0 = 0$$

To find the frequency of the sustained oscillation, we substitute $s = j \omega$ into this characteristic equation as follows:

$$(j \omega) ^ {3} + 6 (j \omega) ^ {2} + 5 (j \omega) + 3 0 = 0$$

or

$$6 (5 - \omega^ {2}) + j \omega (5 - \omega^ {2}) = 0$$

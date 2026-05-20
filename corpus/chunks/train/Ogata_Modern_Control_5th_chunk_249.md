$$K _ {p} = \lim _ {s \rightarrow 0} \frac {K (T _ {a} s + 1) (T _ {b} s + 1) \cdots}{(T _ {1} s + 1) (T _ {2} s + 1) \cdots} = K$$

For a type 1 or higher system,

$$K _ {p} = \lim _ {s \rightarrow 0} \frac {K (T _ {a} s + 1) (T _ {b} s + 1) \cdots}{s ^ {N} (T _ {1} s + 1) (T _ {2} s + 1) \cdots} = \infty , \quad \text { for } N \geq 1$$

Hence, for a type 0 system, the static position error constant $K _ { p }$ is finite, while for a type 1 or higher system, $K _ { p }$ is infinite.

For a unit-step input, the steady-state error $e _ { \mathrm { s s } }$ may be summarized as follows:

$$
\begin{array}{l} e _ {\mathrm{ss}} = \frac {1}{1 + K}, \quad \text {   for   type   0   systems   } \\ e _ {\mathrm{ss}} = 0, \quad \text {   for   type   1   or   higher   systems   } \\ \end{array}
$$

From the foregoing analysis, it is seen that the response of a feedback control system to a step input involves a steady-state error if there is no integration in the feedforward path. (If small errors for step inputs can be tolerated, then a type 0 system may be permissible, provided that the gain K is sufficiently large. If the gain K is too large, however, it is difficult to obtain reasonable relative stability.) If zero steady-state error for a step input is desired, the type of the system must be one or higher.

Static Velocity Error Constant $K _ { v } .$ The steady-state error of the system with a unit-ramp input is given by

$$
\begin{array}{l} e _ {\mathrm{ss}} = \lim _ {s \rightarrow 0} \frac {s}{1 + G (s)} \frac {1}{s ^ {2}} \\ = \lim _ {s \rightarrow 0} \frac {1}{s G (s)} \\ \end{array}
$$

The static velocity error constant $K _ { v }$ is defined by

$$K _ {v} = \lim _ {s \to 0} s G (s)$$

Thus, the steady-state error in terms of the static velocity error constant $K _ { v }$ is given by

$$e _ {\mathrm{ss}} = \frac {1}{K _ {v}}$$

The term velocity error is used here to express the steady-state error for a ramp input.The dimension of the velocity error is the same as the system error.That is, velocity error is not an error in velocity, but it is an error in position due to a ramp input.

For a type 0 system,

$$K _ {v} = \lim _ {s \rightarrow 0} \frac {s K (T _ {a} s + 1) (T _ {b} s + 1) \cdots}{(T _ {1} s + 1) (T _ {2} s + 1) \cdots} = 0$$

Figure 5–47 Response of a type 1 unity-feedback system to a ramp input.   
![](image/75bc00582d0d2d799507540374fb3d44191c667f71fcf181cd63731dc95add96.jpg)

<details>
<summary>line</summary>

| t | r(t) | c(t) |
| --- | --- | --- |
| 0 | 0 | 0 |
| >0   | >r(t)| <r(t)
</details>

For a type 1 system,

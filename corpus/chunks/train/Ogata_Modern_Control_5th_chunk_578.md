Ziegler–Nichols Rules for Tuning PID Controllers. Ziegler and Nichols proposed rules for determining values of the proportional gain $K _ { p } ,$ integral time, $T _ { i } ,$ and de-, rivative time $T _ { d }$ based on the transient response characteristics of a given plant. Such determination of the parameters of PID controllers or tuning of PID controllers can be made by engineers on-site by experiments on the plant. (Numerous tuning rules for PID controllers have been proposed since the Ziegler–Nichols proposal. They are available in the literature and from the manufacturers of such controllers.)

There are two methods called Ziegler–Nichols tuning rules: the first method and the second method. We shall give a brief presentation of these two methods.

First Method. In the first method, we obtain experimentally the response of the plant to a unit-step input, as shown in Figure 8–2. If the plant involves neither integrator(s) nor dominant complex-conjugate poles, then such a unit-step response curve may look S-shaped, as shown in Figure 8–3. This method applies if the response to a step input exhibits an S-shaped curve. Such step-response curves may be generated experimentally or from a dynamic simulation of the plant.

The S-shaped curve may be characterized by two constants, delay time L and time constant T. The delay time and time constant are determined by drawing a tangent line at the inflection point of the S-shaped curve and determining the intersections of the tangent line with the time axis and line $c ( t ) = K$ , as shown in Figure 8–3. The transfer function $C ( s ) / U ( s )$ may then be approximated by a first-order system with a transport lag as follows:

Figure 8–2 Unit-step response of a plant.   
Figure 8–3 S-shaped response curve.   
![](image/26df14617ab1d66b5c6c963cc72146cfcc9b378fd04004bb4d3c58142ac8a6f9.jpg)

<details>
<summary>line</summary>

| t | c(t) |
| --- | --- |
| 0 | 0 |
| L | ~0.5 |
| T | ~1 |
| K | K |
</details>

Table 8–1 Ziegler–Nichols Tuning Rule Based on Step Response of Plant (First Method)

<table><tr><td>Type of Controller</td><td> $K_p$ </td><td> $T_i$ </td><td> $T_d$ </td></tr><tr><td>P</td><td> $\frac{T}{L}$ </td><td> $\infty$ </td><td>0</td></tr><tr><td>PI</td><td> $0.9\frac{T}{L}$ </td><td> $\frac{L}{0.3}$ </td><td>0</td></tr><tr><td>PID</td><td> $1.2\frac{T}{L}$ </td><td> $2L$ </td><td> $0.5L$ </td></tr></table>

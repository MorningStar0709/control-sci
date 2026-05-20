$$
\begin{array}{l} F _ {\mathrm{out}} = c ^ {\prime} u \sqrt {\frac {2 \rho g \ell}{\rho}} \\ = c u \sqrt {\ell} \tag {2.29} \\ \end{array}
$$

where $c$ is a constant encompassing all constants in the equations.

From Equations 2.28 and 2.29, the state equation is

$$\dot {\ell} = - \frac {c}{A} u \sqrt {\ell} + \frac {F _ {\mathrm{in}}}{A}. \tag {2.30}$$

Specific values are $A = 1 \, \mathrm{m}^2$ , $c = 2.0 \, \mathrm{m}^{3/2}/\mathrm{s}$ . With these,

$$\dot {\ell} = - 2. 0 u \sqrt {\ell} + F _ {\mathrm{in}}. \tag {2.31}$$

The simulation conditions are as follows: $\ell(0)=1\;\mathrm{m}, u(t)=.01\;\mathrm{m}, F_{\mathrm{in}}(t)=0, 0\leq t\leq100\;\mathrm{s}$ . These conditions correspond to the tank being emptied at constant valve opening. Figure 2.12 shows the behavior of the level (MATLAB command ode23). Note that the behavior is not exponential: the asymptotic value $\ell=0$ is reached in finite time.

![](image/286b751bd974e48da8d0182e2dcc55e9181e492ea17567854e129b8d44c3348e.jpg)

<details>
<summary>line</summary>

| Time(s) | Level (m) |
| --- | --- |
| 0 | 1.0 |
| 10 | 0.8 |
| 20 | 0.6 |
| 30 | 0.5 |
| 40 | 0.35 |
| 50 | 0.25 |
| 60 | 0.15 |
| 70 | 0.1 |
| 80 | 0.05 |
| 90 | 0.02 |
| 100 | 0.0 |
</details>

Figure 2.12 Response of level with zero in flow

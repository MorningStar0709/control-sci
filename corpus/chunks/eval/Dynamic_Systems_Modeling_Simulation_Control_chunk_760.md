As with any Simulink simulation, the user must set the desired integration parameters (ode4 is used here), stop time (8 s), and initial conditions for each Integrator block (recall that the default is zero initial conditions for each integrator). Recall that the initial condition are y(0) = 0, z(0) = 1, and $\dot { z } ( 0 ) = 0$ , and, therefore, only Integrator2 in Fig. C.11 has a nonzero initial condition. Figure C.12 shows plots of the responses y(t) and z(t) obtained by executing the Simulink model. Note that $z ( 0 ) = 1$ , as determined by setting the initial condition for Integrator2.

![](image/93f192638f34bd196a927db9060e0245e5394f39156ffa4c51e753de6de0204c.jpg)

<details>
<summary>line</summary>

| Time, s | y(t) | z(t) |
| --- | --- | --- |
| 0 | 0 | 1 |
| 1 | 2 | 2 |
| 2 | 6.5 | 1 |
| 3 | 2 | -3 |
| 4 | -6 | -2 |
| 5 | -2 | 2 |
| 6 | 2 | 1 |
| 7 | -4 | -3 |
| 8 | -9 | -2 |
</details>

Figure C.12 System responses y(t) and z(t) (Example C.4).

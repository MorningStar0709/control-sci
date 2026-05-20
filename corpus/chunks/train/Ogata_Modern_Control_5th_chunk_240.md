# 5–7 EFFECTS OF INTEGRAL AND DERIVATIVE CONTROL ACTIONS ON SYSTEM PERFORMANCE

In this section, we shall investigate the effects of integral and derivative control actions on the system performance. Here we shall consider only simple systems, so that the effects of integral and derivative control actions on system performance can be clearly seen.

Integral Control Action. In the proportional control of a plant whose transfer function does not possess an integrator $1 / s .$ , there is a steady-state error, or offset, in the response to a step input. Such an offset can be eliminated if the integral control action is included in the controller.

In the integral control of a plant, the control signal—the output signal from the controller—at any instant is the area under the actuating-error-signal curve up to that instant.The control signal $u ( t )$ can have a nonzero value when the actuating error signal $e ( t )$ is zero, as shown in Figure 5–36(a). This is impossible in the case of the proportional controller, since a nonzero control signal requires a nonzero actuating error signal. (A nonzero actuating error signal at steady state means that there is an offset.) Figure $5 \mathrm { - } 3 6 ( \mathrm { b } )$ shows the curve $e ( t )$ versus t and the corresponding curve $u ( t )$ versus t when the controller is of the proportional type.

Note that integral control action, while removing offset or steady-state error, may lead to oscillatory response of slowly decreasing amplitude or even increasing amplitude, both of which are usually undesirable.

Figure 5–36

(a) Plots of $e ( t )$ and $u ( t )$ curves showing nonzero control signal when the actuating error signal is zero (integral control); (b) plots of $e ( t )$ and $u ( t )$ curves showing zero control signal when the actuating error signal is zero (proportional control).

![](image/42c208ddc34e3f6733fd3585f31dc1d75965ca39904285f2a7eb1c9c6cb32881.jpg)

<details>
<summary>line</summary>

| t | e(t) |
| --- | --- |
| 0 | High |
| >0 | Decreasing to near zero |
</details>

![](image/f08367735a119ce3a073d4c1378fb01b6b26f9e370d9dbbcea29a3b01f8e8141.jpg)

<details>
<summary>line</summary>

| t | e(t) |
| --- | --- |
| 0 | 0.8 |
| >0 | 0.0 |
</details>

![](image/49bbe1c368d54193cec3596679e8c7c8245a374715eb1726b127135e1edf7451.jpg)

<details>
<summary>line</summary>

| t | u(t) |
| --- | --- |
| 0 | 0 |
| Peak | High |
| Decline | Low |
</details>

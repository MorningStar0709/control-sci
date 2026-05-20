# Tuning

A PID-controller has parameters $K, T_i, T_d, T_t, b, N, u_{\text{low}}$ , and $u_{\text{high}}$ that must be chosen. The primary parameters are $K, T_i,$ and $T_d$ . Parameter $N$ can often be given a fixed default value, for example, $N = 10$ . The tracking-time constant $(T_i)$ is often related to the integration time $(T_i)$ . In some implementations it has to be equal to $T_i$ ; in other cases it can be chosen as 0.1 to 0.5 times $T_i$ . The parameters $u_{\text{low}}$ and $u_{\text{high}}$ should be chosen close to the true saturation limits.

If the process dynamics and the disturbances are known parameters, then $K, T_{i}$ , and $T_{d}$ can be computed using the design methods of Chapters 4, 5, 11, and 12. Some special methods have, however, been developed to tune the PID-parameters experimentally. The behavior of the discrete-time PID-controller is very close to the analog PID-controller if the sampling interval is short. The traditional tuning rules for continuous-time controllers can thus be used. There are two classical heuristic rules due to Ziegler and Nichols (1942) that can be used to determine the controller parameters: the step-response method and the ultimate-sensitivity method.

The step-response method. In this method the unit step response of the open-loop process is determined experimentally. The technique can be applied to processes whose step response is monotone or essentially monotone apart from an initial nonminimum phase characteristic. To use the method the tangent to the step response that has the steepest slope is drawn and the intersections of the tangent with the axes are determined. See Fig. 8.13. The controller parameters are then obtained from Table 8.2. The Ziegler-Nichols rule was designed to give good response to load disturbances. It does, however, give fairly low damping of the dominant poles.

![](image/0f899348a9eb1d16860a008eae4d973f1f49a126951bf309e67563a7182de7e8.jpg)

<details>
<summary>line</summary>

| t | y(t) |
| --- | --- |
| L | 0 |
| >L | >y(t) |
</details>

Figure 8.13 Determination of parameters a = RL and L from the unit step response to be used in Ziegler-Nichols step-response method.

Parameter L is called the apparent deadtime. For stable processes parameter T, which is called the apparent-time constant, can also be determined from a step response of the open-loop system..

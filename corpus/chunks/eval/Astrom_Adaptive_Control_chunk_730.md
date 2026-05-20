# EXACT: The Foxboro Adaptive Controller

This controller is based on analysis of the transient response of the closed-loop system to setpoint changes or load disturbances and traditional tuning methods of the Ziegler-Nichols type.

Parameter Estimation. Assuming controller parameters such that the closed-loop system is stable, a typical response of the control error to a step or impulse disturbance is shown in Fig. 12.2. Heuristic logic is used to detect that a proper disturbance has occurred and to detect the peaks $e_{1}$ , $e_{2}$ , and $e_{3}$ and period $T_{p}$ . The estimation process is simple, but it is based on the assumption that the disturbances are steps or short pulses. The algorithm can give wrong estimates if the disturbances are two short pulses because $T_{p}$ will then be estimated to be the distance between the pulses.

Control Design. The control design is based on specifications on damping, overshoot, and the ratios $T_{i}/T_{p}$ and $T_{d}/T_{p}$ , where $T_{i}$ is the integration time, $T_{d}$ is the derivative time, and $T_{p}$ is the period of oscillation. The damping is defined as

$$d = \frac {e _ {3} - e _ {2}}{e _ {1} - e _ {2}}$$

and the overshoot as

$$\sigma = - \frac {e _ {2}}{e _ {1}}$$

In typical cases, both d and o must be less than 0.3. Empirical rules are used to calculate the controller parameters from $T_{p}$ , d, and o. These rules are based on traditional tuning rules of the Ziegler-Nichols type, augmented by experiences from controller tuning.

![](image/5ed35dc294c85e995b5096d1285fdd50991911418d49170d6f5422cb12e828bb.jpg)

<details>
<summary>line</summary>

| Point | Value |
| --- | --- |
| e₁ | 1.5 |
| e₂ | 0.2 |
| e₃ | 0.8 |
</details>

Figure 12.2 Typical response of control error to step or impulse disturbances.

Prior Information. The tuning procedure requires prior information about the controller parameters $K_{c}$ , $T_{i}$ , and $T_{d}$ . It also requires information on the time scale of the process. This is used to determine the maximum time the heuristic logic waits for the second peak. Some measure of the process noise is also needed to set the tolerances in the heuristic logic. Some parameters may also be set optionally: damping d, overshoot o, maximum derivative gain, and bounds on the controller parameters.

$$J \frac {d \omega}{d t} = k _ {m} I \tag {10.1}$$

where $J = J_{a} + J_{m}$ is the total moment of inertia and $k_{m}$ the current gain of the motor. The plant of Eq. (10.1) can be controlled adequately with a PI controller. The controller parameters can be chosen to be

$$K = \frac {2 \zeta_ {0} \omega_ {0} J}{k _ {m}}T _ {i} = \frac {2 \zeta_ {0}}{\omega_ {0}}$$

This gives the following characteristic equation for the closed-loop system:

$$s ^ {2} + 2 \zeta_ {0} \omega_ {0} s + \omega_ {0} ^ {2} = 0$$

The controller parameters are thus related to the model by simple equations. Notice that the integration time $T_{i}$ does not depend on the moment of inertia of the robot arm and that the controller gain K should be proportional to the moment of inertia.

A root-locus calculation indicates that the design based on the simplified model will work well if

$$\omega_ {0} < \omega_ {c r i t} = \zeta_ {0} \left(\frac {k J _ {m}}{J _ {a} ^ {2}}\right) ^ {1 / 2}$$

The most critical case occurs for $J_{a} = 0.002$ . It implies that $\omega_{0}$ must be less than 200 rad/s.

The fact that the design is based on a simplified model limits the closed-loop bandwidth. A fast response to command signals can still be obtained by use of feedforward compensation. For this purpose, let the desired response to angular velocity commands be given by

$$G _ {m} (s) = \frac {\omega_ {m} ^ {2}}{s ^ {2} + 2 \zeta_ {0} \omega_ {m} s + \omega_ {m} ^ {2}}$$

The feedforward controller can now be designed such that the closed-loop system gets the desired response.

An adaptive system can be obtained simply by estimating the total moment of inertia by applying recursive least squares to the model of Eq. (10.1) and feeding the estimate into the above design equation. To estimate the parameters of the continuous-time model of Eq. (10.1), it is necessary to introduce

![](image/f67393a34e25dda5bbbf9c95f3a2fb07479888273d7019bd5d295d077566cc72.jpg)

<details>
<summary>line</summary>

| Time | y |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 1.0 |
| 0.4 | 0.0 |
| 0.6 | 1.0 |
</details>

![](image/d88f5e0b558739a3406e078fed57eec63b5d1f2f238746eeed8cf85d66e06bbf.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0.0 | 0.25 |
| 0.1 | 0.0 |
| 0.2 | -0.1 |
| 0.3 | 0.0 |
| 0.4 | 0.1 |
| 0.5 | 0.0 |
| 0.6 | 0.0 |
</details>

Figure 10.5 Simulation of the tailored adaptive systems response with the arm inertia $J_{a} = 0.0002$ . The controller is initially tuned for $J_{a} = 0.002$ .

Note that the integral control action added to the proportional controller has converted the originally second-order system to a third-order one. Hence the control system may become unstable for a large value of $K _ { p } ,$ , since the roots of the characteristic equation may have positive real parts. (The second-order system is always stable if the coefficients in the system differential equation are all positive.)

It is important to point out that if the controller were an integral controller, as in Figure 5–42, then the system always becomes unstable, because the characteristic equation

$$J s ^ {3} + b s ^ {2} + K = 0$$

will have roots with positive real parts. Such an unstable system cannot be used in practice.

Note that in the system of Figure 5–41 the proportional control action tends to stabilize the system, while the integral control action tends to eliminate or reduce steadystate error in response to various inputs.

Derivative Control Action. Derivative control action, when added to a proportional controller, provides a means of obtaining a controller with high sensitivity. An advantage of using derivative control action is that it responds to the rate of change of the actuating error and can produce a significant correction before the magnitude of the actuating error becomes too large. Derivative control thus anticipates the actuating error, initiates an early corrective action, and tends to increase the stability of the system.

Figure 5–43 (a) Proportional control of a system with inertia load; (b) response to a unit-step input.   
![](image/7d51f2755fbf128a67ead33be82e8ed82d614c1c86787d4ef9acd878dbb0966a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum
    Sum --> Kp["K_p"]
    Kp --> |1/(Js²)| C["s"]
    C["s"] --> |feedback| Sum
```
</details>

![](image/f61e2c5dd03b98ad26c1258f8f4247b7ca307be2d1de5b57bc8fc86d52d105a6.jpg)

<details>
<summary>line</summary>

| t | c(t) |
| --- | --- |
| 0 | 0 |
| 0.5 | 1 |
| 1 | 0 |
| 1.5 | 1 |
| 2 | 0 |
| 2.5 | 1 |
| 3 | 0 |
| 3.5 | 1 |
| 4 | 0 |
</details>

Although derivative control does not affect the steady-state error directly, it adds damping to the system and thus permits the use of a larger value of the gain K, which will result in an improvement in the steady-state accuracy.

Since the numerator involves ${ } ^ { \left. } s { } ^ { \right. } , G _ { c 1 } ( s )$ must include an integrator to cancel this $" s >$ . [Although we want “s” in the numerator of the closed-loop transfer function $Y ( s ) / D ( s )$ to obtain zero steady-state error to the step disturbance input, we do not want to have $" s \ "$ in the numerator of the closed-loop transfer function $Y ( s ) / R ( s ) . ]$ To eliminate the offset in the response to the step reference input and eliminate the steady-state errors in following the ramp reference input and acceleration reference input, the numerator of $Y ( s ) / R ( s )$ must be equal to the last three terms of the denominator, as mentioned earlier. That is,

$$1 0 s G _ {c 1} (s) = 2 0. 4 s ^ {2} + 1 2 2. 4 4 s + 2 5 9. 6 8$$

or

$$G _ {c 1} (s) = 2. 0 4 s + 1 2. 2 4 4 + \frac {2 5 . 9 6 8}{s}$$

Thus, $G _ { c 1 } ( s )$ is a PID controller. Since $G _ { c } ( s )$ is given as

$$G _ {c} (s) = G _ {c 1} (s) + G _ {c 2} (s) = \frac {1 . 9 4 s ^ {2} + 1 2 . 2 4 4 s + 2 5 . 9 6 8}{s}$$

we obtain

$$
\begin{array}{l} G _ {c 2} (s) = G _ {c} (s) - G _ {c 1} (s) \\ = \left(1. 9 4 s + 1 2. 2 4 4 + \frac {2 5 . 9 6 8}{s}\right) - \left(2. 0 4 s + 1 2. 2 4 4 + \frac {2 5 . 9 6 8}{s}\right) \\ = - 0. 1 s \\ \end{array}
$$

Thus, $G _ { c 2 } ( s )$ is a derivative controller. A block diagram of the designed system is shown in Figure 8–37.

The closed-loop transfer function $Y ( s ) / R ( s )$ now becomes

$$\frac {Y (s)}{R (s)} = \frac {2 0 . 4 s ^ {2} + 1 2 2 . 4 4 s + 2 5 9 . 6 8}{s ^ {3} + 2 0 . 4 s ^ {2} + 1 2 2 . 4 4 s + 2 5 9 . 6 8}$$

Figure 8–37 Block diagram of the designed system.   
![](image/1523bfe9976f0bda6151e5dc3f56e8d7c21371084d76513a425abd4bc41b12b1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"] --> B["2.04s + 12.244 + (25.968)/s"]
    B --> C["+"] --> D["+"] --> E["10/(s(s+1))"]
    E --> Y["s"]
    Y["s"] --> F["0.1s"]
    F --> C
    D["s"] --> G["C2(s)"]
    G --> C
    D["s"] --> H["D(s)"]
    H --> E
```
</details>

Figure 8–38 (a) Response to unitramp reference input; (b) response to unit-acceleration reference input.   
![](image/c9d531d96ac7343e9fff0008b67a7ef984649674d68c2aa9a2bcc6d9b0400e43.jpg)

<details>
<summary>line</summary>

| t (sec) | Unit-Ramp Input | Output |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.2 | 0.2 | 0.2 |
| 0.4 | 0.4 | 0.4 |
| 0.6 | 0.6 | 0.6 |
| 0.8 | 0.8 | 0.8 |
| 1.0 | 1.0 | 1.0 |
| 1.2 | 1.2 | 1.2 |
| 1.4 | 1.4 | 1.4 |
| 1.6 | 1.6 | 1.6 |
| 1.8 | 1.8 | 1.8 |
| 2.0 | 2.0 | 2.0 |
</details>

![](image/2efd9fb49f91a43192ead6a2f84009f2d172737d4187d514d88b42cf29f91106.jpg)

<details>
<summary>line</summary>

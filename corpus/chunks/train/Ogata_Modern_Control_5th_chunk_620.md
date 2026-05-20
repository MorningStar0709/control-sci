One way to realize such an approximate differentiator is to utilize an integrator in the feedback path. Show that the closed-loop transfer function of the system shown in Figure 8–46 is given by the preceding expression. (In the commercially available differentiator, the value of g may be set as 0.1.)

Solution. The closed-loop transfer function of the system shown in Figure 8–46 is

$$\frac {C (s)}{R (s)} = \frac {\frac {1}{\gamma}}{1 + \frac {1}{\gamma T _ {d} s}} = \frac {T _ {d} s}{1 + \gamma T _ {d} s}$$

Note that such a differentiator with first-order delay reduces the bandwidth of the closed-loop control system and reduces the detrimental effect of noise signals.

A–8–5. Consider the system shown in Figure 8–47. This is a PID control of a second-order plant G(s). Assume that disturbances $D ( s )$ enter the system as shown in the diagram. It is assumed that the reference input $R ( s )$ is normally held constant, and the response characteristics to disturbances are a very important consideration in this system.

![](image/561f1d577c734b1e5511f68684f5048db6d0dda3abf7d8f962d110d6f56889c9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum1
    Sum1 --> PID["PID controller"]
    PID --> |+| Plant["G(s)"]
    Plant --> C["s"]
    D["s"] --> |+| Sum2
    Sum2 --> |1/(s² + 3.6s + 9)| Plant
    D["s"] --> |+| Sum1
    Sum1 --> |-| Sum2
```
</details>

Figure 8–47 PID-controlled system.

Design a control system such that the response to any step disturbance will be damped out quickly (in 2 to 3 sec in terms of the 2% settling time). Choose the configuration of the closed-loop poles such that there is a pair of dominant closed-loop poles. Then obtain the response to the unit-step disturbance input. Also, obtain the response to the unit-step reference input.

Solution. The PID controller has the transfer function

$$G _ {c} (s) = \frac {K (a s + 1) (b s + 1)}{s}$$

For the disturbance input in the absence of the reference input, the closed-loop transfer function becomes

$$
\begin{array}{l} \frac {C _ {d} (s)}{D (s)} = \frac {s}{s \left(s ^ {2} + 3 . 6 s + 9\right) + K (a s + 1) (b s + 1)} \\ = \frac {s}{s ^ {3} + (3 . 6 + K a b) s ^ {2} + (9 + K a + K b) s + K} \tag {8-14} \\ \end{array}
$$

$$\frac {C (s)}{R (s)} = \frac {K}{s (T s + 1) + K}$$

Hence

$$\frac {E (s)}{R (s)} = \frac {R (s) - C (s)}{R (s)} = \frac {s (T s + 1)}{s (T s + 1) + K}$$

Since the system is stable, the steady-state error for the unit-step response can be obtained by applying the final-value theorem, as follows:

$$
\begin{array}{l} e _ {\mathrm{ss}} = \lim _ {s \rightarrow 0} s E (s) \\ = \lim _ {s \rightarrow 0} \frac {s ^ {2} (T s + 1)}{T s ^ {2} + s + K} \frac {1}{s} \\ = 0 \\ \end{array}
$$

Integral control of the system thus eliminates the steady-state error in the response to the step input. This is an important improvement over the proportional control alone, which gives offset.

Response to Torque Disturbances (Proportional Control). Let us investigate the effect of a torque disturbance occurring at the load element. Consider the system shown in Figure 5–40.The proportional controller delivers torque T to position the load element, which consists of moment of inertia and viscous friction. Torque disturbance is denoted by D.

Assuming that the reference input is zero or R(s)=0, the transfer function between C(s) and D(s) is given by

$$\frac {C (s)}{D (s)} = \frac {1}{J s ^ {2} + b s + K _ {p}}$$

![](image/ba3755cd5775715674e56c466f74e05131125f62ec24aa68eb4a1db54bb701bb.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R --> |+| A["×"]
    A --> E --> Kp --> T --> |+| B["×"]
    D --> |+| C --> 1/(s(Js + b)) --> C
    C --> A
```
</details>

Figure 5–40   
Control system with a torque disturbance.

Hence

$$\frac {E (s)}{D (s)} = - \frac {C (s)}{D (s)} = - \frac {1}{J s ^ {2} + b s + K _ {p}}$$

The steady-state error due to a step disturbance torque of magnitude $T _ { d }$ is given by

$$
\begin{array}{l} e _ {\mathrm{ss}} = \lim _ {s \rightarrow 0} s E (s) \\ = \lim _ {s \rightarrow 0} \frac {- s}{J s ^ {2} + b s + K _ {p}} \frac {T _ {d}}{s} \\ = - \frac {T _ {d}}{K _ {p}} \\ \end{array}
$$

At steady state, the proportional controller provides the torque $- T _ { d } .$ which is equal in, magnitude but opposite in sign to the disturbance torque $T _ { d }$ The steady-state output due. to the step disturbance torque is

$$c _ {\mathrm{ss}} = - e _ {\mathrm{ss}} = \frac {T _ {d}}{K _ {p}}$$

The steady-state error can be reduced by increasing the value of the gain $K _ { p }$ . Increasing this value, however, will cause the system response to be more oscillatory.

Integral Control Action. In a controller with integral control action, the value of the controller output $u ( t )$ is changed at a rate proportional to the actuating error signal $e ( t )$ . That is,

$$\frac {d u (t)}{d t} = K _ {i} e (t)$$

or

$$u (t) = K _ {i} \int_ {0} ^ {t} e (t) d t$$

where $K _ { i }$ is an adjustable constant. The transfer function of the integral controller is

$$\frac {U (s)}{E (s)} = \frac {K _ {i}}{s}$$

Proportional-Plus-Integral Control Action. The control action of a proportionalplus-integral controller is defined by

$$u (t) = K _ {p} e (t) + \frac {K _ {p}}{T _ {i}} \int_ {0} ^ {t} e (t) d t$$

or the transfer function of the controller is

$$\frac {U (s)}{E (s)} = K _ {p} \left(1 + \frac {1}{T _ {i} s}\right)$$

where $T _ { i }$ is called the integral time.

Proportional-Plus-Derivative Control Action. The control action of a proportionalplus-derivative controller is defined by

$$u (t) = K _ {p} e (t) + K _ {p} T _ {d} \frac {d e (t)}{d t}$$

and the transfer function is

$$\frac {U (s)}{E (s)} = K _ {p} \left(1 + T _ {d} s\right)$$

where $T _ { d }$ is called the derivative time.

Proportional-Plus-Integral-Plus-Derivative Control Action. The combination of proportional control action, integral control action, and derivative control action is termed proportional-plus-integral-plus-derivative control action. It has the advantages of each of the three individual control actions. The equation of a controller with this combined action is given by

$$u (t) = K _ {p} e (t) + \frac {K _ {p}}{T _ {i}} \int_ {0} ^ {t} e (t) d t + K _ {p} T _ {d} \frac {d e (t)}{d t}$$

or the transfer function is

$$\frac {U (s)}{E (s)} = K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right)$$

where $K _ { p }$ is the proportional gain, $T _ { i }$ is the integral time, and $T _ { d }$ is the derivative time. The block diagram of a proportional-plus-integral-plus-derivative controller is shown in Figure 2–10.

Figure 2–10 Block diagram of a proportional-plusintegral-plusderivative controller.   
![](image/94d7afe1c068ecafc393cb0a5f48dacf23745fdd5dc1d5f74bb2976ae6d2ec5b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] -->|E(s)| B["Kp(1 + Ti s + Ti Td s^2)/Ti s"]
    B --> C["U(s)"]
    C --> D["Feedback"]
    D --> A
```
</details>

Figure 2–11 Closed-loop system subjected to a disturbance.   
![](image/d426320ae1f5825e2640a7326d6e5176620530f73f6e8d8b18bfda59e21d0ace.jpg)

<details>
<summary>flowchart</summary>

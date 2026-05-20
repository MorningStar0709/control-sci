# 5–2 FIRST-ORDER SYSTEMS

Consider the first-order system shown in Figure 5–1(a). Physically, this system may represent an RC circuit, thermal system, or the like. A simplified block diagram is shown in Figure 5–1(b). The input-output relationship is given by

$$\frac {C (s)}{R (s)} = \frac {1}{T s + 1} \tag {5-1}$$

In the following, we shall analyze the system responses to such inputs as the unit-step, unit-ramp, and unit-impulse functions. The initial conditions are assumed to be zero.

Note that all systems having the same transfer function will exhibit the same output in response to the same input. For any given physical system, the mathematical response can be given a physical interpretation.

Unit-Step Response of First-Order Systems. Since the Laplace transform of the unit-step function is $1 / s ,$ , substituting $R ( s ) = 1 / s$ into Equation (5–1), we obtain

$$C (s) = \frac {1}{T s + 1} \frac {1}{s}$$

Expanding C(s) into partial fractions gives

$$C (s) = \frac {1}{s} - \frac {T}{T s + 1} = \frac {1}{s} - \frac {1}{s + (1 / T)} \tag {5-2}$$

Taking the inverse Laplace transform of Equation (5–2), we obtain

$$c (t) = 1 - e ^ {- t / T}, \quad \text { for } t \geq 0 \tag {5-3}$$

Equation (5–3) states that initially the output c(t) is zero and finally it becomes unity. One important characteristic of such an exponential response curve c(t) is that at t=T the value of c(t) is 0.632, or the response $c ( t )$ has reached 63.2% of its total change.This may be easily seen by substituting t=T in c(t). That is,

$$c (T) = 1 - e ^ {- 1} = 0. 6 3 2$$

Figure 5–1 (a) Block diagram of a first-order system; (b) simplified block diagram.   
![](image/030419c86db3c6c579a3727b20de8edf0b30452f269ac6dd74f590665485d82e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["E(s)"]
    C --> D["1/Ts"]
    D --> E["C(s)"]
    E --> F["Feedback"]
    F --> B
```
</details>

![](image/2c9aa1c08f8dc753204df5ff284a7e3362caab70a337ebc3f9c199146f7c6f0c.jpg)  
(b)

Figure 5–2 Exponential response curve.   
![](image/340a2a622f2de2d2dc67b613118e4a7890042ba2336eea6cf3ca78676de861a8.jpg)

<details>
<summary>line</summary>

| t | c(t) | Label |
| --- | --- | --- |
| 0 | 0 |  |
| T | ~0.632 | A |
| 2T | ~0.875 | B |
| 3T | ~0.95 |  |
| 4T | ~0.98 |  |
| 5T | ~0.99 |  |
|  | 1 | c(t) = 1 - e^-(t/T) |
</details>

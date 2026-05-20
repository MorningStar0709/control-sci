$$b _ {1 \mathrm{eq}} = \left(\frac {N _ {1}}{N _ {2}}\right) ^ {2} \left(\frac {N _ {3}}{N _ {4}}\right) ^ {2} b _ {3 \mathrm{eq}}$$

The effect of $J _ { 2 }$ and $J _ { 3 }$ on an equivalent moment of inertia is determined by the gear ratios $N _ { 1 } / N _ { 2 }$ and $N _ { 3 } / N _ { 4 }$ For speed-reducing gear trains, the ratios,. $N _ { 1 } / N _ { 2 }$ and $N _ { 3 } / N _ { 4 }$ are usually less than unity. If $N _ { 1 } / N _ { 2 } \ll 1$ and1 $N _ { 3 } / N _ { 4 } \ll 1$ then the effect of, $J _ { 2 }$ and $J _ { 3 }$ on the equivalent moment of inertia ${ \cal J } _ { \mathrm { 1 e q } }$ is negligible. Similar comments apply to the equivalent viscous-friction coefficient $b _ { \mathrm { 1 e q } }$ of the gear train. In terms of the equivalent moment of inertia ${ \cal J } _ { \mathrm { 1 e q } }$ and equivalent viscous-friction coefficient $b _ { \mathrm { 1 e q } }$ , Equation (5–66) can be simplified to give

$$J _ {1 \mathrm{eq}} \ddot {\theta} _ {1} + b _ {1 \mathrm{eq}} \dot {\theta} _ {1} + n T _ {L} = T _ {m}$$

where

$$n = \frac {N _ {1} N _ {3}}{N _ {2} N _ {4}}$$

A–5–3. When the system shown in Figure 5–52(a) is subjected to a unit-step input, the system output responds as shown in Figure 5–52(b). Determine the values of K and T from the response curve.

Solution. The maximum overshoot of 25.4% corresponds to z=0.4. From the response curve we have

$$t _ {p} = 3$$

Consequently,

$$t _ {p} = \frac {\pi}{\omega_ {d}} = \frac {\pi}{\omega_ {n} \sqrt {1 - \zeta^ {2}}} = \frac {\pi}{\omega_ {n} \sqrt {1 - 0 . 4 ^ {2}}} = 3$$

![](image/af97ac97634c699e847a8e726a0e1e174cf6e0823cdc12b8463721919f460f95.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A["+"]
    A --> B["K/(s(Ts+1))"]
    B --> C["C(s)"]
    C --> D["Feedback"]
    D --> A
```
</details>

(a)

![](image/745a4fb6321a7caa364c973ff52cfc1d72e039c036ef41d3fbba7d49e4141a8c.jpg)

<details>
<summary>line</summary>

| t | c(t) |
| --- | --- |
| 0 | 0 |
| 3 | 0.254 |
</details>

(b)   
Figure 5–52   
(a) Closed-loop system; (b) unit-step response curve.

It follows that

$$\omega_ {n} = 1. 1 4$$

From the block diagram we have

$$\frac {C (s)}{R (s)} = \frac {K}{T s ^ {2} + s + K}$$

from which

$$\omega_ {n} = \sqrt {\frac {K}{T}}, \quad 2 \zeta \omega_ {n} = \frac {1}{T}$$

Therefore, the values of T and K are determined as

$$T = \frac {1}{2 \zeta \omega_ {n}} = \frac {1}{2 \times 0 . 4 \times 1 . 1 4} = 1. 0 9K = \omega_ {n} ^ {2} T = 1. 1 4 ^ {2} \times 1. 0 9 = 1. 4 2$$

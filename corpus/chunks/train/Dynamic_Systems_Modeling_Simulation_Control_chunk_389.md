# Log Decrement and the Damping Ratio

In many mechanical system applications, characterizing the system’s friction or damping is often a difficult task. The damping ratio $\zeta$ for an underdamped system can be estimated from the peak values of the transient response and the “amplitude envelope.” Figure 7.22 shows the step and impulse responses of an underdamped second-order system. Expressions for the complete system responses shown in Fig. 7.22 are

$\mathrm { S t e p r e s p o n s e : } \quad y ( t ) = K _ { 1 } e ^ { - \zeta \omega _ { n } t } \cos ( \omega _ { d } t + \phi _ { 1 } ) + y _ { \mathrm { s s } }$ (7.83)

$\mathrm { I m p u l s e r e s p o n s e : \quad } y ( t ) = K _ { 2 } e ^ { - \zeta \omega _ { n } t } \cos ( \omega _ { d } t + \phi _ { 2 } )$ (7.84)

where constants $K _ { 1 } , K _ { 2 } , \phi _ { 1 }$ , and $\phi _ { 2 }$ depend on the initial conditions and the magnitude of the input function. Note that the steady-state step response in Fig. 7.22a is $y _ { \mathrm { s s } } = 1$ , while the steady-state impulse response in Fig. 7.22b is zero because the input is zero for $t > 0$ . We can define the peak values relative to the steady-state value as

First relative peak value: $x _ { 1 } = y _ { 1 } - y _ { \mathrm { s s } }$

Second relative peak value: $x _ { 2 } = y _ { 2 } - y _ { \mathrm { s s } }$

![](image/124136a937c67af4af26462faf8dab370fbda69b894fcc4b71d15a5b7e87fcee.jpg)

<details>
<summary>line</summary>

| Time, s | Step response, y(t) |
| --- | --- |
| 0.0 | 0.0 |
| 0.4 | 1.6 |
| 0.8 | 0.6 |
| 1.2 | 1.2 |
| 1.5 | 0.9 |
| 2.0 | 1.1 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
</details>

(a)

![](image/f8089d1b3d12bd8ab4bbc00bd9e71643a687f7f44fb02da759a7c73dc9f2a687.jpg)

<details>
<summary>line</summary>

| Time, s | Impulse response, y(t) |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 0.35 |
| 0.5 | -0.2 |
| 1.0 | 0.1 |
| 1.5 | -0.05 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
| 3.5 | 0.0 |
| 4.0 | 0.0 |
</details>

(b)   
Figure 7.22 Underdamped second-order system response: (a) step response and (b) impulse response.

where $y _ { 1 }$ and $y _ { 2 }$ are the first two peak values of the complete response. The relative peak values are denoted in Figs. 7.22a and 7.22b. If we compute the ratio of the relative peak values, $x _ { 1 } / x _ { 2 }$ , for the step response, the sinusoidal term cancels because

$$K _ {1} \cos (\omega_ {d} t _ {1} + \phi_ {1}) = K _ {1} \cos (\omega_ {d} t _ {2} + \phi_ {1})$$

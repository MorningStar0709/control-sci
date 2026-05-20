Configuration 2: A different configuration of the control system is shown in Figure 10–31. The observer controller is placed in the feedback path. The input r is introduced into the closed-loop system through the box with gain N. From this block diagram, the closed-loop transfer function is obtained as

$$\frac {Y (s)}{R (s)} = \frac {N \left(s ^ {2} + 1 8 s + 1 1 3\right)}{s \left(s ^ {2} + 1\right) \left(s ^ {2} + 1 8 s + 1 1 3\right) + 3 0 2 s ^ {2} + 3 0 3 s + 2 5 6}$$

We determine the value of constant N such that for a unit-step input r, the output y is unity as t approaches infinity. Thus we choose

$$N = \frac {2 5 6}{1 1 3} = 2. 2 6 5 5$$

The unit-step response of the system is shown in Figure 10–32. Notice that the maximum overshoot is very small, approximately 4%. The settling time is about 5 sec.

![](image/8d8d336821bd13f9e3a48da3042ccad8672fe0286f7f603fd365f7512836003f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> N
    N --> adder
    adder --> Nr + u
    Nr + u --> transfer["1/(s(s²+1))"]
    transfer --> y
    y --> adder
    adder -->|-u"
    adder --> 302s² + 303s + 256/(s² + 18s + 113)
```
</details>

Figure 10–31 Control system with observer controller in the feedback path.

Figure 10–32 The unit-step response of the system shown in Figure 10–31. (The closed-loop poles for pole placement are at s=–1 ; j, s=–8. The observer poles are at s=–4, s=–4.)   
![](image/16f7e0ba02d95c411a669f54eb9243be1a3ad1de0568f1389bb9c555d74e0fb3.jpg)

<details>
<summary>line</summary>

| t (sec) | Output y |
| --- | --- |
| 0 | 0.0 |
| 1 | 0.2 |
| 2 | 0.8 |
| 3 | 1.0 |
| 4 | 1.0 |
| 5 | 1.0 |
| 6 | 1.0 |
| 7 | 1.0 |
| 8 | 1.0 |
| 9 | 1.0 |
| 10 | 1.0 |
</details>

Comments. We considered two possible configurations for the closed-loop control systems using observer controllers. As stated earlier, other configurations are possible.

The first configuration,which places the observer controller in the feedforward path,generally gives a fairly large overshoot.The second configuration,which places the observer controller in the feedback path, gives a smaller overshoot.This response curve is quite similar to that of the system designed by the pole-placement approach without using the observer controller. See the unit-step response curve of the system, shown in Figure 10–33, designed by the pole-placement approach without observer.Here the desired closed-loop poles used are

$$s = - 1 + j, \quad s = - 1 - j, \quad s = - 8$$

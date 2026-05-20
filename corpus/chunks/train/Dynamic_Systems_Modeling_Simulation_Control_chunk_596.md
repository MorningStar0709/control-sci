# Proportional controller

The open-loop transfer function with P-control or $G _ { C } ( s ) = K _ { P }$ and actuator gain $K _ { A } = 2 \mathrm { N } / \mathrm { V }$ is

$$G (s) H (s) = \frac {2}{s ^ {2} + 0 . 3 s} \tag {10.47}$$

Hence, the following MATLAB commands will create the root locus with natural-frequency and damping-ratio grid lines

```txt
>> sysGH = tf(2, [1 0.3 0])
>> rlocus(sysGH)
>> sgrid 
```

% create $G(s)H(s)$ for P-controller
% create and draw the root locus
% draw $\omega_{n}$ and $\zeta$ grid lines on root locus

The root locus in Fig. 10.41 shows that as gain $K _ { P }$ increases, the two closed-loop roots move along the real axis starting from the open-loop roots at $s = 0$ and $s = - 0 . 3$ until they meet at $s = - 0 . 1 5$ . The roots then move vertically along $\pm 9 0 ^ { \circ }$ asymptotes at $\sigma _ { a } = - 0 . 1 5$ . Consequently, the complex roots will always have a real part equal to $- 0 . 1 5$ and an increasing imaginary part as the gain $K _ { P }$ increases. Hence, the decay envelop term will always be $e ^ { - 0 . 1 5 t }$ with an associated settling time of about 26.67 s. Furthermore, the root locus shows that the damping ratio $\zeta$ will continually decrease with increasing gain as the roots move along the vertical asymptotes. These observations gleaned from the root-locus plot are illustrated by Fig. 10.19 (Example 10.6), which shows an underdamped closed-loop response for three $K _ { P }$ gains. All three closed-loop responses in Fig. 10.19 exhibit a settling time of 26.67 s and a decrease in damping as gain is increased. In summary, the root locus in Fig. 10.41 demonstrates that a P-control scheme will never provide a fast, well-damped transient response.

![](image/92f53dd5108e928a8c06a2155dadc2b15f68d943d709bea535967efaa4bfd1d2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference position, x_ref(t)"] --> B((+))
    B --> C["Position error, x_e(t)"]
    C --> D["G_C(s), Controller"]
    D --> E["Actuator voltage, e_in(t)"]
    E --> F["K_A"]
    F --> G["Actuator gain (N/V)"]
    G --> H["Force, f(t)"]
    H --> I["\frac{1}{s^2 + 0.3s}"]
    I --> J["Position, x(t)"]
    J --> K["-"]
    K --> B
```
</details>

Figure 10.40 Closed-loop position control of a mechanical system (Example 10.12).

![](image/c210fb88ccb408f52302c6c3a0e977d773afff4a47a05589b080b34ab09689b2.jpg)  
Figure 10.41 Root-locus plot for system with P-controller (Example 10.12).

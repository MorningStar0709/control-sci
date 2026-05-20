Figure 7–138 Control system.   
![](image/ec8448b89fe779ff84e3191a211431a4f91e4d1b13588611c64495f1b474ff6a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["K (s + 0.1)/(s + 0.5)"]
    B --> C["10/(s(s + 1))"]
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
    L --> M
    M --> N
    N --> O
    O --> P
    P --> Q
    Q --> R
    R --> S
    S --> T
    T --> U
    U --> V
    V --> W
    W --> X
    X --> Y
    Y --> Z
```
</details>

Let us plot the Bode diagram of $G ( s )$ when K=1. MATLAB Program 7–22 may be used for this purpose. Figure 7–139 shows the Bode diagram produced by this program. From this diagram the required phase margin of $6 0 ^ { \circ }$ occurs at the frequency $\omega = 1 . 1 5$ radsec. The magnitude of $G ( j \omega )$ at this frequency is found to be 14.5 dB. Then gain K must satisfy the following equation:

$$2 0 \log K = - 1 4. 5 \mathrm{dB}$$

or

$$K = 0. 1 8 8$$

<table><tr><td>MATLAB Program 7-22</td></tr><tr><td>num = [10 1];den = [1 1.5 0.5 0];bode(num,den)title(&#x27;Bode Diagram of G(s) = (10s + 1)/[s(s + 0.5)(s + 1)]&#x27;)</td></tr></table>

Thus, we have determined the value of gain K. Since the angle curve does not cross the $- 1 8 0 ^ { \circ }$ line, the gain margin is ±q dB.

To verify the results, let us draw a Nyquist plot of G for the frequency range

$$w = 0. 5: 0. 0 1: 1. 1 5$$

The end point of the locus $( \omega = 1 . 1 5 \mathrm { r a d / s e c } )$ will be on a unit circle in the Nyquist plane.To check the phase margin, it is convenient to draw the Nyquist plot on a polar diagram, using polar grids.

To draw the Nyquist plot on a polar diagram, first define a complex vector z by

$$z = \mathrm{re} + \mathrm{i} * \mathrm{im} = \mathrm{re} ^ {\mathrm{i} \theta}$$

where r and u (theta) are given by

$$r = \operatorname{abs} (z)\mathrm{theta} = \mathrm{angle(z)}$$

The abs means the square root of the sum of the real part squared and imaginary part squared; angle means tan–1 (imaginary part/real part).

![](image/0fe9b0e6ba661c750a985b9797f0753ac90c6652cb6abbbb40a87e70494e7d26.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.001 | 70 | -90 |
| 0.01 | 50 | -85 |
| 0.1 | 30 | -60 |
| 1 | 10 | -120 |
| 10 | -20 | -180 |
</details>

Figure 7–139   
Bode diagram of

$$G (s) = \frac {1 0 s + 1}{s (s + 0 . 5) (s + 1)}.$$

If we use the command

polar(theta,r)

MATLAB will produce a plot in the polar coordinates. Subsequent use of the grid command draws polar grid lines and grid circles.

# EXAMPLE 7–21

Draw a Bode diagram of the open-loop transfer function G(s) of the closed-loop system shown in Figure 7–71. Determine the gain margin, phase margin, phase-crossover frequency, and gaincrossover frequency with MATLAB.

A MATLAB program to plot a Bode diagram and to obtain the gain margin, phase margin, phase-crossover frequency, and gain-crossover frequency is shown in MATLAB Program 7–11. The Bode diagram of G(s) is shown in Figure 7–72.

Figure 7–71 Closed-loop system.   
![](image/b5b0fa60b123ff5312c5f03274f7f05dd85379e460408dae3d00f0eb7c0a32c9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["20(s + 1) / (s(s + 5)(s² + 2s + 10))"]
    B --> C["G(s)"]
    C --> D["Feedback"]
    D --> A
```
</details>

<table><tr><td>MATLAB Program 7-11</td></tr><tr><td>num = [20 20];den = conv([1 5 0],[1 2 10]);sys = tf(num,den);w = logspace(-1,2,100);bode(sys,w)[Gm,pm,wcp,wcg] = margin(sys);GmdB = 20*log10(Gm);[GmdB pm wcp wcg]ans =9.9293 103.6573 4.0131 0.4426</td></tr></table>

![](image/bda1d5deb53e8724142f182c3b37f00a624df2047316fd39e4c757339d1b145d.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.4426 | -103.6573 | 9.9293 |
</details>

Figure 7–72 Bode diagram of G(s) shown in Figure 7–71.

Resonant Peak Magnitude $M _ { r }$ and Resonant Frequency ${ \pmb { \omega } } _ { r }$ . Consider the standard second-order system shown in Figure 7–73.The closed-loop transfer function is

$$\frac {C (s)}{R (s)} = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}} \tag {7-16}$$

where $\zeta$ and $\omega _ { n }$ are the damping ratio and the undamped natural frequency, respectively. The closed-loop frequency response is

$$\frac {C (j \omega)}{R (j \omega)} = \frac {1}{\left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) + j 2 \zeta \frac {\omega}{\omega_ {n}}} = M e ^ {j \alpha}$$

where

$$M = \frac {1}{\sqrt {\left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) ^ {2} + \left(2 \zeta \frac {\omega}{\omega_ {n}}\right) ^ {2}}}, \quad \alpha = - \tan^ {- 1} \frac {2 \zeta \frac {\omega}{\omega_ {n}}}{1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}}$$

As given by Equation (7–12), for $0 \leq \zeta \leq 0 . 7 0 7$ , the maximum value of M occurs at the frequency $\omega _ { r }$ , where

$$\omega_ {r} = \omega_ {n} \sqrt {1 - 2 \zeta^ {2}} \tag {7-17}$$

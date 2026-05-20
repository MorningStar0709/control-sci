As the damping ratio $\zeta$ approaches zero, the resonant frequency approaches $\omega _ { n }$ . For $0 < \zeta \leq 0 . 7 0 7$ , the resonant frequency $\omega _ { r }$ is less than the damped natural frequency $\omega _ { d } = \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } }$ which is exhibited in the transient response. From Equation (7–12),, it can be seen that for $\zeta > 0 . 7 0 7$ , there is no resonant peak. The magnitude $\left| G ( j \omega ) \right.$ de-@ creases monotonically with increasing frequency $\omega .$ . (The magnitude is less than 0 dB for all values of $\omega > 0$ . Recall that, for $0 . 7 < \zeta < 1$ , the step response is oscillatory, but the oscillations are well damped and are hardly perceptible.)

Figure 7–10 M -versus-z curve for the second-order system $\bar { 1 / [ 1 + 2 \zeta ( j \omega / \omega _ { n } ) + }$ ${ \left( j \omega / \omega _ { n } \right) } ^ { 2 } \ ] .$ .   
![](image/45875cd1108bdc206771e4532a22a19c1241dd4eab55ba8e0604700985b16ce6.jpg)

<details>
<summary>line</summary>

| ζ | Mr in dB |
| --- | --- |
| 0.0 | 14.0 |
| 0.2 | 8.0 |
| 0.4 | 4.0 |
| 0.6 | 1.0 |
| 0.8 | 0.5 |
| 1.0 | 0.2 |
</details>

For $0 \leq \zeta \leq 0 . 7 0 7$ , the magnitude of the resonant peak, $M _ { r } = \left| G ( j \omega _ { r } ) \right|$ , can be found from Equations (7–12) and (7–9). For $0 \leq \zeta \leq 0 . 7 0 7$ ,

$$M _ {r} = \left| G (j \omega) \right| _ {\max} = \left| G (j \omega_ {r}) \right| = \frac {1}{2 \zeta \sqrt {1 - \zeta^ {2}}} \tag {7-13}$$

For $\zeta > 0 . 7 0 7 .$

$$M _ {r} = 1 \tag {7-14}$$

$\mathbf { A } \mathbf { s } \ \boldsymbol { \zeta }$ approaches zero, $M _ { r }$ approaches infinity. This means that if the undamped system is excited at its natural frequency, the magnitude of $G ( j \omega )$ becomes infinity. The relationship between $M _ { r }$ and $\zeta$ is shown in Figure 7–10.

The phase angle of $G ( j \omega )$ at the frequency where the resonant peak occurs can be obtained by substituting Equation (7–12) into Equation (7–8). Thus, at the resonant frequency $\omega _ { r }$ ,

$$\underline {{{/ G (j \omega_ {r})}}} = - \tan^ {- 1} \frac {\sqrt {1 - 2 \zeta^ {2}}}{\zeta} = - 9 0 ^ {\circ} + \sin^ {- 1} \frac {\zeta}{\sqrt {1 - \zeta^ {2}}}$$

General Procedure for Plotting Bode Diagrams. MATLAB provides an easy way to plot Bode diagrams. (The MATLAB approach is presented later in this section.) Here, however, we consider the case where we want to draw Bode diagrams manually without using MATLAB.

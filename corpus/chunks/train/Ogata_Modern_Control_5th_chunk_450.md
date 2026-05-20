# 7–4 LOG-MAGNITUDE-VERSUS-PHASE PLOTS

Another approach to graphically portraying the frequency-response characteristics is to use the log-magnitude-versus-phase plot, which is a plot of the logarithmic magnitude in decibels versus the phase angle or phase margin for a frequency range of interest. [The phase margin is the difference between the actual phase angle f and $- 1 8 0 ^ { \circ } .$ ; that is, $\phi - ( - 1 8 0 ^ { \circ } ) = 1 8 0 ^ { \circ } + \phi . ]$ The curve is graduated in terms of the frequency v. Such log-magnitude-versus-phase plots are commonly called Nichols plots.

In the Bode diagram, the frequency-response characteristics of $G ( j \omega )$ are shown on semilog paper by two separate curves, the log-magnitude curve and the phase-angle curve, while in the log-magnitude-versus-phase plot, the two curves in the Bode diagram are combined into one. In the manual approach the log-magnitude-versus-phase plot can easily be constructed by reading values of the log magnitude and phase angle from the Bode diagram. Notice that in the log-magnitude-versus-phase plot a change in the gain constant of $G ( j \omega )$ merely shifts the curve up (for increasing gain) or down (for decreasing gain), but the shape of the curve remains the same.

Advantages of the log-magnitude-versus-phase plot are that the relative stability of the closed-loop system can be determined quickly and that compensation can be worked out easily.

The log-magnitude-versus-phase plot for the sinusoidal transfer function $G ( j \omega )$ and that for $1 / G ( j \omega )$ are skew symmetrical about the origin, since

$$\left| \frac {1}{G (j \omega)} \right| \text { in dB } = - | G (j \omega) | \text { in dB }$$

![](image/501acb975cc7461bb8f3d65733445848334daf6a22bc154ee6e9af035e4ace13.jpg)  
(a)

![](image/05d04906978c32607a02305a5d38a82122575b36a3bfa803e1f2b48641d59633.jpg)

<details>
<summary>text_image</summary>

Im
ω = ∞
1
Re
ω = 0
Mr
ωn
ωr
</details>

(b)

![](image/7b8b5fb3c01751d89f2d7db21cb00a18f4f9d1ed0120b69990564664eb6714cb.jpg)  
(c)   
Figure 7–43 Three representations of the frequency response of $\frac { 1 } { 1 + 2 \zeta \bigg ( j \frac { \omega } { \omega _ { n } } \bigg ) + \bigg ( j \frac { \omega } { \omega _ { n } } \bigg ) ^ { 2 } }$ for z>0.2 , $\zeta > 0 .$ 1 + 2z vn   
(a) Bode diagram; (b) polar plot; (c) log-magnitude-versus-phase plot.

and

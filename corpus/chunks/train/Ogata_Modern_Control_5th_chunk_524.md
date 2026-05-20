# 7–13 LAG–LEAD COMPENSATION

We shall first examine the frequency-response characteristics of the lag–lead compensator. Then we present the lag–lead compensation technique based on the frequencyresponse approach.

Characteristic of Lag–Lead Compensator. Consider the lag–lead compensator given by

$$G _ {c} (s) = K _ {c} \left(\frac {s + \frac {1}{T _ {1}}}{s + \frac {\gamma}{T _ {1}}}\right) \left(\frac {s + \frac {1}{T _ {2}}}{s + \frac {1}{\beta T _ {2}}}\right) \tag {7-27}$$

where $\gamma > 1$ and $\beta > 1$ . The term

$$\frac {s + \frac {1}{T _ {1}}}{s + \frac {\gamma}{T _ {1}}} = \frac {1}{\gamma} \left(\frac {T _ {1} s + 1}{\frac {T _ {1}}{\gamma} s + 1}\right) \quad (\gamma > 1)$$

produces the effect of the lead network, and the term

$$\frac {s + \frac {1}{T _ {2}}}{s + \frac {1}{\beta T _ {2}}} = \beta \left(\frac {T _ {2} s + 1}{\beta T _ {2} s + 1}\right) \quad (\beta > 1)$$

produces the effect of the lag network.

Figure 7–109

Polar plot of a lag–lead compensator given by Equation (7–27), with $K _ { c } = 1$ and $\gamma = \beta .$

![](image/c97d9b3c116ddbf8b314535d76e9dc020697247f207c279e0b39a9a93b241132.jpg)

<details>
<summary>text_image</summary>

Im
ω = ω₁
0
1
ω = 0
Re
ω = ∞
</details>

In designing a lag–lead compensator, we frequently chose $\gamma = \beta .$ . (This is not necessary. We can, of course, choose $\gamma \neq \beta . )$ In what follows, we shall consider the case where $\gamma = \beta .$ . The polar plot of the lag–lead compensator with $K _ { c } = 1$ and $\gamma = \beta$ becomes as shown in Figure 7–109. It can be seen that, for $0 < \omega < \omega _ { 1 }$ , the compensator acts as a lag compensator, while for $\omega _ { 1 } < \omega <$ <q it acts as a lead compensator. The frequency $\omega _ { 1 }$ is the frequency at which the phase angle is zero. It is given by

$$\omega_ {1} = \frac {1}{\sqrt {T _ {1} T _ {2}}}$$

(To derive this equation, see Problem A–7–21.)

Figure 7–110 shows the Bode diagram of a lag–lead compensator when $K _ { c } = 1$ , $\gamma = \beta = 1 0 .$ , and $T _ { 2 } = 1 0 T _ { 1 }$ Notice that the magnitude curve has the value 0 dB at the. low- and high-frequency regions.

Figure 7–110

Bode diagram of a lag–lead compensator given by Equation (7–27) with $K _ { c } = 1$ , $\gamma = \beta = 1 0$ , and $T _ { 2 } = 1 0 T _ { 1 } .$ .

![](image/127644926abaac4e3a275cc6cbef9107ca4798258ad35083cce668e3efb3128a.jpg)

<details>
<summary>line</summary>

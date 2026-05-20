# EXAMPLE 7–28

Consider the unity-feedback system whose open-loop transfer function is

$$G (s) = \frac {K}{s (s + 1) (s + 2)}$$

It is desired that the static velocity error constant be $1 0 \ \mathrm { s e c } ^ { - 1 }$ , the phase margin be $5 0 ^ { \circ }$ , and the gain margin be 10 dB or more.

Assume that we use the lag–lead compensator given by Equation (7–28). [Note that the phaselead portion increases both the phase margin and the system bandwidth (which implies increasing the speed of response). The phase-lag portion maintains the low-frequency gain.]

The open-loop transfer function of the compensated system is $G _ { c } ( s ) G ( s )$ . Since the gain K of the plant is adjustable, let us assume that $K _ { c } = 1$ . Then, lim $G _ { c } ( s ) = 1$ .

From the requirement on the static velocity error constant, we obtain

$$K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) = \lim _ {s \rightarrow 0} s G _ {c} (s) \frac {K}{s (s + 1) (s + 2)} = \frac {K}{2} = 1 0$$

Hence,

$$K = 2 0$$

We shall next draw the Bode diagram of the uncompensated system with $K = 2 0$ , as shown in Figure 7–111. The phase margin of the gain-adjusted but uncompensated system is found to be $- 3 2 ^ { \circ }$ , which indicates that the gain-adjusted but uncompensated system is unstable.

The next step in the design of a lag–lead compensator is to choose a new gain crossover frequency. From the phase-angle curve for $G ( j \omega )$ , we notice that $/ G ( j \omega ) = - 1 8 0 ^ { \circ } \mathrm { a t } \omega = 1 . 5 \mathrm { r a d / s e c } .$ It is convenient to choose the new gain crossover frequency to be 1.5 radsec so that the phaselead angle required at $\omega = 1 . 5$ radsec is about $5 0 ^ { \circ }$ , which is quite possible by use of a single lag–lead network.

Once we choose the gain crossover frequency to be 1.5 radsec, we can determine the corner frequency of the phase-lag portion of the lag–lead compensator. Let us choose the corner frequency $\omega = 1 / T _ { 2 }$ (which corresponds to the zero of the phase-lag portion of the compensator) to be 1 decade below the new gain crossover frequency, or at $\omega = 0 . 1 5 \mathrm { r a d / s e c }$ .

Figure 7–111 Bode diagrams for G (gain-adjusted but uncompensated open-loop transfer function), $G _ { c }$ (compensator), and $G _ { c } G$ (compensated open-loop transfer function).   
![](image/51b8855061ab08ba764e01e9a46af0b47643723197af7fc3cb36965576bad2b0.jpg)

<details>
<summary>line</summary>

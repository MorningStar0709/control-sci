4.30 Calculate the optimum sensitivity, in the $H^{\infty}$ sense, for the plant $P(s) = (s^{2} + 1) / [s(s + 1)^{2}]$ and $W(s) = (s + 1) / s$ .

4.31 High-wire artist Calculate the optimum sensitivity, in the $H^{\infty}$ sense, for the plant whose transfer function is $\phi/\tau$ in Problem 3.16 (Chapter 3), and for a weight $W(s) = (s + 12)^{2}/s^{2}$ .

![](image/69ac180ad6b53203e8ee53416d3e2676ebee5888aa33555130020eddaa11a054.jpg)

4.32 Two-pendula problem Calculate the optimum sensitivity, in the $H^{\infty}$ sense, for the transfer function $X / F$ of Problem 3.21 (Chapter 3) and the weighting function $W(s) = (s + 1)^{2} / [s^{2}(s + 5)^{2}]$ . Plot $|S(j\omega)|$ . (The pole at $s = -5$ is chosen so as to ensure that $|W(j\omega)|$ is relatively large up to about $\omega = 5$ , because the plant has its largest RHP pole at approximately $s = 5$ .) (See Section 4.4.4.)

![](image/3b8aad9ae6a428b0679fba3c1d2b3247c8cac775390838922603d074925b42dd.jpg)

4.33 For a plant $P(s) = (.5s + 1) / (.1s + 1)^3$ , the sensitivity is to be small up to about 20 rad/s because of the expected disturbance spectrum. On the other hand, fairly large step inputs to $y_d$ are expected, and we are willing to give up some speed of response (i.e., bandwidth) in order to keep the control effort at reasonable levels.

We choose

$$S (s) = \frac {. 0 5 s}{. 0 5 s + 1} \quad \text { and } \quad \frac {y}{y _ {d}} = \frac {1}{T s + 1}.$$

a. Design a 2-DOF system that yields the required $S(s)$ and $y / y_{d}$ .   
b. Calculate the transfer function $u/y_{d}$ .   
c. Obtain $u(t)$ in response to $y_{d} = u_{-1}(t)$ , for $T = .05, .5$ , and 1.

4.34 Given $P(s) = (.5s - 1) / [s(s + 1)]$ , design a stable 2-DOF control system such that $S(s)$ is of the form $k[(s + a) / (s + 1)]$ , and $y / y_d$ is of the form $(Ts + 1) / (s^2 + 1.4s + 1)$ .

4.35 Figure 4.31 shows a 2-DOF structure different from that in Figure 4.21.

a. Show that the matrix transfer function between the inputs $y_{d}$ , d, and v and the outputs y and u are the same as for the configuration of Figure 4.27.   
b. The configuration of Figure 4.27 allows cancellation of the RHP zeros of $S$ by $R$ . Show that that is not possible for this configuration if the system is to be internally stable.

![](image/4395652ebc97018530aa208c17cfe2b72f92fcbccbd93c07c968a623af98ddef.jpg)

<details>
<summary>flowchart</summary>

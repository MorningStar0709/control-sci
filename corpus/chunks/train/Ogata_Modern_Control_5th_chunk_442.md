# EXAMPLE 7–10

Consider the following open-loop transfer function:

$$G (s) = \frac {1}{s ^ {2} + 0 . 8 s + 1}$$

Draw a Nyquist plot with MATLAB.

Since the system is given in the form of the transfer function, the command

$$\text { nyquist(num,den) }$$

may be used to draw a Nyquist plot. MATLAB Program 7–5 produces the Nyquist plot shown in Figure 7–36. In this plot, the ranges for the real axis and imaginary axis are automatically determined.

Figure 7–36

Nyquist plot of

$$G (s) = \frac {1}{s ^ {2} + 0 . 8 s + 1}.$$

<table><tr><td>MATLAB Program 7-5</td></tr><tr><td>num = [1];den = [1 0.8 1];nyquist(num,den)gridtitle(&#x27;Nyquist Plot of G(s) = 1/(s^2 + 0.8s + 1)&#x27;)</td></tr></table>

![](image/3f2bcc345b56b23d5a6be31857423fc0f39aea8ce4d2c064d1424a1d080aa497.jpg)

<details>
<summary>other</summary>

Nyquist plot of

$$G (s) = \frac {1}{s ^ {2} + 0 . 8 s + 1}.$$

![](image/d050dab837a39cb7a5b4b82fd8a21321d551635a828ca210d092a8da9bf563ea.jpg)

<details>
<summary>other</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -1.0 | 0.0 |
| 0.0 | 0.0 |
| 0.5 | 1.3 |
| 1.0 | -1.3 |
| 0.5 | -1.5 |
| 0.0 | -1.5 |
| -0.5 | -0.5 |
| -1.0 | 0.0 |
</details>

Caution. In drawing a Nyquist plot, where a MATLAB operation involves “Divide by zero,” the resulting Nyquist plot may have an erroneous or undesirable appearance. For example, if the transfer function G(s) is given by

$$G (s) = \frac {1}{s (s + 1)}$$

then the MATLAB command

$$\mathrm{num} = [ 1 ];\mathrm{den} = [ 1 \quad 1 \quad 0 ];\text { nyquist(num,den) }$$

produces an undesirable Nyquist plot. An example of an undesirable Nyquist plot is shown in Figure 7–38. If such an undesirable Nyquist plot appears on the computer, then it can be corrected if we specify the axis(v). For example, if we enter the axis command

![](image/28791e00cc7d4b1a09e793f2dceb7e6ebd1add6505bcb79393d7ee9dfb9d7c9b.jpg)

<details>
<summary>other</summary>

Nyquist Diagram
| Real Axis | Imaginary Axis |
| --- | --- |
| -1.0 | 100 |
| -1.0 | -100 |
| -0.8 | 0 |
| -0.6 | 0 |
| -0.4 | 0 |
| -0.2 | 0 |
| 0.0 | 0 |
</details>

Figure 7–38   
Undesirable Nyquist plot.

$$
v = \left[ \begin{array}{c c c c} - 2 & 2 & - 5 & 5 \end{array} \right]; a x i s (v)
$$

in the computer, then a desirable form of Nyquist plot can be obtained. See Example 7–11.

EXAMPLE 7–11 Draw a Nyquist plot for the following G(s):

$$G (s) = \frac {1}{s (s + 1)}$$

MATLAB Program 7–7 will produce a desirable form of Nyquist plot on the computer, even though a warning message “Divide by zero” may appear on the screen.The resulting Nyquist plot is shown in Figure 7–39.

<table><tr><td>MATLAB Program 7-7</td></tr><tr><td>% ---- Nyquist plot------</td></tr><tr><td>num = [1];</td></tr><tr><td>den = [1 1 0];</td></tr><tr><td>nyquist(num,den)</td></tr><tr><td>v = [-2 2 -5 5]; axis(v)</td></tr><tr><td>grid</td></tr><tr><td>title(&#x27;Nyquist Plot of G(s) = 1/[s(s + 1)]&#x27;)</td></tr></table>

Notice that the Nyquist plot shown in Figure 7–39 includes the loci for both v $> 0$ and $\omega < 0$ . If we wish to draw the Nyquist plot for only the positive frequency region $( \omega > 0 )$ , then we need to use the command

$$[ \mathrm{re}, \mathrm{im}, \mathrm{w} ] = \text {nyquist} (\mathrm{num}, \mathrm{den}, \mathrm{w})$$

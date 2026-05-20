# EXAMPLE 7–5 Consider the following transfer function:

$$G (s) = \frac {2 5}{s ^ {2} + 4 s + 2 5}$$

Plot a Bode diagram for this transfer function.

When the system is defined in the form

$$G (s) = \frac {\operatorname{num} (s)}{\operatorname{den} (s)}$$

use the command bode(num,den) to draw the Bode diagram. [When the numerator and denominator contain the polynomial coefficients in descending powers of s, bode(num,den) draws the Bode diagram.] MATLAB Program 7–1 shows a program to plot the Bode diagram for this system. The resulting Bode diagram is shown in Figure 7–20.

<table><tr><td>MATLAB Program 7-1</td></tr><tr><td>num = [25];den = [1 4 25];bode(num,den)title(&#x27;Bode Diagram of G(s) = 25/(s^2 + 4s + 25)&#x27;)</td></tr></table>

![](image/2bc7f699e38516378c3d27d77aa967345c67d1ccb151dd0f3190147a68aee5ee.jpg)  
Figure 7–20 Bode diagram of $G ( s ) = \frac { 2 5 } { s ^ { 2 } + 4 s + 2 5 } .$

$$G (s) = \frac {9 (s ^ {2} + 0 . 2 s + 1)}{s (s ^ {2} + 1 . 2 s + 9)}$$

Plot a bode diagram.

MATLAB Program 7–2 plots a Bode diagram for the system. The resulting plot is shown in Figure 7–22. The frequency range in this case is automatically determined to be from 0.01 to 10 radsec.

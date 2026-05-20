# Constructing the Bode Diagram Using MATLAB

The previous example illustrates how relatively easy the frequency response can be determined if we are given the Bode diagram. In Example 9.5 we used the Bode diagram in Fig. 9.15 to determine the frequency response for an input frequency ?? = 7 rad/s; however, we could have computed the frequency response for any input frequency between 0.1 and 100 rad/s as this is the range shown in Fig. 9.15.

Several textbooks such as References 1 and 2 present rules for constructing the approximate Bode diagram from linear asymptotes for the low- and high-frequency ranges (this calculation is presented by Problem 9.9 at the end of this chapter). Although these approximate methods can offer insight into how magnitude and phase vary with frequency, it is this author’s opinion that it is more important for the system engineer to know how to use the Bode diagram than it is to know how to construct an approximate Bode diagram. This opinion is reinforced by the fact that the exact Bode diagram can be easily constructed by a single MATLAB command. To illustrate, let’s construct the Bode diagram for the transfer function used in Table 9.1 and Fig. 9.15

$$G (s) = \frac {6}{s + 4} \tag {9.48}$$

The required MATLAB commands are

$$
\begin{array}{l} > > \text { sysG } = t f (6, [ 1 4 ]) \\ \% \text{ create the system, transfer function } G(s) \\ > > \text { bode(sysG) } \\ \% \text{ create and draw the Bode diagram for } G(s) \\ \end{array}
$$

The bode command draws the Bode diagram to the screen where magnitude is in decibels, phase is in degrees, and the frequency (rad/s) is plotted on a logarithmic scale.

The bode command can be modified to compute the magnitude and phase of the sinusoidal transfer function G( j??) for a desired frequency ?? by using the following format

$$
\begin{array}{l} > > \mathrm{w} = 7; \\ \% \text{set desired input frequency} \omega = 7 \text{rad / s} \\ > > [ \text { mag }, \text { phase } ] = \text { bode(sysG,w) } \\ \% \text{compute magnitude and phase (degrees)} \\ \end{array}
$$

No plot of the Bode diagram is drawn to the screen. The magnitude mag is the absolute value of G( j??). If the magnitude in decibels is desired, the additional MATLAB command is required:

```txt
>> magdB = 20*log10 (mag) % magnitude of G(jω) in decibels 
```

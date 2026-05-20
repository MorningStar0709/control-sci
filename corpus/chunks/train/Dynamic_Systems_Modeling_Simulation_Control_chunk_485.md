As we already know how to compute the magnitude and phase of $G ( j \omega )$ , we can illustrate the Bode diagram with the following simple example. Consider the simple first-order transfer function

$$G (s) = \frac {6}{s + 4} \tag {9.44}$$

Replacing s with j?? the sinusoidal transfer function is

$$G (j \omega) = \frac {6}{j \omega + 4} \tag {9.45}$$

Using Eqs. (9.13) and (9.14) the magnitude and phase of the sinusoidal transfer function are

$$\text { Magnitude: } \quad | G (j \omega) | = \frac {\sqrt {6 ^ {2} + 0 ^ {2}}}{\sqrt {4 ^ {2} + \omega^ {2}}} \tag {9.46}\text { Phase: } \quad \phi = \angle G (j \omega) = \tan^ {- 1} \left(\frac {0}{6}\right) - \tan^ {- 1} \left(\frac {\omega}{4}\right) \tag {9.47}$$

We can use Eqs. (9.46) and (9.47) to compute the magnitude and phase for a wide range of input frequencies. Table 9.1 summarizes these two key frequency response parameters for frequencies ranging from $\omega = 0 . 1$ rad/s (or, “low frequency” with a period of 62.8 s) to $\omega = 1 0 0$ rad/s (or, “high frequency” with a period of 0.06 s). Note that the corresponding magnitude in decibels using Eq. (9.42) is also presented in Table 9.1, and that the phase angle has been converted from radians to degrees. At very low frequency (say, as $\omega  0 )$ ), the magnitude approaches the DC gain of transfer function G(s) (i.e., 6/4 = 1.5, or $2 0 \log _ { 1 0 } ( 1 . 5 ) =$ 3.522 dB) and the phase approaches zero. At very high frequency $( \omega  \infty )$ the magnitude approaches zero $( \mathrm { o r } , 2 0 \mathrm { l o g } _ { 1 0 } ( 0 + )  - \infty$ dB) and the phase approaches $- 9 0 ^ { \circ }$ .

Figure 9.15 shows the Bode diagram for the first-order transfer function (9.44). The nine values of magnitude and phase from Table 9.1 are shown as discrete points in Fig. 9.15. Figure 9.15 shows that the Bode diagram consists of the two graphs: the top plot is magnitude (in decibels) vs. frequency (rad/s) and the bottom plot is phase (degrees) vs. frequency. The common frequency axis (i.e., the independent variable) is plotted on a logarithmic scale so that a wide range of input frequency can be shown.

Table 9.1 Magnitude and Phase of First-Order Transfer Function $G ( s ) = 6 / ( s + 4 )$

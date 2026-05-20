We need to find the frequency point where, when the lead compensator is added, the total magnitude becomes 0 dB.

From Figure 7–145 we see that the frequency point where the magnitude of $G _ { 1 } ( j \omega )$ is $- 6 . 7 7 7 8$ dB occurs between $\omega = 1$ and 10 radsec. Hence, we plot a new Bode diagram of $G _ { 1 } ( j \omega )$ in the frequency range between $\omega = 1$ and 10 to locate the exact point where $G _ { 1 } ( j \omega ) = - 6 . 7 7 7 8 ~ \mathrm { d B . M A T L A E }$ Program 7–25 produces the Bode diagram in this frequency range, which is shown in Figure 7–146. From this diagram, we find the frequency point where $\left| G _ { 1 } ( j \omega ) \right| = - 6 . 7 7 7 8$ occurs at dB $\omega = 6 . 5 6 8 6 \mathrm { r a d / s e c }$ . Let us select this frequency to be the new gain crossover frequency, or $\omega _ { c } = 6 . 5 6 8 6 ~ \mathrm { r a d / s e c }$ . Noting that this frequency corresponds to $\bar { 1 } / ( \sqrt { \alpha } T )$ o r,

$$\omega_ {c} = \frac {1}{\sqrt {\alpha} T}$$

we obtain

$$\frac {1}{T} = \omega_ {c} \sqrt {\alpha} = 6. 5 6 8 6 \sqrt {0 . 2 1} = 3. 0 1 0 1$$

and

$$\frac {1}{\alpha T} = \frac {\omega_ {c}}{\sqrt {\alpha}} = \frac {6 . 5 6 8 6}{\sqrt {0 . 2 1}} = 1 4. 3 3 3 9$$

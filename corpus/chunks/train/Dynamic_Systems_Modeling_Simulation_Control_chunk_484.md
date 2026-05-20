# 9.3 BODE DIAGRAMS

If the reader reviews the previous section and examples, he or she will see that the frequency response of an LTI system is completely determined by the magnitude and phase angle of the sinusoidal transfer function $G ( j \omega )$ . To emphasize this point, we repeat the frequency-response equation (9.17)

$$y _ {\mathrm{ss}} (t) = | G (j \omega) | U _ {0} \sin (\omega t + \phi) \tag {9.41}$$

where the (known) sinusoidal input is $u ( t ) = U _ { 0 }$ sin ??t. Hence, the frequency response (9.41) can be determined if we can compute $| G ( j \omega ) |$ and $\phi = \angle G ( j \omega )$ .

| |In the 1930s, H.W. Bode developed a graphical depiction of the magnitude (or amplitude ratio) $| G ( j \omega ) |$ and phase angle ?? plotted as a function of the input frequency ??. This graphical diagram (now called the Bode plot or Bode diagram) consists of two plots: (1) magnitude $| G ( j \omega ) |$ vs. input frequency ?? and (2) phase angle ?? vs. input frequency ??. The magnitude is plotted on a logarithmic scale and both plots share a common logarithmic scale for the independent variable (frequency, ??). Magnitude $| G ( j \omega ) |$ is plotted in decibels (dB), which is defined using the base-10 logarithm

$$| G (j \omega) | \text { in dB } \equiv 2 0 \log_ {1 0} | G (j \omega) | \tag {9.42}$$

Let us denote the absolute-value magnitude as G( j??) and its corresponding value in decibels as $| G ( j \omega ) | _ { \mathrm { d B } }$ . As a quick example, consider the magnitude $| G ( j \omega ) | = 0 . 1 6$ . Using Eq. (9.42) the corresponding magnitude in decibels is $| G ( j \omega ) | _ { \mathrm { d B } } = 2 0 1 \mathrm { o g } _ { 1 0 } ( 0 . 1 6 ) = - 3 6 . 6 5 \mathrm { d B }$ . Hence, while magnitude (or absolute value) $| G ( j \omega ) |$ is always positive, its corresponding magnitude in decibels may be positive or negative. Converting the magnitude in decibels to an absolute-value magnitude requires the inverse of Eq. (9.42):

$$| G (j \omega) | = 1 0 ^ {| G (j \omega) | _ {\mathrm{dB}} / 2 0} \tag {9.43}$$

We can summarize a few key properties linking the absolute-value magnitude $| G ( j \omega ) |$ with the magnitude in decibels, $\big | G ( j \omega ) \big | _ { \mathrm { d B } } \big :$

1. $2 0 \log _ { 1 0 } ( 1 ) = 0$ dB; therefore, unity amplitude ratio = 0 dB   
2. If $| G ( j \omega ) | > 1 , | G ( j \omega ) | _ { \mathrm { d B } } > 0$   
3. If $| G ( j \omega ) | < 1 , | G ( j \omega ) | _ { \mathrm { d B } } < 0$   
4. Very small $| G ( j \omega ) |$ results in large negative $| G ( j \omega ) | _ { \mathrm { d B } }$

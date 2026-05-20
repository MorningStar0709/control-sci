# 7–2 BODE DIAGRAMS

Bode Diagrams or Logarithmic Plots. A Bode diagram consists of two graphs: One is a plot of the logarithm of the magnitude of a sinusoidal transfer function; the other is a plot of the phase angle; both are plotted against the frequency on a logarithmic scale.

The standard representation of the logarithmic magnitude of G(jv) is 20 log @G(jv)@, where the base of the logarithm is 10.The unit used in this representation of the magnitude is the decibel, usually abbreviated dB. In the logarithmic representation, the curves are drawn on semilog paper, using the log scale for frequency and the linear scale for either magnitude (but in decibels) or phase angle (in degrees). (The frequency range of interest determines the number of logarithmic cycles required on the abscissa.)

The main advantage of using the Bode diagram is that multiplication of magnitudes can be converted into addition. Furthermore, a simple method for sketching an approximate log-magnitude curve is available. It is based on asymptotic approximations. Such approximation by straight-line asymptotes is sufficient if only rough information on the frequency-response characteristics is needed. Should the exact curve be desired, corrections can be made easily to these basic asymptotic plots. Expanding the low-frequency range by use of a logarithmic scale for the frequency is highly advantageous, since characteristics at low frequencies are most important in practical systems. Although it is not possible to plot the curves right down to zero frequency because of the logarithmic frequency (log 0=– q), this does not create a serious problem.

Note that the experimental determination of a transfer function can be made simple if frequency-response data are presented in the form of a Bode diagram.

Basic Factors of ${ \cal G } ( j \omega ) { \cal H } ( j \omega )$ . As stated earlier, the main advantage in using the logarithmic plot is the relative ease of plotting frequency-response curves. The basic factors that very frequently occur in an arbitrary transfer function $G ( j \omega ) H ( j \omega )$ are

1. Gain K   
2. Integral and derivative factors $\left( j \omega \right) ^ { \mp 1 }$   
3. First-order factors $( 1 + j \omega T ) ^ { \mp 1 }$   
4. Quadratic factors $\smash { \bigl [ 1 + 2 \zeta \bigl ( j \omega / \omega _ { n } \bigr ) + \bigl ( j \omega / \omega _ { n } \bigr ) ^ { 2 } \bigr ] ^ { \mp 1 } }$

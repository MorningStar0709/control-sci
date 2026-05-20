To determine the transfer function, we first draw asymptotes to the experimentally obtained log-magnitude curve. The asymptotes must have slopes of multiples of ;20 dBdecade. If the slope of the experimentally obtained log-magnitude curve changes from –20 to –40 dBdecade at $\mathbf { \omega } _ { \omega } = \mathbf { \omega } _ { 1 }$ , it is clear that a factor $1 \ 7 [ 1 + j ( \omega / \omega _ { 1 } ) ]$ exists in the transfer function. If the slope changes by –40 dBdecade at $\mathbf { \omega } _ { \omega } = \mathbf { \omega } _ { 2 }$ , there must be a quadratic factor of the form

$$\frac {1}{1 + 2 \zeta \left(j \frac {\omega}{\omega_ {2}}\right) + \left(j \frac {\omega}{\omega_ {2}}\right) ^ {2}}$$

in the transfer function. The undamped natural frequency of this quadratic factor is equal to the corner frequency $\omega _ { 2 }$ . The damping ratio $\zeta$ can be determined from the experimentally obtained log-magnitude curve by measuring the amount of resonant peak near the corner frequency $\omega _ { 2 }$ and comparing this with the curves shown in Figure 7–9.

Once the factors of the transfer function $G ( j \omega )$ have been determined, the gain can be determined from the low-frequency portion of the log-magnitude curve. Since such terms as $1 + j ( \omega / \omega _ { 1 } )$ and $1 + 2 \zeta \big ( j \omega / \omega _ { 2 } \big ) + \big ( j \omega / \omega _ { 2 } \big ) ^ { 2 }$ become unity as v approaches zero, at very low frequencies the sinusoidal transfer function $G ( j \omega )$ can be written

$$\lim _ {\omega \rightarrow 0} G (j \omega) = \frac {K}{(j \omega) ^ {\lambda}}$$

In many practical systems, l equals 0, 1, or 2.

1. For l=0, or type 0 systems,

$$G (j \omega) = K, \quad \text { for } \omega \ll 1$$

or

$$2 0 \log | G (j \omega) | = 2 0 \log K, \quad \text { for } \omega \ll 1$$

The low-frequency asymptote is a horizontal line at 20 log K dB. The value of K can thus be found from this horizontal asymptote.

2. For l=1, or type 1 systems,

$$G (j \omega) = \frac {K}{j \omega}, \quad \text { for } \omega \ll 1$$

or

$$2 0 \log | G (j \omega) | = 2 0 \log K - 2 0 \log \omega , \quad \text { for } \omega \ll 1$$

which indicates that the low-frequency asymptote has the slope –20 dBdecade. The frequency at which the low-frequency asymptote (or its extension) intersects the 0-dB line is numerically equal to K.

3. For l=2, or type 2 systems,

$$G (j \omega) = \frac {K}{(j \omega) ^ {2}}, \quad \text { for } \omega \ll 1$$

or

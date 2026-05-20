Note that $\frac { d \ln | { \cal L } ( j \omega ) | } { d \nu }$ is the slope of the Bode plot, which is generally negative for dν almost all frequencies. It follows that $\angle L ( j \omega _ { 0 } )$ will be large if the gain L attenuates slowly near $\omega _ { 0 }$ and small if it attenuates rapidly near $\omega _ { 0 }$ . For example, suppose the slope $\frac { d \ln | L ( j \omega ) | } { d \nu } = - \ell ;$ that is, (−20\` dB per decade), in the neighborhood of $\omega _ { \mathrm { 0 } } ;$ then it is reasonable to expect

$$
\angle L (j \omega_ {0}) <   \left\{ \begin{array}{l l} - \ell \times 6 5. 3 ^ {\circ}, & \text {if the slope of L = -\ell for \frac {1}{3} \leq\frac {\omega}{\omega_{0}} \leq 3} \\ - \ell \times 7 5. 3 ^ {\circ}, & \text {if the slope of L = -\ell for \frac {1}{5} \leq\frac {\omega}{\omega_{0}} \leq 5} \\ - \ell \times 8 2. 7 ^ {\circ}, & \text {if the slope of L = -\ell for \frac {1}{10} \leq\frac {\omega}{\omega_{0}} \leq 10}. \end{array} \right.
$$

The behavior of $\angle L ( j \omega )$ is particularly important near the crossover frequency $\omega _ { c } ,$ where $| L ( j \omega _ { c } ) | = 1$ since $\pi + \angle L ( j \omega _ { c } )$ is the phase margin of the feedback system. Further, the return difference is given by

$$| 1 + L (j \omega_ {c}) | = | 1 + L ^ {- 1} (j \omega_ {c}) | = 2 \left| \sin \frac {\pi + \angle L (j \omega_ {c})}{2} \right|,$$

which must not be too small for good stability robustness. $\mathrm { I f } \ \pi + \angle L ( j \omega _ { c } )$ is forced to be very small by rapid gain attenuation, the feedback system will amplify disturbances and exhibit little uncertainty tolerance at and near $\omega _ { c }$ . Since it is generally required that the loop transfer function $L$ roll off as fast as possible in the high-frequency range, it is reasonable to expect that $\angle L ( j \omega _ { c } )$ is at most $- \ell \times 9 0 ^ { \mathrm { o } }$ if the slope of $L ( j \omega )$ is $- \ell$ near $\omega _ { c }$ . Thus it is important to keep the slope of L near $\omega _ { c }$ not much smaller than $- 1$ for a reasonably wide range of frequencies in order to guarantee some reasonable performance. The conflict between attenuation rate and loop quality near crossover is thus clearly evident.

Bode’s gain and phase relation can be extended to stable and nonminimum phase transfer functions easily. Let $z _ { 1 } , z _ { 2 } , \ldots , z _ { k }$ be the right-half plane zeros of $L ( s )$ , then $L$ can be factorized as

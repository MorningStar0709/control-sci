# EXAMPLE 8.1 Relay oscillation

Consider a system with relay feedback as in Fig. 8.3 with

$$G (s) = \frac {K \alpha}{s (s + 1) (s + \alpha)}$$

K = 5, $\alpha = 10$ , d = 1, and $u_{c} = 0$ . This was the system used to generate Fig. 8.4. Simple calculations show that

$$
\begin{array}{l} \arg G (i \omega_ {u}) = - \frac {\pi}{2} - \tan^ {- 1} \omega_ {u} - \tan^ {- 1} \frac {\omega_ {u}}{\alpha} \\ = - \frac {\pi}{2} - \tan^ {- 1} \frac {\omega_ {u} (\alpha + 1)}{\alpha - \omega_ {u} ^ {2}} = - \pi \\ \end{array}
$$

This implies that the Nyquist curve intersects the negative real axis for $\omega_{u} = \sqrt{\alpha}$ . The approximative analysis thus gives the following estimate of the period:

$$T _ {u} = \frac {2 \pi}{\sqrt {\alpha}} = \frac {6 . 2 8}{\sqrt {\alpha}} = 1. 9 9$$

Using Eqs. (8.8) gives $\alpha = 4d|G(i\omega_{u})|/\pi = 0.58$ . From the simulations it can be determined that the true values are $T_{u} = 2.07$ and $\alpha = 0.62$ , which show that the describing function method gives fair but not very accurate estimates in this example.

Several refinements of the method are useful. The amplitude of the limit cycle oscillation can be specified by introducing a feedback that adjusts the relay amplitude. A hysteresis in the relay is useful to make the system less sensitive to noise. The parameters $T_{u}$ and $K_{u}$ can be used to determine the parameters of a PID regulator. The method can be made insensitive to disturbances by comparing and averaging over several periods of the oscillation.

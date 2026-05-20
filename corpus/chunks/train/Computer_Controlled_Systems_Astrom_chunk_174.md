# Relative Stability

Amplitude and phase margins can be defined for discrete-time systems analogously to continuous-time systems.

DEFINITION 3.4 AMPLITUDE MARGIN Let the open-loop system have the pulse-transfer function $H(z)$ and let $\omega_{o}$ be the smallest frequency such that

$$\arg H (e ^ {i \omega_ {o} h}) = - \pi$$

and such that $H(e^{i\omega_{o}h})$ is decreasing for $\omega = \omega_{0}$ . The amplitude or gain margin is then defined as

$$A _ {\mathrm{marg}} = \frac {1}{| H (e ^ {i \omega_ {0} h}) |}$$

DEFINITION 3.5 PHASE MARGIN Let the open-loop system have the pulse-transfer function $H(z)$ and further let the crossover frequency $\omega_c$ be the smallest frequency such that

$$\left| H (e ^ {i \omega_ {c} h}) \right| = 1$$

The phase margin $\phi_{\mathrm{marg}}$ is then defined as

$$\phi_ {\mathrm{marg}} = \pi + \arg H (e ^ {i \omega_ {c} h})$$

In words, the amplitude margin is how much the gain can be increased before the closed-loop system becomes unstable. The phase margin is how much extra phase lag is allowed before the closed-loop system becomes unstable.

The amplitude and phase margins are easily determined from the Nyquist and Bode diagrams.

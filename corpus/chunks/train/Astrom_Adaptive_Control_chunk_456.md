# Sinusoidal Command Signals

Several of the difficulties encountered with step commands are due to the fact that a step is persistently exciting of first order only. This means that the equilibrium set is a manifold and only a linear combination of the parameters can be determined. With a sinusoidal command signal that is persistently exciting of second order, two parameters can be determined consistently. It may therefore be expected that some of the difficulties will disappear. However, the simulation shown in Fig. 6.14 indicates that there are some problems with sinusoidal command signals in combination with unmodeled dynamics.

As before, it is assumed that the adaptive controller is designed as if the process were described by the transfer function

$$G (s) = \frac {b}{s + a}$$

Since the character of the unmodeled dynamics is important, it is assumed that the actual plant is described by the frequency function

$$G (i \omega) = \frac {b}{a + i \omega} r (\omega) e ^ {- i \phi (\omega)} \tag {6.67}$$

The functions $r$ and $\phi$ represent the distortions of amplitude and phase due to unmodeled dynamics. It is assumed that the transfer function corresponding to $r$ and $\phi$ has no poles in the right half-plane.

The unmodeled dynamics may change the properties of the system drastically. For example, the nominal system will be stable for all values of the feedback gain, since it is SPR. If the unmodeled dynamics are such that the additional phase lag can be large, the system with unmodeled dynamics will be unstable for sufficiently large feedback gains. The critical gain can be determined as follows. The phase lag of the plant is $\phi(\omega) + \arctan(\omega/\alpha)$ . This lag is $\pi$ if

$$\frac {\omega}{a} = \tan (\pi - \phi (\omega)) = - \tan \phi (\omega)$$

or

$$\omega \cos \phi (\omega) + a \sin \phi (\omega) = 0 \tag {6.68}$$

The process gain of this frequency is

$$| G (i \omega) | = \frac {b r (\omega)}{\sqrt {a ^ {2} + \omega^ {2}}}$$

The system thus becomes unstable for the gain

$$\bar {\theta} _ {2} = \bar {\theta} _ {2} ^ {0} = \frac {\sqrt {a ^ {2} + \omega^ {2}}}{b r (\omega)} \tag {6.69}$$

where $\omega$ is the smallest value that satisfies Eq. (6.68).

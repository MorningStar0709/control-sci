# Equilibrium Analysis

The possible equilibria of the parameters will first be determined. Introducing the transfer function of Eq. (6.67) into Eq. (6.59) gives (after straightforward but tedious calculations)

$$
\hat {\theta} _ {1} = \frac {b _ {m}}{b} \cdot \frac {(a \sin \phi (\omega) + \omega \cos \phi (\omega))}{\omega r (\omega)}
\begin{array}{l} \hat {\theta} _ {2} = \frac {\omega (a _ {m} - a) \cos \phi (\omega) + \left(\omega^ {2} + a a _ {m}\right) \sin \phi (\omega)}{\omega b r (\omega)} \tag {6.70} \\ = \frac {1}{b r (\omega)} \left(\left(\omega \sin \phi (\omega) - a \cos \phi (\omega)\right) + \frac {a _ {m}}{\omega} (a \sin \phi (\omega) + \omega \cos \phi (\omega))\right) \\ \end{array}
$$

A comparison with the nominal case shows that the equilibrium will be shifted because of the unmodeled dynamics. The shift in the equilibrium depends on the frequency of the input signal as well as on the unmodeled dynamics.

It is of particular interest to determine whether there are conditions that may lead to difficulties. The feedforward gain vanishes for frequencies such that Eq. (6.68) is satisfied. This is precisely the frequency at which the process has a phase lag of $180^{\circ}$ . The feedback gain for this frequency is

$$\hat {\theta} _ {2} = \frac {1}{b r (\omega)} \left(\omega \sin \phi - a \cos \phi\right) = \frac {\sqrt {a ^ {2} + \omega^ {2}}}{b r (\omega)}$$

This implies that $\hat{\theta}_2|G(i\omega)| = 1$ , that is, that the loop gain then becomes unity.

We thus find that the equilibrium values of the parameters for sinusoidal input signals will depend on the unmodeled dynamics and the frequency of the sinusoidal command signal. When the frequency is such that the plant has a phase shift of $180^{\circ}$ , the feedforward gain is zero and the feedback gain is such that the closed-loop system is unstable. This observation is illustrated by an example.

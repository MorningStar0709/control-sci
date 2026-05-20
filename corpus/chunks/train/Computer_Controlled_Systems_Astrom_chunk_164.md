# Example 3.1 Harmonic oscillator

Consider the sampled harmonic oscillator (see Example A.3)

$$
\begin{array}{l} x (k h + h) = \left( \begin{array}{c c} \cos \omega h & \sin \omega h \\ - \sin \omega h & \cos \omega h \end{array} \right) x (k h) + \binom {1 - \cos \omega h} {\sin \omega h} u (k h) \\ y (k h) = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x (k h) \\ \end{array}
$$

The magnitude of the eigenvalues is one. The system is stable because $\|x(kh)\| = \|x(0)\|$ if $u(kh) = 0$ . Let the input be a square wave with the frequency $\omega$ rad/s. By using the z-transform, it is easily seen that the output contains a sinusoidal function with growing amplitude and the system is not BIBO stable. Figure 3.1 shows the input and output of the system. The input signal is exciting the system at its undamped frequency and the output amplitude is growing.

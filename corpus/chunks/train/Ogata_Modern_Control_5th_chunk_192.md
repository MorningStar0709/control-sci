where $\omega _ { d } = \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } }$ The frequency. $\omega _ { d }$ is called the damped natural frequency. For a unit-step input, $C ( s )$ can be written

$$C (s) = \frac {\omega_ {n} ^ {2}}{\left(s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}\right) s} \tag {5-11}$$

The inverse Laplace transform of Equation (5–11) can be obtained easily if $C ( s )$ is written in the following form:

$$
\begin{array}{l} C (s) = \frac {1}{s} - \frac {s + 2 \zeta \omega_ {n}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}} \\ = \frac {1}{s} - \frac {s + \zeta \omega_ {n}}{\left(s + \zeta \omega_ {n}\right) ^ {2} + \omega_ {d} ^ {2}} - \frac {\zeta \omega_ {n}}{\left(s + \zeta \omega_ {n}\right) ^ {2} + \omega_ {d} ^ {2}} \\ \end{array}
$$

Referring to the Laplace transform table in Appendix A, it can be shown that

$$\mathscr {L} ^ {- 1} \left[ \frac {s + \zeta \omega_ {n}}{\left(s + \zeta \omega_ {n}\right) ^ {2} + \omega_ {d} ^ {2}} \right] = e ^ {- \zeta \omega_ {n} t} \cos \omega_ {d} t\mathcal {L} ^ {- 1} \left[ \frac {\omega_ {d}}{(s + \zeta \omega_ {n}) ^ {2} + \omega_ {d} ^ {2}} \right] = e ^ {- \zeta \omega_ {n} t} \sin \omega_ {d} t$$

Hence the inverse Laplace transform of Equation (5–11) is obtained as

$$
\begin{array}{l} \mathscr {L} ^ {- 1} \bigl [ C (s) \bigr ] = c (t) \\ = 1 - e ^ {- \zeta \omega_ {n} t} \left(\cos \omega_ {d} t + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {d} t\right) \\ = 1 - \frac {e ^ {- \zeta \omega_ {n} t}}{\sqrt {1 - \zeta^ {2}}} \sin \left(\omega_ {d} t + \tan^ {- 1} \frac {\sqrt {1 - \zeta^ {2}}}{\zeta}\right), \quad \text { for   } t \geq 0 \tag {5-12} \\ \end{array}
$$

From Equation (5–12), it can be seen that the frequency of transient oscillation is the damped natural frequency $\omega _ { d }$ and thus varies with the damping ratio $\zeta .$ . The error signal for this system is the difference between the input and output and is

$$
\begin{array}{l} e (t) = r (t) - c (t) \\ = e ^ {- \zeta \omega_ {n} t} \left(\cos \omega_ {d} t + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {d} t\right), \quad \text { for } t \geq 0 \\ \end{array}
$$

This error signal exhibits a damped sinusoidal oscillation. At steady state, or at $t = \infty$ , no error exists between the input and output.

If the damping ratio $\zeta$ is equal to zero, the response becomes undamped and oscillations continue indefinitely. The response $c ( t )$ for the zero damping case may be obtained by substituting $\zeta = 0$ in Equation (5–12), yielding

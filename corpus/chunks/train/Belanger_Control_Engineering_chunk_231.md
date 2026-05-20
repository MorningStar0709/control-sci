# Example 4.11 (Level Control)

Consider the level-control system of Example 4.5. Suppose that the disturbance d referred to the output is relatively small and has a spectrum extending to about 2 rad/s. Suppose also that the system is called upon to handle relatively large set-point changes, and to do so without undue valve motion. To handle the disturbances, let $T(s) = \omega_{0}^{2}/(s^{2} + \sqrt{2}\omega_{0}s + \omega_{0}^{2})$ , with $\omega_{0} = 2$ rad/s. To avoid large inputs in response to set-point changes, let $y/y_{d}$ be similar in form to $T(s)$ , but with $\omega_{0} = 0.5$ rad/s. The response will be slow, but the input will be less likely to “kick.” Design the required 2-DOF system.

Solution First, design the 1-DOF loop to handle disturbances. We have

$$S (s) = 1 - T (s) = \frac {s ^ {2} + 2 \sqrt {2} s}{s ^ {2} + 2 \sqrt {2} s + 4}$$

and

$$
\begin{array}{l} F (s) = \frac {T}{S P} = \frac {4}{s (s + 2 \sqrt {2})} \frac {s + . 0 0 5}{- 2} \\ = \frac {- 2 (s + . 0 0 5)}{s (s + 2 . 8 2)}. \\ \end{array}
$$

Next, design $R(s)$ . We have

$$R P S = \frac {. 2 5}{s ^ {2} + . 5 \sqrt {2} s + . 2 5}.$$

Note that any stable transfer function RPS is allowed, because P has no RHP zeros. Going on,

$$R = \frac {0 . 2 5}{s ^ {2} + . 7 0 7 s + . 2 5} \frac {s ^ {2} + 2 . 8 2 s + 4}{s (s + 2 . 8 2)} \cdot \frac {s + . 0 0 5}{- 2}= \frac {- 0 . 1 2 5 (s ^ {2} + 2 . 8 2 s + 4) (s + . 0 0 5)}{s (s + 2 . 8 2) (s ^ {2} + . 7 0 7 s + . 2 5)}.$$

The compensator in the feedback path is

$$\frac {F}{R} = \frac {1 6 (s ^ {2} + . 7 0 7 s + . 2 5)}{s ^ {2} + 2 . 8 2 s + 4}.$$

# Example 6.13 (dc Servo)

In Example 6.8, a lag compensator was designed for the dc servo, with a resulting closed-loop bandwidth of about 1 rad/s. The load torque is assumed available for measurement, to be used as an input for feedforward control. Design such a control to improve the response to disturbances up to 10 rad/s.

Solution From Equations 3.21 and 3.22,

$$P (s) = \frac {\theta}{v} = \frac {8 8 . 7 6}{s (s + 2 1 . 5 2 6) (s + 2 . 4 7 4)}P _ {w} (s) = \frac {\theta}{T _ {L}} = \frac {- 7 . 3 9 6 (s + 2 4)}{s (s + 2 1 . 5 2 6) (s + 2 . 4 7 4)}$$

so that

$$\frac {P _ {w}}{P} = \frac {- 7 . 3 9 6}{8 8 . 7 6} (s + 2 4) = - 2. 0 0 \left(\frac {s}{2 4} + 1\right).$$

Over the specified frequency range, the approximation Q = -2.00 is valid, so the feedforward control is

$$v _ {f f} = - 2. 0 0 T _ {L}.$$

Figure 6.29 shows the magnitude of the frequency response from disturbance to output, with and without feedforward.

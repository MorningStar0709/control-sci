# Example 6.14 (Active Suspension)

In Example 6.9, a PI controller was designed for the active suspensions. The bandwidth of 3.51 rad/s would suggest a time constant of the order 0.3s, probably too fast to lead to comfortable set-point changes. A response to set point with a time constant of the order of 3s is desired. Use a 2-DOF design to achieve this.

Solution The PI controller is

$$F (s) = G _ {c} (s) = 2 4 2 7 \frac {(2 . 8 5 s + 1)}{2 . 8 5 s}.$$

Since 1/2.85 is well below the bandwidth of 3.51 rad/s, we choose $R'(s) = 1/(2.85s + 1)$ . The time constant of 2.85s is close enough to 3s, and leads to simplification.

The two compensators are:

Forward path: $R = FR' = \frac{851.6}{s}$

Feedback path: $\frac{F}{R} = \frac{1}{R'} = 2.85s + 1$ .

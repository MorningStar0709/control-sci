# Example 2.6 (dc Servo)

For the servomechanism of Example 2.1, calculate the constant equilibrium point for $T_{L}=0$ and $\theta^{*}=\theta_{d}$ . Give the incremental model.

Solution From Equation 2.17 and the first of the two output equations in Equation 2.18, application of Equation 2.53 yields

$$
\left[ \begin{array}{l} 0 \\ 0 \\ 0 \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & \frac {N K _ {m}}{J _ {e}} \\ 0 & \frac {- N K _ {m}}{L} & - \frac {R}{L} \end{array} \right] \left[ \begin{array}{l} \theta^ {*} \\ \omega^ {*} \\ i ^ {*} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ \frac {1}{L} \end{array} \right] v ^ {*}

\theta_ {d} = [ 1 \quad 0 \quad 0 ] \left[ \begin{array}{l} \theta^ {*} \\ \omega^ {*} \\ i ^ {*} \end{array} \right].
$$

\- It follows easily that $\omega^{*} = i^{*} = v^{*} = 0$ .

The incremental variables are

$$\Delta \theta = \theta - \theta_ {d}, \quad \Delta \omega = \omega - \omega^ {*} = \omega , \quad \Delta i = i - i ^ {*} = i, \quad \Delta v = v - v ^ {*} = v.$$

Following Equation 2.55, the incremental model is

$$
\frac {d}{d t} \left[ \begin{array}{c} \Delta \theta \\ \omega \\ i \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & \frac {N K _ {m}}{J _ {e}} \\ 0 & \frac {- N K _ {m}}{L} & \frac {- R}{L} \end{array} \right] \left[ \begin{array}{c} \Delta \theta \\ \omega \\ i \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ \frac {1}{L} \end{array} \right] v

\left[ \begin{array}{c} \Delta \theta \\ \omega \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{c} \Delta \theta \\ \omega \\ i \end{array} \right].
$$

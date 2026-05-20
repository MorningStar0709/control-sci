<table><tr><td>Type of Controller</td><td> $K_p$ </td><td> $T_i$ </td><td> $T_d$ </td></tr><tr><td>P</td><td> $0.5K_{\text{cr}}$ </td><td> $\infty$ </td><td>0</td></tr><tr><td>PI</td><td> $0.45K_{\text{cr}}$ </td><td> $\frac{1}{1.2}P_{\text{cr}}$ </td><td>0</td></tr><tr><td>PID</td><td> $0.6K_{\text{cr}}$ </td><td> $0.5P_{\text{cr}}$ </td><td> $0.125P_{\text{cr}}$ </td></tr></table>

Notice that the PID controller tuned by the second method of Ziegler–Nichols rules gives

$$
\begin{array}{l} G _ {c} (s) = K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right) \\ = 0. 6 K _ {\mathrm{cr}} \left(1 + \frac {1}{0 . 5 P _ {\mathrm{cr}} s} + 0. 1 2 5 P _ {\mathrm{cr}} s\right) \\ = 0. 0 7 5 K _ {\mathrm{cr}} P _ {\mathrm{cr}} \frac {\left(s + \frac {4}{P _ {\mathrm{cr}}}\right) ^ {2}}{s} \\ \end{array}
$$

Thus, the PID controller has a pole at the origin and double zeros at $s = - 4 / P _ { \mathrm { c r } }$

Note that if the system has a known mathematical model (such as the transfer function), then we can use the root-locus method to find the critical gain $K _ { \mathrm { c r } }$ and the frequency of the sustained oscillations $\omega _ { \mathrm { c r } }$ , where $2 \pi / \omega _ { \mathrm { c r } } = P _ { \mathrm { c r } }$ These values can be found. from the crossing points of the root-locus branches with the jv axis. (Obviously, if the root-locus branches do not cross the jv axis, this method does not apply.)

Comments. Ziegler–Nichols tuning rules (and other tuning rules presented in the literature) have been widely used to tune PID controllers in process control systems where the plant dynamics are not precisely known. Over many years, such tuning rules proved to be very useful. Ziegler–Nichols tuning rules can, of course, be applied to plants whose dynamics are known. (If the plant dynamics are known, many analytical and graphical approaches to the design of PID controllers are available, in addition to Ziegler–Nichols tuning rules.)

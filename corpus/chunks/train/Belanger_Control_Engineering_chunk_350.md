$$
\begin{array}{l} F (s) = k \left(\frac {1}{T _ {1} s} + 1\right) \left(T _ {2} s + 1\right) \\ = \frac {k}{T _ {1}} \frac {(T _ {1} s + 1) (T _ {2} s + 1)}{s}. \\ \end{array}
$$

Typically, $T_{1}$ will be larger than $T_{2}$ . If the bandwidth is greater than $1/T_{1}$ , it is reasonable to use $R'(s)=\frac{1}{T_{1}s+1}$ , which, from Equation 6.48, will be approximately the set-point response.

From Figure 6.30, the two compensator blocks will be

Forward path: $R = FR' = \frac{k}{T_1}\frac{T_2s + 1}{s}$

Feedback path: $\frac{F}{R} = \frac{1}{R'} = T_1s + 1.$

The effect is to differentiate only the measurement and not the reference, so that step changes in the latter do not produce “spikes” on the control. Note that this design has a PI control in the forward path and a PD in the feedback path.

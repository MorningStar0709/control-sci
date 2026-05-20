# THEOREM 11.2 Compatibility of identification and control

The control performance error $e_{cp}$ is identical to the least-squares estimation error if identification is performed in closed loop and if the transfer function of the data filter is chosen to be

$$H _ {f} - \frac {R}{A _ {0} A _ {m}} \tag {11.44}$$

Proof: The proof is a straightforward calculation. The output of the true system is given by

$$y _ {0} = \frac {P _ {0} T}{R + P _ {0} S} u _ {\mathrm{c}} \tag {11.45}$$

and the control signal is

$$u _ {0} = \frac {T}{R + P _ {0} S} u _ {c} \tag {11.46}$$

The corresponding signals for the nominal plant are obtained simply by omitting the index 0 on $y_{0}$ , $u_{0}$ , and $P_{0}$ . The control performance error then becomes

$$
\begin{array}{l} e _ {c p} = \left(\frac {P _ {0} T}{R + P _ {0} S} - \frac {P T}{R + P S}\right) u _ {c} = \frac {R T (P _ {0} - P)}{(R + P _ {0} S) (R + P S)} u _ {c} \\ = \frac {R (P _ {0} - P)}{R + P S} u _ {0} - \frac {A R (P _ {0} - P)}{A _ {o} A _ {m}} u _ {0} \tag {11.47} \\ \end{array}
$$

where the first equality follows from Eqs. (11.43), (11.45), and (11.46). The second equality is obtained by a simple algebraic manipulation. The third follows from Eq. (11.46), and the last equality follows from Eq. (11.41). The least-squares estimation error is given by

$$e = H _ {f} (A y _ {0} - B u _ {0})$$

It follows from Eq. (11.47) that e and $e_{cp}$ are identical if estimation is based on closed-loop data and if the data filter is chosen to be Eq. (11.44). ☐

Remark 1. Notice that the denominator of the filter (11.44) is given by $A_{o}A_{m}$ , which are given by the specifications.

Remark 2. Notice that for a controller with integral action the filter (11.44) is a bandpass filter.

Remark 3. Notice that only the numerator of the filter has to be adapted. □

This result gives a rational way of choosing the data filter for a servo problem.

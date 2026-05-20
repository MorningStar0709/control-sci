# 4.3.5 Feedforward Control

Feedforward control is a variation of open-loop control. It is applicable when the disturbance input is measured. From Figure 4.14a it is easy to see that the effect of the disturbance on the output y will be nullified if $y' = -d$ . We set up an open-loop problem in Figure 4.14b, where the output is $y'$ and $y_d = -d$ . The open-loop controller F is chosen, as in the case of open-loop design, to make $y'$ as close as possible to $y_d$ . The final step is to generate $y_d = -d$ , as in Figure 4.14c; note that $P_w(s)$ , the transfer function relating the measured disturbance w to the output, is assumed to be known.

For feedforward control, with reference to Equation 4.5,

$$H _ {w} (s) = [ 1 - F (s) P (s) ] P _ {w} (s). \tag {4.25}$$

# Example 1.6 Difference equations

The input-output properties of the process Eq. (1.1) can be described by

$$y (t _ {k}) - 2 y (t _ {k - 1}) + y (t _ {k - 2}) = \frac {k h ^ {2}}{2 J} \left(u (t _ {k - 1}) + u (t _ {k - 2})\right) \tag {1.7}$$

This equation is exact if the control signal is constant over the sampling intervals. The deadbeat control strategy is given by Eq. (1.5) and the closed-loop system thus can be described by the equations.

$$
\begin{array}{l} y (t _ {k}) - 2 y (t _ {k - 1}) + y (t _ {k - 2}) = \alpha \left(u (t _ {k - 1}) + u (t _ {k - 2})\right) \tag {1.8} \\ u \left(t _ {k - 1}\right) + r _ {1} u \left(t _ {k - 2}\right) = t _ {0} u _ {c} \left(t _ {k - 1}\right) - s _ {0} y \left(t _ {k - 1}\right) - s _ {1} y \left(t _ {k - 2}\right) \\ \end{array}
$$

where $\alpha = kh^{2}/2J$ . Elimination of the control signal u between these equations gives

$$
\begin{array}{l} y (t _ {k}) + \left(r _ {1} - 2 + \alpha s _ {0}\right) y (t _ {k - 1}) + \left(1 - 2 r _ {1} + \alpha \left(s _ {0} + s _ {1}\right)\right) y (t _ {k - 2}) + \left(r _ {1} + \alpha s _ {1}\right) y (t _ {k - 3}) \\ = \frac {\alpha t _ {0}}{2} \left(u _ {c} \left(t _ {k - 1}\right) + u _ {c} \left(t _ {k - 2}\right)\right) \\ \end{array}
$$

The parameters of the deadbeat controller are given by

$$
\begin{array}{l} r _ {1} = 0. 7 5 \\ s _ {0} = \frac {1 . 2 5}{\alpha} = \frac {2 . 5 J}{k h ^ {2}} \\ s _ {1} = - \frac {0 . 7 5}{\alpha} = - \frac {1 . 5 J}{k h ^ {2}} \\ t _ {0} = \frac {1}{4 \alpha} = \frac {1}{2} \\ \end{array}
$$

With these parameters the closed-loop system becomes

$$y (t _ {k}) = \frac {1}{2} \left(u _ {\mathrm{c}} (t _ {k - 1}) + u _ {\mathrm{r}} (t _ {k - 2})\right)$$

It follows from this equation that the output is the average value of the past two values of the command signal. Compare with Fig. 1.9.

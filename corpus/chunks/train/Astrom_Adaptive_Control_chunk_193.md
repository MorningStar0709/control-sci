$$
\begin{array}{l} A _ {o} ^ {*} \left(q ^ {- 1}\right) A _ {m} ^ {*} \left(q ^ {- 1}\right) y (t + d) - A _ {o} (1) A _ {m} (1) y (t) \\ = b _ {0} \left(R ^ {\prime *} (q ^ {- 1}) \Delta^ {*} u (t) + S ^ {\prime *} (q ^ {- 1}) \Delta^ {*} y (t)\right) \\ = \mathcal {R} ^ {*} (q ^ {- 1}) \Delta^ {*} u (t) + S ^ {*} (q ^ {- 1}) \Delta^ {*} y (t) \tag {3.51} \\ \end{array}
$$

Division by $A_{o}^{*}A_{m}^{*}$ now gives

$$y (t + d) - \frac {A _ {o} (1) A _ {m} (1)}{A _ {o} ^ {*} (q ^ {- 1}) A _ {m} ^ {*} (q ^ {- 1})} y (t) = \mathcal {R} ^ {*} (q ^ {- 1}) u _ {f} (t) + \mathcal {S} ^ {*} (q ^ {- 1}) y _ {f} (t) \tag {3.52}$$

where

$$u _ {f} (t) = \frac {1 - q ^ {- 1}}{A _ {o} ^ {*} \left(q ^ {- 1}\right) A _ {m} ^ {*} \left(q ^ {- 1}\right)} u (t)y _ {f} (t) = \frac {1 - q ^ {- 1}}{A _ {o} ^ {*} \left(q ^ {- 1}\right) A _ {m} ^ {*} \left(q ^ {- 1}\right)} y (t)$$

Notice that the difference operation eliminates levels and that division by $A_{o}^{*}A_{m}^{*}$ corresponds to low-pass filtering. Thus the net effect is that the signals are band-pass filtered with filters that are matched to the desired closed-loop dynamics and the specified observer polynomial.

To complete the algorithm, it now remains to specify how the control law is obtained from the estimated parameters. To obtain the response to command signals given by Eq. (3.44), it follows from Eq. (3.51) that

$$\mathcal {R} ^ {*} (q ^ {- 1}) \Delta^ {*} u (t) + S ^ {*} (q ^ {- 1}) \Delta^ {*} y (t) + A _ {o} (1) A _ {m} (1) y (t) = A _ {o} ^ {*} (q ^ {- 1}) A _ {m} (1) u _ {c} (t)$$

A controller with integral action may perform poorly if there are actuators that saturate. The feedback loop is broken during saturation, and the integrator may drift to undesirable values. This phenomenon, which is called windup, can be avoided if the control algorithm is modified to

$$
\begin{array}{l} A _ {o} ^ {*} (q ^ {- 1}) \left(\tilde {u} (t) - A _ {m} (1) u _ {c} (t)\right) \\ = - A _ {o} (1) A _ {m} (1) y (t) - S ^ {*} \left(q ^ {- 1}\right) \Delta^ {*} y (t) \tag {3.53} \\ - \left(\mathcal {R} ^ {*} (q ^ {- 1}) \Delta^ {*} - A _ {o} ^ {*} (q ^ {- 1})\right) u (t) \\ \end{array}
u (t) = \mathrm{sat} \bar {u} (t)
$$

The windup phenomenon is discussed in detail in Section 11.2. In summary, Algorithm 3.6 is obtained.

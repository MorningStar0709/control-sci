# Main Result

The tools for explaining how the SOAS works are now available. Consider the system in Fig. 10.7. From Section 8.5 the period of the limit cycle is given by

Eqs. (8.8) when the describing function method is used. The amplitude of the limit cycle at the relay input is also given by Eqs. (8.8):

$$N _ {A} \left| G (i \omega_ {u}) \right| = 1 \tag {10.4}$$

The transmission of a sinusoidal signal through a relay can thus be approximately described by an equivalent gain, which is inversely proportional to the signal amplitude at the relay input. The amplitude thus automatically adjusts so that the loop gain is unity at the frequency $\omega_{u}$ .

Now consider the propagation of slowly varying signals superimposed on the limit cycle oscillations. The propagation of the signals through the linear parts of the system can be described by the transfer function $G(s)$ . If the signals vary slowly in comparison with the limit cycle oscillations, the propagation through the relay is approximately described by the dual-input describing function $N_{B}$ . The propagation of slowly varying signals is thus approximately described by the loop transfer function

$$G _ {0} (s) = N _ {B} (a) G (s)$$

It follows from Eqs. (10.3) and (10.4) that

$$\left| G _ {0} (i \omega_ {u}) \right| = N _ {B} (a) \left| G (i \omega_ {u}) \right| = \frac {1}{2} N _ {A} \left| G (i \omega_ {u}) \right| = 0. 5$$

We thus obtain the following important result, which describes the operation of the SOAS.

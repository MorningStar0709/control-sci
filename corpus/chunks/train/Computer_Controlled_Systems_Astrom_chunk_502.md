The systems (8.14) and (8.15) have the same poles up to and including order $h^{2}$ when

$$\tilde {L} = L \left(I + (A - B L) h / 2\right) \tag {8.16}$$

Without modification of $L$ the poles are the same up to and including order $h$ .

The modification of M is determined by assuming that the steady-state values are the same for (8.14) and (8.15). Let the reference value be constant and assume that the steady-state value of the state is $x^{0}$ . This gives the relations

$$(I - \Phi_ {c}) x ^ {0} = \Gamma_ {c} M u _ {c}$$

and

$$\left(I - (\Phi - \Gamma \tilde {L})\right) x ^ {0} = \Gamma \tilde {M} u _ {c}$$

The series expansions of the left-hand sides of these two relations are equal for powers of h up to and including $h^{2}$ . Now determine $\tilde{M}$ such that the series expansions of the right-hand sides are the same for h and $h^{2}$ . Assume that

$$\tilde {M} = M _ {0} + M _ {1} h / 2$$

then

$$\Gamma_ {c} M \approx B M h + (A - B L) B M h ^ {2} / 2 + \dots$$

and

$$\Gamma \tilde {M} \approx B M _ {0} h + (B M _ {1} + A B M _ {0}) h ^ {2} / 2 + \dots$$

This gives

$$\tilde {M} = (I - L B h / 2) M \tag {8.17}$$

The modifications (8.16) and (8.17) are easily computed using the continuous-time system and the continuous-time controller.

![](image/ce6f5d9d4e52f27b5b871a66faef258f6f968f1e8a1f442a14f3fbd3ea4bd0c3.jpg)  
Figure 8.7 Digital control of the double integrator (solid) using the control law in (8.19) when h = 0.5. The continuous-time response when using (8.18) is shown by the dashed curves.

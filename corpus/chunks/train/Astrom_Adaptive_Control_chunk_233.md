By using the same idea it is possible to construct a new system, which has Eq. (4.37) as its minimum-variance controller. Augment the original system with a parallel connection with the pulse transfer operator $\rho q^{-d_{0}}/r_{0}$ (see Fig. 4.9). This is in fact a standard technique to obtain an equivalent controller with a bounded gain. The input-output relation of the augmented system is

$$A ^ {*} y _ {a} (t) = \left(B ^ {*} + \frac {\rho}{r _ {0}} A ^ {*}\right) u (t - d _ {0}) + C ^ {*} e (t)$$

The minimum-variance control law for this system is given by

$$R _ {1} ^ {*} \left(B ^ {*} + \frac {\rho}{r _ {0}} A ^ {*}\right) u (t) = - S ^ {*} y _ {a} (t) \tag {4.38}$$

where $R_1^*$ and $S^*$ satisfy Eq. (4.16). It follows from Fig. 4.9 that

$$y _ {a} (t) = y (t) + \frac {\rho}{r _ {0}} q ^ {- d _ {0}} u (t)$$

Then Eq. (4.38) can be written as

$$\left(R _ {1} ^ {*} B ^ {*} + \frac {\rho}{r _ {0}} A ^ {*} R _ {1} ^ {*}\right) u (t) = - S ^ {*} \left(y (t) + \frac {\rho}{r _ {0}} q ^ {- d _ {0}} u (t)\right)$$

or

$$\left(R _ {1} ^ {*} B ^ {*} + \frac {\rho}{r _ {0}} \left(A ^ {*} R _ {1} ^ {*} + q ^ {- d _ {0}} S ^ {*}\right)\right) u (t) = - S ^ {*} y (t)$$

Equation (4.16) gives

$$\left(R _ {1} ^ {*} B ^ {*} + \frac {\rho}{r _ {0}} C ^ {*}\right) u (t) = - S ^ {*} y (t)$$

which is identical to Eq. (4.37). Notice that with the control law of Eq. (4.38) the canceled factor is not $B^{*}$ but $B^{*} + \rho A^{*}/r_{0}$ . This implies that problems can be expected when the system is nonminimum-phase and close to the stability boundary.

In the generalized minimum-variance control algorithm it is assumed that $C^{*}(q^{-1}) = 1$ . The algorithm can thus be obtained simply by adding a parallel path to the original system and applying an ordinary self-tuning regulator based on minimum-variance control to the augmented system. The control gain is adjusted simply by changing the parameter $\rho$ of the parallel path.

The preceding analysis shows that Algorithm 4.2 is very flexible. It can be used for many different types of specifications, not only for minimum-variance control. This is very important for the implementation of self-tuning regulators.

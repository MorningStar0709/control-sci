# Non-minimum-Phase (NMP) Systems

The case in which process zeros cannot be canceled will now be discussed. Consider the transformed process model Eq. (3.24), that is,

$$A _ {o} A _ {m} y (t) = B ^ {-} (R u (t) + S y (t))$$

where $\deg R = \deg S = \deg (A_0A_m) - \deg B^{-}$ . If we introduce

$$\mathcal {R} = B ^ {-} R \quad \text { and } \quad S = B ^ {-} S$$

the equation can be written as

$$y (t) = \frac {1}{A _ {o} A _ {m}} (\mathcal {R} u (t) + S y (t)) = \mathcal {R} ^ {*} u _ {f} \left(t - d _ {0}\right) + S ^ {*} y _ {f} \left(t - d _ {0}\right) \tag {3.33}$$

where $u_{f}$ and $y_{f}$ are the filtered inputs and outputs given by Eqs. (3.28). Notice that the polynomial R is not monic. The polynomials R and S have a common factor, which represents poorly damped zeros. This factor should be canceled before the control law is calculated. The following direct adaptive control algorithm is then obtained.

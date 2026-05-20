# 3.5 DIRECT SELF-TUNING REGULATORS

The design calculations in the indirect self-tuners may be time-consuming and poorly conditioned for some parameter values. It is possible to derive other algorithms in which the design calculations are simplified or even eliminated. The idea is to use the design equations to reparameterize the model in terms of the parameters of the controller. This reparameterization is also the key to understanding the relations between model-reference adaptive systems and self-tuning regulators.

Consider a process described by Eq. (3.1) with $v - 0$ , that is,

$$A y (t) = B u (t)$$

and let the desired response be given by Eq. (3.5):

$$A _ {m} y _ {m} (t) = B _ {m} u _ {c} (t)$$

The process model will now be reparameterized in terms of the controller parameters. To do this, consider the Diophantine equation (3.11),

$$A _ {o} A _ {m} = A R ^ {\prime} + B ^ {-} S$$

as an operator identity, and let it operate on $y(t)$ . This gives

$$A _ {o} A _ {m} y (t) = R ^ {\prime} A y (t) + B ^ {-} S y (t) = R ^ {\prime} B u (t) + B ^ {-} S y (t)$$

It follows from Eq. (3.10) that

$$R ^ {\prime} B = R ^ {\prime} B ^ {+} B ^ {-} = R B ^ {-}$$

Hence

$$A _ {o} A _ {m} y (t) = B ^ {-} \left(R u (t) + S y (t)\right) \tag {3.24}$$

Notice that this equation can be considered a process model that is parameterized in the coefficients of the polynomials $B^{-}$ , R, and S. If the parameters in the model given by Eq. (3.24) are estimated, the control law is thus obtained directly without any design calculations. Notice that the model Eq. (3.24) is nonlinear in the parameters because the right-hand side is multiplied by $B^{-}$ . The difficulties caused by this can be avoided in the special case of minimum-phase systems in which $B = b_{0}$ , which is a constant.

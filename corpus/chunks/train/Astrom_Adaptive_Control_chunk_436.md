# LEMMA 6.5 Averaging for sinusoidal input

Let $G_{v}$ and $G_{w}$ be stable transfer functions, and let v and w denote the steady-state responses of the corresponding systems to the input $u_{c} = u_{0}\sin\omega t$ . The mean value of the product uv is then given by

$$\operatorname{avg} (v w) = \frac {u _ {0} ^ {2}}{2} | G _ {v} (i \omega) | | G _ {w} (i \omega) | \cos (\arg G _ {v} (i \omega) - \arg G _ {w} (i \omega))= \frac {u _ {0} ^ {2}}{2} \operatorname{Re} \left(G _ {v} (i \omega) G _ {w} (- i \omega)\right)$$

Proof: The signals v and w have the amplitudes $|G_{v}(i\omega)$ , and $|G_{w}(i\omega)|$ ; their phase angles are $\arg G_{v}(i\omega)$ and $\arg G_{w}(i\omega)$ . Integrating over one period gives the result.

A true parameter equilibrium exists if the equation

$$G _ {e \nu} (\vartheta (\bar {\theta}), \omega) = 0$$

has a unique solution. To derive a necessary condition we consider the averaged equation

$$\frac {d \bar {\theta}}{d t} = \gamma \operatorname{Re} \left\{G _ {\varphi v} (\vartheta (\bar {\theta}), \omega) R _ {v} G _ {e v} ^ {T} (\vartheta (\bar {\theta}), - \omega) \right\} \tag {6.51}$$

where

$$\boldsymbol {R} _ {v} = \operatorname{avg} (\nu v ^ {T})$$

A necessary condition for Eq. (6.51) to have a unique parameter equilibrium is that v and $\bar{\theta}$ have equal dimension and that $R_{v}$ be of full rank. To have a unique parameter equilibrium for slow external driving signals, it is thus necessary that the number of estimated parameters be less than or equal to the number of external driving signals and that the external driving signals be persistently exciting. This result indicates that there may be some disadvantages to overparameterization, contrary to what is indicated in Theorem 6.7. The local stability of the equilibrium $\bar{\theta}^{0}$ is given by the linearized equation

$$\frac {d x}{d t} = A x$$

where $x$ denotes the deviation from the equilibrium $\bar{\theta} - \bar{\theta}^0$ and

$$A = G _ {\varphi \nu} \left(v (\bar {\theta} ^ {0}), \omega\right) R _ {\nu} \frac {\partial}{\partial \theta} G _ {e \nu} ^ {T} \left(v (\bar {\theta} ^ {0}), \omega\right)$$

The preceding equations can be applied to slow or constant perturbations by setting $\omega = 0$ , provided that the assumptions of averaging are fulfilled.

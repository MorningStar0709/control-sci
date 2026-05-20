where $K _ { T } = \hat { \omega } _ { L O S } / \omega _ { L O S }$ in the steady state and $\omega _ { L O S }$ is a unit step input. (Compare this equation with (4.32)). Assuming that $\Lambda = 4 8 0 [ ( \mathrm { f t / s e c } ^ { 2 } ) / ( \mathrm { d e g / s e c } ) ]$ , $\lvert d R _ { M T } / d t \rvert = 4 0 0 0 \mathrm { f t / s e c }$ , $K _ { T } \cong 1$ , and $( \gamma - \lambda ) = 0$ , then $N ^ { \prime } \cong 6 . 8$ . A possible closed loop for this angle-tracking system is shown in Figure 4.20.

A few final remarks about the navigation constant N are in order. As mentioned earlier, the proportional navigation constant appears in the literature under different form(s) and/or nomenclature. Specifically, let us examine three versions for this constant as given in the literature.

(1) In [12], the navigation constant for the “biased proportional navigation” case is given as

$$N > 1 + [ \rho / \sqrt {1 - (\rho + \beta) ^ {2}} ],$$

where $\rho = v _ { t } / v _ { m }$ (where it is assumed that $v _ { m } > v _ { t } )$ . From geometrical considerations between pursuer and evader (i.e., target), we have

$$\left| \rho \sin \theta_ {t} (t) - \sin \theta_ {m} (t) \right| < \beta , \quad t _ {0} \leq t \leq t _ {1},| \sin \theta_ {m} (t _ {o}) | < \pi / 2,$$

with

$$\sin \theta_ {m} (t) = \gamma_ {t} - \lambda ,\sin \theta_ {m} (t) = \gamma_ {m} - \lambda ,$$

where

γm, γt = interceptor and target body attitude angles, respectively,

λ = line of sight.

(2) In [23], the navigation constant is given in terms of the effective navigation constant $N ^ { \prime }$ as

$$N = N ^ {\prime} (V _ {L i} / V _ {m} \cos \phi_ {c}),$$

where

$$V _ {L i} = \text { initial value of the relative velocity along the LOS },\phi_ {i} = \phi_ {c} + \Delta \phi_ {i},$$

where $\phi _ { c }$ is the perturbation heading angle of the pursuer and $\Delta \phi _ { i }$ is the initial missile heading error.

(3) In [19], the navigation constant is given as

$$N = 3 T ^ {3} / (T ^ {3} - t _ {g o} ^ {3}),$$

where T is the intercept time and $t _ { g o } = T - t$ . Here we note that the navigation constant N of proportional navigation is such that the maximum value of the commanded acceleration in proportional navigation is the same as the maximum acceleration commanded by the optimal guidance law (see also Section 4.8). Compare this navigation constant with the effective navigation constant given in [3],

$$K = 3 / [ 1 - (C _ {e} / C _ {p}) ],$$

where $C _ { e }$ and $C _ { p }$ are constants relating the energies of the evader and pursuer, respectively.

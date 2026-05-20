where $y _ { d } = y _ { T } - y _ { M }$ is terminal miss distance at the intercept time T , $\gamma ( \gamma \geq 0 )$ is the weighting on the control effort, and $\boldsymbol { u } _ { c } ( t )$ is the commanded control. That is, this equation states that the optimal control consists in minimizing the terminal meansquare miss distance plus the weighted integral-square missile acceleration normal to the line of sight (LOS). In general, the missile commanded acceleration normal to the LOS is constrained by $| u | \leq u _ { \mathrm { m a x } }$ .

In order to illustrate the above theory, consider the following simple two-dimensional intercept case, illustrated in Figure 4.33. Let ${ \mathbf { R } } _ { M } , \ { \mathbf { v } } _ { M }$ , and $\mathbf { a } _ { M }$ be the interceptor missile’s position, velocity, and acceleration vectors relative to an inertial reference frame. Furthermore, let ${ \bf R } _ { T } , \mathbf { v } _ { T }$ , and $\mathbf { a } _ { T }$ be the target’s corresponding position, velocity, and acceleration vectors relative also to the inertial reference frame. Assume now that the time-to-go $t _ { g o }$ is known and can be computed separately (e.g., as an initial guess, $t _ { g o } = R _ { M T } / v _ { c } .$ , where $v _ { c }$ is the missile’s closing velocity). We will assume $t _ { g o }$ to be independent of the future control, that is, the missile’s corrective lateral acceleration. Moreover, it will be assumed that gravity compensation is used in the missile guidance law to negate the effect of gravity on the missile performance. From Figure 4.33 the closing velocity $v _ { c }$ is defined as the relative velocity measured along the LOS. Mathematically, the closing velocity is given by the expression

$$v _ {c} = v _ {M} \cos (\theta_ {l} + \theta_ {h e} - \lambda) + v _ {T} \cos (\theta_ {a} + \lambda), \tag {4.146}$$

![](image/87dd253729774e082fb6e9a4f93b422ea4e545e263fce034b75a0da3a52a8d53.jpg)

<details>
<summary>text_image</summary>

Y
Vt
Aty
A1
T
A1x
LOS Rmt
a1mn
a1ma
vm
λ
M
θl
rt
rm
ym
θl
x0
Original LOS (inertial reference)
X
yd
yt
θa
</details>

Fig. 4.33. Intercept geometry.

where

$$
\begin{array}{c} \theta_ {l} = \text { the   missile   lead   angle   (note:   the   instantaneous } \\ \text { lead   angle   is } (\theta_ {l} - \lambda)), \end{array}
\theta_ {h e} = \text { missile heading error },\theta_ {a} = \text { target aspect angle },\lambda = \text { line of sight } (L O S),v _ {M} = \text { missile velocity },v _ {T} = \text { target velocity }.
$$

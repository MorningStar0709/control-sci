Figure 4.11 shows the geometry from which the equations representing proportional navigation can be derived. In the derivation of the proportional navigation equations, it will be assumed that the missile speed and target speed remain constant during the time of flight of the missile; this is normally a good assumption.

From the engagement geometry of Figure 4.11, we note that the range between the missile and the target has a value R, and the line of sight has rotated through an angle λ from the initial value. The rate of rotation of the line of sight at any time is given by the difference in the normal components of velocity of the target and missile, divided by the range. This can be expressed by the equation

$$R \left(\frac {d \lambda}{d t}\right) = v _ {t} \sin (\gamma_ {t} - \lambda) - v _ {m} \sin (\gamma_ {m} - \lambda), \tag {4.25a}$$

while the velocity component along the line of sight is given by the equation

$$\frac {d R}{d t} = v _ {t} \cos (\gamma_ {t} - \lambda) - v _ {m} \cos (\gamma_ {m} - \lambda), \tag {4.25b}$$

![](image/61a5b97ed36f0395582409600523c6d3108ae1d042202abc8bcf155cb0002e03.jpg)

<details>
<summary>text_image</summary>

Target
direction
Impact
point
v_t
γ_t
λ
a_t
R
v_m
a_m
Interceptor
γ_m
λ
Inertial reference
</details>

Fig. 4.11. Geometry for derivation of proportional navigation.

where

$$
\begin{array}{l} R = \text { range   between   missile   and   target }, \\ v _ {m} = \text {   interceptor   missile   velocity,   } \\ v _ {t} = \text { velocity   of   the   target }, \\ \lambda = \text { line - of - sight   (LOS)   angle }, \\ \begin{array}{l} \gamma_ {m} = \text { missile   flight   path   (or   heading)   angle }, \\ \quad \text { that   is,   angle   between   the   missile   velocity } \\ \quad \text { vector   and   inertial   reference }, \end{array} \\ \gamma_ {t} = \text {   target   flight   path   angle.   } \\ \end{array}
$$

The proportional navigation guidance law states that the rate of change of the missile heading $( \gamma _ { m } )$ is directly proportional to the rate of change of the line-of-sight angle (λ) from the missile to the target. Therefore, the basic differential equation for this case is given by

$$\frac {d \gamma_ {m}}{d t} = N \left(\frac {d \lambda}{d t}\right), \tag {4.26}$$

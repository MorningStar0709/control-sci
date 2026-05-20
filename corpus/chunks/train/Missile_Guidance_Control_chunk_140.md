Furthermore, the dependency of $\theta _ { r }$ on $\theta _ { m }$ couples body motion into the boresight error signal, thus forming what is commonly called the parasitic attitude loop (for a discussion of the parasitic attitude loop see Section 3.5). This loop can drastically alter missile response characteristics and in turn increase the miss distance. This is particularly true at high altitudes, where the missile body motion tends to be greatest. The aberration (or refraction) angle error is normally a nonlinear function of the following factors: (a) the angle between the missile center line and the line of sight to the target (also known as the look angle, which is defined as $\left( \lambda - \theta _ { m } \right) )$ ; (b) the radome thickness distribution; (c) material; (d) radome shape; (e) manufacturing tolerances; (f) temperature; and (g) erosion of the surface during flight. In addition, the nonlinearity arises from such optical and electrical properties as frequency, standing waves inside the radome, and polarization of the received signal. Consequently, an accurate model may require a nonlinear, time-varying statistical characterization of the radome. From the above discussion, it can be said that the radome error magnitude can neither be precisely measured nor predicted. However, since these characteristics tend to vary over rather wide limits depending on the particular application and missile configuration, a constant refraction error slope model is used to capture the important body-coupling effect.

From the above discussion, we note that radome aberration error is one of the errors contributing to the overall miss distance of a radar-guided homing missile. Figure 3.26 illustrates the aberration angle as a function of look angle [3].

The derivation of the radome model can be obtained as follows. Let λ be the true LOS and $\lambda _ { m }$ the measured LOS. Then,

$$\lambda_ {m} = \lambda + \theta_ {r}, \tag {3.74a}$$

![](image/434cad61a0fe365f659e4d2c4b1879d7918b5bf984af779713e018f8fe87ce65.jpg)

<details>
<summary>text_image</summary>

Aberration
angle
θr
θo bias angle
Look angle
(λ - θm)
Error
slope
R
</details>

Fig. 3.26. Aberration angle error as a function of look angle.

where $\theta _ { r } = f ( \theta _ { h } )$ . Taking the derivative of (3.74a), we have

$$\frac {d \lambda_ {m}}{d t} = \frac {d \lambda}{d t} + \frac {d \theta_ {r}}{d t}. \tag {3.74b}$$

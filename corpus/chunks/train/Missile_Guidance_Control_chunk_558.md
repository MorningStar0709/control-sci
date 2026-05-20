# (4.1.1) Formulation (I )

VR = required missile velocity,

Vr = radial component of velocity $= d r _ { v } / d t$ ,

Vθ = tangential component of velocity

![](image/4e554d6fdbc45e99ac5c6f9546abec2cb17e6b8c9d4978309922055a1801a079.jpg)

<details>
<summary>text_image</summary>

V_R
V_R
γ
l_r
l_θ
l_θ
r_v
r_t
θ
0
T
</details>

Required velocity geometry.

From the above figure, we obtain

$$\mathbf {V} _ {R} = V _ {r} \mathbf {1} _ {r} + V _ {\theta} \mathbf {1} _ {\theta},$$

and the unit vectors $\mathbf { 1 } _ { r } , \mathbf { 1 } _ { \theta }$ , and ${ \bf 1 } _ { n }$ are the radial, tangential, and normal unit vectors, respectively, and are given by the expressions

$$\mathbf {1} _ {r} = \mathbf {r} _ {v} / | \mathbf {r} _ {v} | = (X / r _ {v}) \mathbf {1} _ {x} + (Y / r _ {v}) \mathbf {1} _ {y} + (Z / r _ {v}) \mathbf {1} _ {z},\mathbf {1} _ {\theta} = \mathbf {1} _ {n} \times \mathbf {1} _ {r},\mathbf {1} _ {n} = (\mathbf {r} _ {v} \times \mathbf {r} _ {t}) / | \mathbf {r} _ {v} \times \mathbf {r} _ {t} |.$$

Therefore,

$$\mathbf {V} _ {R} = V _ {r} \mathbf {1} _ {r} + V _ {\theta} \mathbf {1} _ {\theta} = V _ {r} (\mathbf {r} _ {v} / r _ {v}) + \{[ V _ {\theta} (\mathbf {r} _ {v} \times \mathbf {r} _ {t}) \times \mathbf {r} _ {v} ] / [ | \mathbf {r} _ {v} | \cdot | \mathbf {r} _ {v} \times \mathbf {r} _ {t} | ] \}, \tag {15}$$

where

$$V _ {R} ^ {2} = 2 \mu \left[ (1 / r _ {v}) - \left(\frac {1}{2 a}\right) \right] - V _ {\theta} ^ {2}, \tag {16}V _ {\theta} ^ {2} = h ^ {2} / r _ {v} ^ {2} = (\mu a / r _ {v} ^ {2}) (1 - e ^ {2}). \tag {17}$$

The quantity $( 1 - e ^ { 2 } )$ is given as

$$1 - e ^ {2} = \left[ 4 \left(s - r _ {v}\right) \left(s - r _ {t}\right) / c ^ {2} \right] \sin^ {2} ((\alpha - \beta) / 2) \tag {18}$$

if

$$t _ {f f} > \left(\sqrt {a ^ {3} / \mu}\right) [ \pi - (\beta - \sin \beta) ],\alpha = \pi ,a = s / 2,$$

or

$$1 - e ^ {2} = [ 4 (s - r _ {v}) (s - r _ {t}) / c ^ {2} ] \sin^ {2} ((\alpha + \beta) / 2) \tag {19}$$

if

$$t _ {f f} < \left(\sqrt {a ^ {3} / \mu}\right) [ \pi - (\beta - \sin \beta) ],\alpha = \pi ,a = s / 2,$$

and

$$s = \frac {1}{2} (r _ {v} + r _ {t} + c), \tag {20}c = \left| \mathbf {r} _ {t} - \mathbf {r} _ {v} \right|, \tag {21}\sin (\alpha / 2) = \sqrt {s / 2 a} = ((r _ {v} + r _ {t} + c) / 4 a) ^ {1 / 2}, \quad \alpha \leq \pi , \tag {22}\sin (\beta / 2) = \sqrt {(s - c) / 2 a} = ((r _ {v} + r _ {t} - c) / 4 a) ^ {1 / 2}, \quad \beta \leq \alpha \leq \pi . \tag {23}$$

The semimajor axis a is determined by the constraint of a required time-of-flight $( T - t _ { o } )$ and is determined by the methods that will be presented in Section (5).

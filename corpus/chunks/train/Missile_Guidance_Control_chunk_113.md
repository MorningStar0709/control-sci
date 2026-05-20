Example 2. In this example we will apply the most important results of Sections 3.1 and 3.2. Consider an air-to-air missile represented in Figure 3.14.

The problem will be formulated as follows:

Missile Dynamics

$$\frac {d u}{d t} = \left\{\left[ - C (\alpha , M, h, t) + T (t) \right] / m (t) \right\} - q w, \tag {1}\frac {d w}{t} = \left\{- N \left(\alpha , M, \delta_ {z}\right) / m (t) \right\} + q u, \tag {2}\frac {d q}{d t} = \left\{\left[ M _ {y} (\alpha , M, \delta_ {z}, X _ {c g} - X _ {c p}, t) - q \left(\frac {d I _ {y} (t)}{d t}\right) \right] / I _ {y} (t), \right. \tag {3}$$

where

$$u = \text { longitudinal velocity component },C = \text { axial force },M = \text { Mach number } = V _ {m} / V _ {s},V _ {m} = \text { missile speed },V _ {s} = \text { speed of sound },\alpha = \text { angle of attack } = \tan^ {- 1} (u / w),$$

![](image/637ac216a53ca6db6d0defaf83dd6329e6d591f90f2551e8c597a9ca8f2876f2.jpg)

<details>
<summary>text_image</summary>

Airframe axes
w
r
z
v
p
u
x
q
y
Y
w
Z
cg
α
T
δz
Xcg
Xcp
Vm
</details>

Fig. 3.14. Representation of the missile in the local reference frame XYZ.

h = flight altitude,

t = time,

m = mass of missile,

w = normal velocity component,

q = pitch rate,

T = rocket motor thrust,

N = normal force (yawing moment),

δz = thrust deflection (or tail fin) angle,

M = pitching moment,

$X _ { c g } , X _ { c p }$ = center of gravity and center of aerodynamic pressure, respectively,

$I _ { y }$ = missile’s moment of inertia about the Y -axis.

The aerodynamic forces with respect to the local reference frame XY Z are as follows:

Axial Force

$$C = \tilde {q} C _ {c} (\alpha , M, h, t), \tag {4}C _ {c} = F _ {f r} (M) \{[ (h - 6. 0 9 6) / 3. 0 4 8 ] + F _ {a f c} (\alpha , M) + F _ {b} (M, t) [ 1 - (A _ {e} / A _ {b}) ]. \tag {5}$$

Normal Force

$$N = \tilde {q} C _ {n} (\alpha , M, \delta_ {z}), \tag {6}C _ {n} = F _ {n f c} (\alpha , M) \alpha - F _ {t n f} (M) \delta_ {z}, \tag {7}$$

where

$F _ { n f c }$ = normal force coefficient,

$F _ { t n f }$ = trim normal force effectiveness,

$F _ { b }$ = base drag coefficient,

$F _ { f r }$ = friction drag coefficient,

$F _ { a f c }$ = axial force coefficient.

Aerodynamic Couple

$$M _ {y} = \tilde {q} L _ {r} C _ {m} (\alpha , M, \delta_ {z}, q, t), \tag {8}C _ {m} = C _ {m a} \alpha + C _ {m \delta z} \delta_ {z} + C _ {m q} q, \tag {9}C _ {m \alpha} = F _ {n f c} (\alpha , M) \left\{\left[ X _ {c g} (t) - X _ {c p} (\alpha , M) \right] / L _ {r} \right\}, \tag {10}C _ {m \delta z} = F _ {t p m} (M) - F _ {t n f} (M) \{[ X _ {c g} (t) - X _ {c g b} ] / L _ {r} \}, \tag {11}C _ {m q} = - F _ {p d m} (M) ] 5 0 0 L _ {r} / V _ {m}, \tag {12}$$

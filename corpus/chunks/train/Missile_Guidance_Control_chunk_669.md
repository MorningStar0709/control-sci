$$\frac {d r}{d t} = \left[ \left(F _ {v} - A _ {e} P\right) k _ {\theta} \partial \psi \left(L _ {j} - L _ {g}\right) \right] / I _ {y y} \tag {6.276}$$

with

$$\partial \psi = r \delta_ {\dot {\psi}} - \delta_ {\psi} \bar {\psi} _ {c}, \tag {6.277}$$

where the symbols have been defined above.

An Example In this example we will derive the differential equations used to generate the orbital motion of a space vehicle (e.g., a missile), including gravity and drag effects.

Coordinate Systems The computations are performed in an inertial rectangular coordinate system (x, y, z), with origin at the geocenter, with the z-axis along the Earth’s axis in a northerly direction. The Greenwich meridian is assumed to intersect the positive x-axis at time zero (i.e., the starting time of the orbit). A spherical coordinate system $( \mathbf { r } , \theta , \phi )$ will also be employed frequently (see the illustration below).

![](image/42c6d3e55eb491068c376bf2190195c987347dacee3acf6ba1037e694db73444.jpg)

<details>
<summary>text_image</summary>

z
I_r
I_φ
I_θ
r
θ
I_z
I_y
y
I_x
φ
x
</details>

Rectangular and spherical coordinate systems.

The angle $\phi$ is measured counterclockwise from the positive x-axis, as seen from the North Pole. Associated with the angles θ and $\phi$ is a rectangular system with axes in the $\operatorname { r } , \theta .$ , and φ directions. The transformation matrix from the rectangular (r, θ , φ) system to the (x, y, z) system is [11]

$$
T _ {S R} = \left[ \begin{array}{c c c} \sin \theta \cos \phi & \cos \theta \cos \phi & - \sin \phi \\ \sin \theta \sin \phi & \cos \theta \sin \phi & \cos \phi \\ \cos \theta & - \sin \phi & 0 \end{array} \right] \tag {1}
$$

Orbit Differential Equations The differential equations satisfied by the orbit are

$${\frac {d x}{d t}} = u,\frac {d y}{d t} = v,\frac {d z}{d t} = w,\frac {d u}{d t} = g _ {x} + D _ {x}, \tag {2}\frac {d v}{d t} = g _ {y} + D _ {y},\frac {d w}{d t} = g _ {z} + D _ {z},$$

or in vector form,

$$\frac {d x}{d t} = \mathbf {v}, \tag {3a}\frac {d \mathbf {v}}{d t} = \mathbf {g} + \mathbf {D}, \tag {3b}$$

where g is the gravitational acceleration and D is the drag acceleration.

Gravitational Forces The components of gravitational acceleration are most conveniently evaluated in the $( \boldsymbol { \mathbf { r } } , \theta , \phi )$ system and later transformed. Therefore, we use the components of g as follows:

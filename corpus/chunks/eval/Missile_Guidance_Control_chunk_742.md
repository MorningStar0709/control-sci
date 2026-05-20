# 7.3.1 Navigation Coordinate System

The coordinate systems used for navigation computations are illustrated in Figure 7.9. The cruise missile’s navigation coordinate system, designated $( x , y , z )$ , is obtained from an Earth-centered, Earth-fixed coordinate system (X, Y, Z) by successive rotations as follows [8]: (a) a positive rotation (λ-longitude) about the X-axis, (b) a positive rotation (φ-latitude) about the rotated Y -axis, (c) a rotation by $1 8 0 ^ { \circ }$ about the rotated X-axis, and (d) a positive rotation (α-wander angle) about the z-axis. The X-axis is defined by the polar axis of the Earth, the Z-axis is formed by the intersection of the plane containing the Greenwich Meridian and the equatorial plane of the Earth (positive Z intersects the Greenwich Meridian), and the Y -axis completes a right-handed coordinate system.

![](image/5dbddd3946df6c05c81a2c5b63feb2f137e33ca3ed0eb300c848e88105cc3a5d.jpg)

<details>
<summary>text_image</summary>

X (Polar axis)
Ω
Greenwich
Meridian
x
y
z
φ
λ
Equator
Y
Z
φ = Latitude
λ = Longitude
α = Wander angle
ψ = Heading
V = Velocity
</details>

Fig. 7.9. Navigation coordinate system.

The transformation from the (X, Y, Z) system to the $( x , y , z )$ system is obtained as follows:

$$
\begin{array}{l} \left[ \begin{array}{c} x \\ y \\ z \end{array} \right] = \left[ \begin{array}{c c c} C _ {x x} & C _ {y x} & C _ {z x} \\ C _ {x y} & C _ {y y} & C _ {z y} \\ C _ {x z} & C _ {y z} & C _ {z z} \end{array} \right] \left[ \begin{array}{c} X \\ Y \\ Z \end{array} \right] \\ = \left[ \begin{array}{c c c} \cos \alpha \cos \phi & \cos \alpha \sin \phi \sin \lambda - \sin \alpha \cos \lambda & - \cos \alpha \sin \phi \cos \lambda - \sin \alpha \sin \lambda \\ - \sin \alpha \cos \phi & - \sin \alpha \sin \phi \sin \lambda - \cos \alpha \cos \lambda & \sin \alpha \sin \phi \cos \lambda - \cos \alpha \sin \lambda \\ - \sin \phi & \cos \phi \sin \lambda & - \cos \phi \cos \lambda \end{array} \right] \\ \left[ \begin{array}{l} X \\ Y \\ Z \end{array} \right] \tag {7.7} \\ \end{array}
$$

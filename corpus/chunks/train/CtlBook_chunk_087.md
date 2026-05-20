# 3.2.1 Torque

Torque (also called moment) is a vector quantity relating a force and an associated moment arm through which the force acts to rotate a body around an axis. The simplest case is a force which is perpendicular to both the axis of rotation and a radius connecting the axis and the point through which the force is acting on the rigid body (Figure 3.1, Left). In this case, the magnitude of the torque is

$$| \tau | = | r | | F |$$

and the full magnitude and direction of the torque vector will be obtained by the right hand rule

$$\tau = r \times F$$

(where × indicates the vector cross product).

If the force vector is not applied at a right angle (Figure 3.1, Right), it must be resolved into perpendicular and radial components, $F _ { p } , \bar { F } _ { r } ^ { \phantom { \dagger } } ,$ , and then the torque magnitude is

$$| \tau | = | r | | F _ {p} |$$

the full torque vector can still be obtained by the vector cross product above. When the axis of rotation is xed, for example by a shaft mounted in bearings, then only the component of the torque vector which is parallel to the axis causes rotation about the axis.

In most of the problems we will study however, we will assume that a torque value is a known or measured quantity and not worry about the radius or moment arm. In a very common control system application, a DC electric motor is applied to a shaft and the torque is simply proportional to the current

$$\tau (t) = K _ {m} i (t)$$

![](image/9a79fa38c758309e159dbb4611cfae25f41b55b1bac8b6aee06e398a2a328313.jpg)

<details>
<summary>text_image</summary>

AXIS
(INTO
paper)
r
F
</details>

![](image/401240b3cdb9c3d10935491f7d851f0d3bf3367aa5458f8a02ee32585a412168.jpg)

Figure 3.1: An applied force F generates a torque if it acts through a point having a radius, r from the axis of rotation. Left: force is applied perpendicular to the moment arm. Right: force is appled in a general direction. (see text).

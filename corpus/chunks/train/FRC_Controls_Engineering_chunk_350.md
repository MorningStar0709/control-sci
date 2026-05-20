# 11.4 Curvilinear motion

Curvilinear motion describes the motion of an object along a fixed curve. This motion has both linear and angular components. For derivations involving curvilinear motion, we’ll assume positive $\bar { x ( i ) }$ is forward, positive $y ( \hat { j } )$ is to the left, positive $z \left( { \hat { k } } \right)$ is up, and the robot is facing in the x direction. This axes convention is known as North-West-Up (NWU), and is shown in figure 11.1.

![](image/56d34126e8d0eef0e653fe40190debe8cac0fc096267ce3f7efb67f7d9e1435a.jpg)

<details>
<summary>text_image</summary>

+x
+y
</details>

Figure 11.1: 2D projection of North-West-Up (NWU) axes convention. The positive z-axis is pointed out of the page toward the reader.

The main equation we’ll need is the following.

$$\vec {v} _ {B} = \vec {v} _ {A} + \omega_ {A} \times \vec {r} _ {B | A}$$

where ${ \vec { v } } _ { B }$ is the velocity vector at point B, ${ \vec { v } } _ { A }$ is the velocity vector at point A, $\omega _ { A }$ is the angular velocity vector at point A, and ${ \vec { r } } _ { B \mid A }$ is the distance vector from point A to point B (also described as the “distance to B relative to A”).

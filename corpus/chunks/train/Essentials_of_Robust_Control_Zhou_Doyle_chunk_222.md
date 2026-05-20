# 8.6 Classical Control for MIMO Systems

In this section, we show through an example that the classical control theory may not be reliable when it is applied to MIMO system design.

Consider a symmetric spinning body with torque inputs, $T _ { 1 }$ and $T _ { 2 }$ , along two orthogonal transverse axes, x and $y ,$ as shown in Figure 8.17. Assume that the angular velocity of the spinning body with respect to the z axis is constant, Ω. Assume further that the inertias of the spinning body with respect to the $x , y ,$ and z axes are $I _ { 1 }$ , $I _ { 2 } = I _ { 1 }$ , and $I _ { 3 } ,$ respectively. Denote by $\omega _ { 1 }$ and $\omega _ { 2 }$ the angular velocities of the body with respect to the x and y axes, respectively. Then the Euler’s equation of the spinning

body is given by

$$I _ {1} \dot {\omega} _ {1} - \omega_ {2} \Omega (I _ {1} - I _ {3}) = T _ {1}I _ {1} \dot {\omega} _ {2} - \omega_ {1} \Omega (I _ {3} - I _ {1}) = T _ {2}$$

![](image/7c22b77de287632b1614156fd30a2dc9c67726ca64400d5daf40532694f24d2a.jpg)

<details>
<summary>text_image</summary>

z
x
y
</details>

Figure 8.17: Spinning body

Define

$$
\left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] := \left[ \begin{array}{c} T _ {1} / I _ {1} \\ T _ {2} / I _ {1} \end{array} \right], a := (1 - I _ {3} / I _ {1}) \Omega .
$$

Then the system dynamical equations can be written as

$$
{\left[ \begin{array}{l} \dot {\omega} _ {1} \\ \dot {\omega} _ {2} \end{array} \right]} = {\left[ \begin{array}{l l} 0 & a \\ - a & 0 \end{array} \right]} {\left[ \begin{array}{l} \omega_ {1} \\ \omega_ {2} \end{array} \right]} + {\left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right]}
$$

Now suppose that the angular rates $\omega _ { 1 }$ and $\omega _ { 2 }$ are measured in scaled and rotated coordinates:

$$
\left[ \begin{array}{l} y _ {1} \\ y _ {2} \end{array} \right] = \frac {1}{\cos \theta} \left[ \begin{array}{c c} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right] \left[ \begin{array}{l} \omega_ {1} \\ \omega_ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & a \\ - a & 1 \end{array} \right] \left[ \begin{array}{l} \omega_ {1} \\ \omega_ {2} \end{array} \right]
$$

where tan $\theta : = a .$ . (There is no specific physical meaning for the measurements of $y _ { 1 }$ and $y _ { 2 }$ but they are assumed here only for the convenience of discussion.) Then the transfer matrix for the spinning body can be computed as

$$Y (s) = P (s) U (s)$$

with

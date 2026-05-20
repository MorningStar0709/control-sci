Referring to Figure 2.1, we will denote the Earth-fixed coordinate system by $( X _ { e } ,$ , $Y _ { e } , Z _ { e } )$ . In this right-handed coordinate system, the $X _ { e } - Y _ { e }$ lie in the horizontal plane, and the $Z _ { e } \mathrm { - a x i s }$ points down vertically in the direction of gravity. (Note that the position of the missile’s center of gravity at any instant of time is given in this coordinate system). The second coordinate system, the body axis system, denoted by $( X _ { b } , Y _ { b } , Z _ { b } )$ , is fixed with respect to the missile, and thus moves with the missile. This is the missile body coordinate system. The positive $X _ { b } \mathrm { - a x i s }$ coincides with the missile’s center line (or longitudinal axis) or forward direction. The positive $Y _ { b } \mathrm { - a x i s }$ is to the right of the $X _ { b } \mathrm { - a x i s }$ in the horizontal plane and is designated as the pitch axis. The positive $Z _ { b } \mathrm { - a x i s }$ is the yaw axis and points down. This coordinate system is similar to the NED system. The Euler angles $( \psi , \theta , \phi )$ are commonly used to define the missile’s attitude with respect to the Earth-fixed axes. These Euler angles are illustrated in Figure 2.1, whereby the order of rotation of the missile axes is yaw, pitch, and roll. This figure also illustrates the angular rates of the Euler angles. The transformation $C _ { e } ^ { b }$ from the Earth-fixed axes coordinate system to the missile body-axes frame is achieved by a yaw, pitch, and roll rotation about the longitudinal, lateral, and normal (i.e., vertical) axes, respectively. The resultant transformation matrix $C _ { e } ^ { b }$ is [2], [7]

![](image/cca68d4e24ebdba2dec5aa666120b68d2f400ffde9cd8b046c2fc9a140f0efbe.jpg)  
Fig. 2.1. Orientation of the missile axes with respect to the Earth-fixed axes.

![](image/b04fbb1704bc479e7dc0dd3d5c80e3d572d45c0cd915ffc433a88457af549fc1.jpg)

<details>
<summary>text_image</summary>

Inertial axes (X_i, Y_i, Z_i)
Z_i
i
Y_i
X_i
b
X_b
Body axes (X_b, Y_b, Z_b)
[Z_b]
Z_o, Z_e
[Z_i]_ib
[i]_ie
[θ]_eb
ω_e·t
e
Earth axes (X_e, Y_e, Z_e)
Y_e
Y_o
ω_e·t
X_o
X_e
Equatorial plane
</details>

Fig. 2.2. Representation of the inertial coordinate system (inertial, Earth, and body coordinate systems).

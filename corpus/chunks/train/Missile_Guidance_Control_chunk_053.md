$$F _ {x} = \frac {d (m u)}{d t}, F _ {y} = \frac {d (m v)}{d t}, F _ {z} = \frac {d (m w)}{d t}, \tag {2.19}$$

where $F _ { x } , F _ { y } , F _ { z }$ and u, v, w are the components of the force and velocity along the missile’s $X _ { b } , Y _ { b }$ , and $Z _ { b }$ axes, respectively. Normally, these force components are composed of contributions due to (1) aerodynamic, (2) propulsive, and (3) gravitational forces acting on the missile. In a similar manner, the moment equations can be expressed as follows [6]:

$$L = \frac {d H _ {x}}{d t}, \quad M = \frac {d H _ {y}}{d t}, \quad N = \frac {d H _ {z}}{d t}, \tag {2.20}$$

where L, M, N are the roll moment, pitch moment, and yaw moment, respectively, and $H _ { x } , H _ { y } , H _ { z }$ are the components of the moment of momentum along the body X, Y , and Z axes, respectively.

At this point, let us summarize the various forces, moments, and axes used in developing the missile 6-DOF equations of motion.

Force:

$$\mathbf {F} = F _ {x} \mathbf {i} + F _ {y} \mathbf {j} + F _ {z} \mathbf {k},$$

where $F _ { x } , F _ { y } , F _ { z }$ are the $( x , y , z )$ components of the force.

Velocity:

$$\mathbf {V} = u \mathbf {i} + v \mathbf {j} + w \mathbf {k},$$

where u, v, w are the velocity components along the $( x , y , z )$ axes, respectively.

Moment of External Forces:

$$\sum \Delta \mathbf {M} = L \mathbf {i} + M \mathbf {j} + N \mathbf {k},$$

where L is the rolling moment, M is the pitching moment, and N is the yawing moment.

Angular Momentum:

$$\mathbf {H} = H _ {x} \mathbf {i} + H _ {y} \mathbf {j} + H _ {z} \mathbf {k},$$

where $H _ { x } , H _ { y } , H _ { z }$ are the components of the angular momentum along the x, y, z axes, respectively.

Angular Velocity:

$$\boldsymbol {\omega} = \omega_ {x} \mathbf {i} + \omega_ {y} \mathbf {j} + \omega_ {z} \mathbf {k} = P \mathbf {i} + Q \mathbf {j} + R \mathbf {k},$$

where P is the roll rate, Q is the pitch rate, and R is the yaw rate. (i = unit vector along the x-axis, j = unit vector along the y-axis, and k = unit vector along the z-axis).

We now wish to develop an expression for the time rate of change of the velocity vector with respect to the Earth. Before we do this, we note that in general, a vector A can be transformed from a fixed (e.g., inertial) to a rotating coordinate system by the relation [6], [7]

$$\left(\frac {d \mathbf {A}}{d t}\right) _ {\text { fixed } (X ^ {\prime}, Y ^ {\prime}, Z ^ {\prime})} = \left[ \frac {d \mathbf {A}}{d t} \right] _ {\text { rot. } (X, Y, Z)} + \boldsymbol {\omega} \times \mathbf {A}, \tag {2.21a}$$

# 8.6.1 Model

Holonomic drivetrains have three degrees of freedom: x, y, and heading. They are described by the following kinematics.

$$
\left[ \begin{array}{c} \dot {x} \\ y \\ \theta \end{array} \right] = \left[ \begin{array}{c c c} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c} v _ {x, c h a s s i s} \\ v _ {y, c h a s s i s} \\ \omega_ {c h a s s i s} \end{array} \right]
$$

where $v _ { x , c h a s s i s }$ is the velocity ahead in the chassis frame, $v _ { y , c h a s s i s }$ is the velocity to the left in the chassis frame, and $\omega _ { c h a s s i s }$ is the angular velocity in the chassis frame. This can be written in state-space notation as

$$
{\left[ \begin{array}{l} \dot {x} \\ y \\ \theta \end{array} \right]} = {\left[ \begin{array}{l l l} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right]} {\left[ \begin{array}{l} x \\ y \\ \theta \end{array} \right]} + {\left[ \begin{array}{l l l} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right]} {\left[ \begin{array}{l} v _ {x, c h a s s i s} \\ v _ {y, c h a s s i s} \\ \omega_ {c h a s s i s} \end{array} \right]}
$$

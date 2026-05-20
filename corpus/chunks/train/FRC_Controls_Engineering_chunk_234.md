# 8.6.2 Control

This control-affine model is fully actuated but nonlinear in the chassis frame. However, we can apply linear control theory to the error dynamics in the global frame instead. Note how equation (8.6)’s state vector contains the global pose and its input vector contains the global linear and angular velocities.

$$
\left[ \begin{array}{l} \dot {x} \\ y \\ \theta \end{array} \right] = \left[ \begin{array}{l l l} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x \\ y \\ \theta \end{array} \right] + \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{l} v _ {x, g l o b a l} \\ v _ {y, g l o b a l} \\ \omega_ {g l o b a l} \end{array} \right] \tag {8.6}

\text { where } \left[ \begin{array}{c} v _ {x, g l o b a l} \\ v _ {y, g l o b a l} \\ \omega_ {g l o b a l} \end{array} \right] = \left[ \begin{array}{c c c} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c} v _ {x, c h a s s i s} \\ v _ {y, c h a s s i s} \\ \omega_ {c h a s s i s} \end{array} \right] \tag {8.7}
$$

We can control the model in equation (8.6) with an LQR, which will have three independent proportional controllers. Then, we can convert the global velocity commands to chassis velocity commands with equation (8.7) and convert the chassis velocity commands to wheel speed commands with inverse kinematics. LQRs on each wheel can track the wheel speed commands.

Note that the full control law is nonlinear because the kinematics contain a rotation matrix for transforming from the chassis frame to the global frame. However, the nonlinear part has been abstracted away from the tunable linear control laws.

This equation assumes a starting orientation of $\theta = 0$ . For nonzero starting orientations, we can apply a counterclockwise rotation by θ.

$$
^ G \left[ \begin{array}{c} \Delta x \\ \Delta y \\ \Delta \theta \end{array} \right] = \left[ \begin{array}{c c c} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} \frac {\sin \omega t}{\omega} & \frac {\cos \omega t - 1}{\omega} & 0 \\ \frac {1 - \cos \omega t}{\omega} & \frac {\sin \omega t}{\omega} & 0 \\ 0 & 0 & t \end{array} \right] ^ {R} \left[ \begin{array}{c} v _ {x} \\ v _ {y} \\ \omega \end{array} \right] (1 0. 1)
$$

![](image/df80b4aa8ec617e77446ee15da477f11d0e6ec554d434057fd00d694b63be421.jpg)

Control system implementations will generally have a model update and a controller update in a given iteration. Equation (10.1) (the model update) uses the current velocity to advance the state to the next timestep (into the future). Since controllers use the current state, the controller update should be run before the model update.

If we factor out a t, we can use change in pose between updates instead of velocities.

$$
^ G \left[ \begin{array}{c} \Delta x \\ \Delta y \\ \Delta \theta \end{array} \right] = \left[ \begin{array}{c c c} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} \frac {\sin \omega t}{\omega} & \frac {\cos \omega t - 1}{\omega} & 0 \\ \frac {1 - \cos \omega t}{\omega} & \frac {\sin \omega t}{\omega} & 0 \\ 0 & 0 & t \end{array} \right] ^ {R} \left[ \begin{array}{c} v _ {x} \\ v _ {y} \\ \omega \end{array} \right]

^ G \left[ \begin{array}{c} \Delta x \\ \Delta y \\ \Delta \theta \end{array} \right] = \left[ \begin{array}{c c c} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} \frac {\sin \omega t}{\omega t} & \frac {\cos \omega t - 1}{\omega t} & 0 \\ \frac {1 - \cos \omega t}{\omega t} & \frac {\sin \omega t}{\omega t} & 0 \\ 0 & 0 & 1 \end{array} \right] ^ {R} \left[ \begin{array}{c} v _ {x} \\ v _ {y} \\ \omega \end{array} \right] t

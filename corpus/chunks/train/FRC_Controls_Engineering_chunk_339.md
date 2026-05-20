^ G \left[ \begin{array}{c} \Delta x \\ \Delta y \\ \Delta \theta \end{array} \right] = \left[ \begin{array}{c c c} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} \frac {\sin \omega t}{\omega t} & \frac {\cos \omega t - 1}{\omega t} & 0 \\ \frac {1 - \cos \omega t}{\omega t} & \frac {\sin \omega t}{\omega t} & 0 \\ 0 & 0 & 1 \end{array} \right] ^ {R} \left[ \begin{array}{c} v _ {x} t \\ v _ {y} t \\ \omega t \end{array} \right]

^ G \left[ \begin{array}{c} \Delta x \\ \Delta y \\ \Delta \theta \end{array} \right] = \left[ \begin{array}{c c c} \cos \theta & - \sin \theta & 0 \\ \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right] ^ {R} \left[ \begin{array}{c c c} \frac {\sin \Delta \theta}{\Delta \theta} & \frac {\cos \Delta \theta - 1}{\Delta \theta} & 0 \\ \frac {1 - \cos \Delta \theta}{\Delta \theta} & \frac {\sin \Delta \theta}{\Delta \theta} & 0 \\ 0 & 0 & 1 \end{array} \right] ^ {R} \left[ \begin{array}{c} \Delta x \\ \Delta y \\ \Delta \theta \end{array} \right] (1 0. 2)
$$

The vector $\begin{array} { r } { \begin{array} { l l l } { ^ { R } \lceil \Delta x } & { \Delta y } & { \Delta \theta \rceil ^ { \mathsf { T } } } \end{array} } \end{array}$ is a twist because it’s an element of the tangent space (the robot’s local coordinate frame).

![](image/3c0042b55d9423a440f50e0cff8108bc75bdea28452d2ea24a9169ef3dbd9f60.jpg)

Control system implementations will generally have a model update and a controller update in a given iteration. Equation (10.2) (the model update) uses local distance and heading deltas between the previous and current timestep, so it advances the state to the current timestep. Since controllers use the current state, the controller update should be run after the model update.

When the robot is traveling on a straight trajectory $( \Delta \theta = 0 )$ , some expressions within the equation above are indeterminate. We can approximate these with Taylor series expansions.

$$\frac {\sin \Delta \theta}{\Delta \theta} = 1 - \frac {\Delta \theta^ {2}}{6} + \dots \approx 1 - \frac {\Delta \theta^ {2}}{6}\frac {\cos \Delta \theta - 1}{\Delta \theta} = - \frac {\Delta \theta}{2} + \frac {\Delta \theta^ {3}}{2 4} - \dots \approx - \frac {\Delta \theta}{2}\frac {1 - \cos \Delta \theta}{\Delta \theta} = \frac {\Delta \theta}{2} - \frac {\Delta \theta^ {3}}{2 4} + \dots \approx \frac {\Delta \theta}{2}$$

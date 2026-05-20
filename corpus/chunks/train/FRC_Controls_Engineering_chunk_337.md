# 10.2.4 Derivation

We can obtain a more accurate approximation of the pose than Euler integration by including first-order dynamics for the heading θ.

$$
\mathbf {x} = \left[ \begin{array}{c} x \\ y \\ \theta \end{array} \right]
$$

$v _ { x }$ , $v _ { y }$ , and $\omega$ are the x and y velocities of the robot within its local coordinate frame, which will be treated as constants.

![](image/efd41f905591d539e71a5b040af5d964b8d07daf55f47207ef6bc3c088e5264c.jpg)

There are two coordinate frames used here: robot and global. A superscript on the left side of a matrix denotes the coordinate frame in which that matrix is represented. The robot’s coordinate frame is denoted by R and the global coordinate frame is denoted by G.

In the robot frame (the tangent space)

$$^ R d x = ^ {R} v _ {x} d t^ R d y = ^ {R} v _ {y} d t^ R d \theta = ^ {R} \omega d t$$

To transform this into the global frame SE(2), we apply a counterclockwise rotation matrix where θ changes over time.

$$
^ {G} \left[ \begin{array}{c} d x \\ d y \\ d \theta \end{array} \right] = \left[ \begin{array}{c c c} \cos \theta (t) & - \sin \theta (t) & 0 \\ \sin \theta (t) & \cos \theta (t) & 0 \\ 0 & 0 & 1 \end{array} \right] ^ {R} \left[ \begin{array}{c} v _ {x} \\ v _ {y} \\ \omega \end{array} \right] d t

^ G \left[ \begin{array}{c} d x \\ d y \\ d \theta \end{array} \right] = \left[ \begin{array}{c c c} \cos \omega t & - \sin \omega t & 0 \\ \sin \omega t & \cos \omega t & 0 \\ 0 & 0 & 1 \end{array} \right] ^ {R} \left[ \begin{array}{c} v _ {x} \\ v _ {y} \\ \omega \end{array} \right] d t
$$

Now, integrate the matrix equation (matrices are integrated element-wise). This derivation heavily utilizes the integration method described in section 4.3.

$$
^ {G} \left[ \begin{array}{c} \Delta x \\ \Delta y \\ \Delta \theta \end{array} \right] = \left[ \begin{array}{c c c} \frac {\sin \omega t}{\omega} & \frac {\cos \omega t}{\omega} & 0 \\ - \frac {\cos \omega t}{\omega} & \frac {\sin \omega t}{\omega} & 0 \\ 0 & 0 & t \end{array} \right] ^ {R} \left[ \begin{array}{c} v _ {x} \\ v _ {y} \\ \omega \end{array} \right] \Bigg | _ {0} ^ {t}

^ G \left[ \begin{array}{c} \Delta x \\ \Delta y \\ \Delta \theta \end{array} \right] = \left[ \begin{array}{c c c} \frac {\sin \omega t}{\omega} & \frac {\cos \omega t - 1}{\omega} & 0 \\ \frac {1 - \cos \omega t}{\omega} & \frac {\sin \omega t}{\omega} & 0 \\ 0 & 0 & t \end{array} \right] ^ {R} \left[ \begin{array}{c} v _ {x} \\ v _ {y} \\ \omega \end{array} \right]
$$

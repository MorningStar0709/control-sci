# 8.8 Linear time-varying unicycle controller

One can also create a linear time-varying controller with a cascaded control architecture, where the outer layer consumes a pose command and produces unicycle velocity commands, and the inner layer consumes unicycle velocity commands and produces wheel motor voltages.

The change in global pose for a unicycle is defined by the following three equations.

$$\dot {x} = v \cos \theta\dot {y} = v \sin \theta\dot {\theta} = \omega$$

Here’s the model as a vector function where $\mathbf { x } = \left[ x \quad y \quad \theta \right] ^ { \mathsf { T } }$ and $\mathbf { u } = { \left[ \begin{array} { l l } { v } & { \omega } \end{array} \right] } ^ { \mathsf { T } }$ .

$$
f (\mathbf {x}, \mathbf {u}) = \left[ \begin{array}{c} v \cos \theta \\ v \sin \theta \\ \omega \end{array} \right] \tag {8.24}
$$

To create an LQR, we need to linearize this.

$$
\frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x}} = \left[ \begin{array}{c c c} 0 & 0 & - v \sin \theta \\ 0 & 0 & v \cos \theta \\ 0 & 0 & 0 \end{array} \right] \quad \frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {u}} = \left[ \begin{array}{c c} \cos \theta & 0 \\ \sin \theta & 0 \\ 0 & 1 \end{array} \right]
$$

We’re going to make a cross-track error controller, so we’ll apply a clockwise rotation matrix to the global tracking error to transform it into the robot’s coordinate frame. Since the cross-track error is always measured from the robot’s coordinate frame, the model used to compute the LQR should be linearized around θ = 0 at all times.

$$
\begin{array}{l} \mathbf {A} = \left[ \begin{array}{c c c} 0 & 0 & - v \sin 0 \\ 0 & 0 & v \cos 0 \\ 0 & 0 & 0 \end{array} \right] \quad \mathbf {B} = \left[ \begin{array}{c c} \cos 0 & 0 \\ \sin 0 & 0 \\ 0 & 1 \end{array} \right] \\ \mathbf {A} = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & v \\ 0 & 0 & 0 \end{array} \right] \qquad \qquad \mathbf {B} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] \\ \end{array}
$$

Therefore,

Theorem 8.8.1 — Linear time-varying unicycle controller. Let the unicycle dynamics be ${ \dot { \mathbf { x } } } = f ( \mathbf { x } , \mathbf { u } ) = \left[ v \cos \theta \right.$ v sin θ ωT where

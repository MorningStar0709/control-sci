# B.5.1 Continuous case

The undelayed continuous linear system is defined as ${ \dot { \mathbf { x } } } = \mathbf { A } \mathbf { x } ( t ) + \mathbf { B } \mathbf { u } ( t )$ with the controller $\mathbf { u } ( t ) = - \mathbf { K } \mathbf { x } ( t )$ . Let L be the delay duration in seconds. We can avoid the delay if we compute the control based on the plant L seconds in the future.

$$\mathbf {u} (t) = - \mathbf {K x} (t + L)$$

We need to find ${ \bf x } ( t + L )$ given ${ \bf x } ( t )$ . Since we know $\mathbf { u } ( t ) = - \mathbf { K } \mathbf { x } ( t )$ will be applied over the time interval $[ t , t + L )$ , substitute it into the continuous model.

$$
\begin{array}{l} \dot {\mathbf {x}} = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t) \\ \dot {\mathbf {x}} = \mathbf {A} \mathbf {x} (t) + \mathbf {B} (- \mathbf {K} \mathbf {x} (t)) \\ \dot {\mathbf {x}} = \mathbf {A} \mathbf {x} (t) - \mathbf {B} \mathbf {K} \mathbf {x} (t) \\ \dot {\mathbf {x}} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} (t) \\ \end{array}
$$

We now have a differential equation for the closed-loop system dynamics. Take the matrix exponential from the current time t to $L$ in the future to obtain ${ \bf x } ( t + L )$ .

$$\mathbf {x} (t + L) = e ^ {(\mathbf {A} - \mathbf {B K}) L} \mathbf {x} (t) \tag {B.8}$$

This works for $t \geq L$ , but if $t < L$ , we have no input history for the time interval $[ t , L )$ . If we assume the inputs for $[ t , L )$ are zero, the state prediction for that interval is

$$\mathbf {x} (L) = e ^ {\mathbf {A} (L - t)} \mathbf {x} (t)$$

The time interval $[ 0 , t )$ has nonzero inputs since it’s in the past and was using the normal control law.

$$
\begin{array}{l} \mathbf {x} (t + L) = e ^ {(\mathbf {A} - \mathbf {B K}) t} \mathbf {x} (L) \\ \mathbf {x} (t + L) = e ^ {(\mathbf {A} - \mathbf {B K}) t} e ^ {\mathbf {A} (L - t)} \mathbf {x} (t) \tag {B.9} \\ \end{array}
$$

Therefore, equations (B.8) and (B.9) give the latency-compensated control law for all $t \geq 0$ .

$$
\begin{array}{l} \mathbf {u} (t) = - \mathbf {K x} (t + L) \\ \mathbf {u} (t) = \left\{ \begin{array}{l l} - \mathbf {K} e ^ {(\mathbf {A} - \mathbf {B K}) t} e ^ {\mathbf {A} (L - t)} \mathbf {x} (t) & \text { if } 0 \leq t <   L \\ - \mathbf {K} e ^ {(\mathbf {A} - \mathbf {B K}) L} \mathbf {x} (t) & \text { if } t \geq L \end{array} \right. \tag {B.10} \\ \end{array}
$$

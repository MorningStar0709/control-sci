# B.5.2 Discrete case

The undelayed discrete linear system is defined as $\mathbf { x } _ { k + 1 } = \mathbf { A } \mathbf { x } _ { k } + \mathbf { B } \mathbf { u } _ { k }$ with the controller $\mathbf { u } _ { k } = - \mathbf { K } \mathbf { x } _ { k }$ . Let $L$ be the delay duration in seconds. We can avoid the delay if we compute the control based on the plant L seconds in the future.

$$\mathbf {u} _ {k} = - \mathbf {K x} _ {k + L / T}$$

We need to find $\mathbf { x } _ { k + L / T }$ given $\mathbf { x } _ { k }$ . Since we know $\mathbf { u } _ { k } = - \mathbf { K } \mathbf { x } _ { k }$ will be applied for the timesteps k through $\begin{array} { r } { k + \frac { L } { T } } \end{array}$ , substitute it into the discrete model.

$$
\begin{array}{l} \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k} \\ \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B} (- \mathbf {K x} _ {k}) \\ \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} - \mathbf {B K x} _ {k} \\ \mathbf {x} _ {k + 1} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} _ {k} \\ \end{array}
$$

Let $T$ be the duration between timesteps in seconds and L be the delay duration in seconds. $\textstyle { \frac { L } { T } }$ gives the number of timesteps represented by $L .$ .

$$\mathbf {x} _ {k + L / T} = \left(\mathbf {A} - \mathbf {B K}\right) ^ {\frac {L}{T}} \mathbf {x} _ {k} \tag {B.11}$$

This works for $k T \geq L$ where $k T$ is the current time, but if $k T < L$ , we have no input history for the time interval $[ k T , L )$ . If we assume the inputs for $[ k T , L )$ are zero, the state prediction for that interval is

$$
\begin{array}{l} \mathbf {x} _ {L / T} = \mathbf {A} ^ {\frac {L - k T}{T}} \mathbf {x} _ {k} \\ \mathbf {x} _ {L / T} = \mathbf {A} ^ {\frac {L}{T} - k} \mathbf {x} _ {k} \\ \end{array}
$$

The time interval $[ 0 , k T )$ has nonzero inputs since it’s in the past and was using the normal control law.

$$
\begin{array}{l} \mathbf {x} _ {k + L / T} = (\mathbf {A} - \mathbf {B K}) ^ {k} \mathbf {x} _ {L / T} \\ \mathbf {x} _ {k + L / T} = \left(\mathbf {A} - \mathbf {B K}\right) ^ {k} \mathbf {A} ^ {\frac {L}{T} - k} \mathbf {x} _ {k} \tag {B.12} \\ \end{array}
$$

Therefore, equations (B.11) and (B.12) give the latency-compensated control law for all $t \geq 0$ .

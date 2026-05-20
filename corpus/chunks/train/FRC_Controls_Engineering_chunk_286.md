# 9.4 Linear stochastic systems

Given the following stochastic system

$$\mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k} + \mathbf {w} _ {k}\mathbf {y} _ {k} = \mathbf {C x} _ {k} + \mathbf {D u} _ {k} + \mathbf {v} _ {k}$$

where ${ \bf w } _ { k }$ is the process noise and $\mathbf { v } _ { k }$ is the measurement noise,

$$
\begin{array}{l} E [ \mathbf {w} _ {k} ] = 0 \\ E [ \mathbf {w} _ {k} \mathbf {w} _ {k} ^ {\top} ] = \mathbf {Q} _ {k} \\ E [ \mathbf {v} _ {k} ] = 0 \\ E [ \mathbf {v} _ {k} \mathbf {v} _ {k} ^ {\mathsf {T}} ] = \mathbf {R} _ {k} \\ \end{array}
$$

where $\mathbf { Q } _ { k }$ is the process noise covariance matrix and ${ \bf R } _ { k }$ is the measurement noise covariance matrix. We assume the noise samples are independent, so $E [ \mathbf { w } _ { k } \mathbf { w } _ { j } ^ { \mathsf { T } } ] = 0$ and $E [ \mathbf { v } _ { k } \mathbf { v } _ { j } ^ { \mathsf { T } } ] = 0$ where $k \neq j$ . Furthermore, process noise samples are independent from measurement noise samples.

We’ll compute the expectation of these equations and their covariance matrices, which we’ll use later for deriving the Kalman filter.

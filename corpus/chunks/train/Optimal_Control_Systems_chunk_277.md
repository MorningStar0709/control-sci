# 5.3 Discrete-Time Linear State Regulator System

optimal control in terms of the state. We may write the closed-loop, optimal control relation $(5.3.15)$ in a simplified form as

$$\boxed {\mathbf {u} ^ {*} (k) = - \mathbf {L} (k) \mathbf {x} ^ {*} (k)} \tag {5.3.16}$$

where,

$$\mathbf {L} (k) = \mathbf {R} ^ {- 1} (k) \mathbf {B} ^ {\prime} (k) \mathbf {A} ^ {- T} (k) [ \mathbf {P} (k) - \mathbf {Q} (k) ]. \tag {5.3.17}$$

This is the required relation for the optimal feedback control law and the feedback gain $\mathbf{L}(k)$ is called the “Kalman gain.” The optimal state $\mathbf{x}^{*}(k)$ is obtained by substituting the optimal control $\mathbf{u}^{*}(k)$ given by (5.3.16) in the original state equation (5.2.1) as

$$\mathbf {x} ^ {*} (k + 1) = (\mathbf {A} (k) - \mathbf {B} (k) \mathbf {L} (k)) \mathbf {x} ^ {*} (k). \tag {5.3.18}$$

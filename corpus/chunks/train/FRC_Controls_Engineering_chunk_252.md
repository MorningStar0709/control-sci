$$
\left[ \begin{array}{c} \dot {v _ {l}} \\ v _ {r} \\ x _ {l} \\ x _ {r} \end{array} \right] = \left[ \begin{array}{l l l} \mathbf {A} & \mathbf {B} & \mathbf {B} _ {\theta} \end{array} \right] \left[ \begin{array}{c} v _ {l} \\ v _ {r} \\ x _ {l} \\ x _ {r} \\ u _ {\text { error }, l} \\ u _ {\text { error }, r} \\ u _ {\text { error }, \text { heading }} \end{array} \right] + \mathbf {B u} \tag {8.21}
$$

A and B are the linear subspace from equation (8.19).

The $u _ { e r r o r } $ states have no dynamics. The observer selects them to minimize the difference between the expected and actual measurements.

$$
\left[ \begin{array}{c} u _ {\text { error }, l} \\ u _ {\text { error }, r} \\ u _ {\text { error }, \text { heading }} \end{array} \right] = \mathbf {0} _ {3 \times 1} \tag {8.22}
$$

The controller is augmented as follows.

$$
\mathbf {K} _ {\text {error}} = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \quad \mathbf {K} _ {\text {aug}} = \left[ \begin{array}{l l} \mathbf {K} & \mathbf {K} _ {\text {error}} \end{array} \right] \quad \mathbf {r} _ {\text {aug}} = \left[ \begin{array}{l} \mathbf {r} \\ 0 \\ 0 \\ 0 \end{array} \right] \tag {8.23}
$$

This controller augmentation compensates for unmodeled dynamics like:

1. Understeer caused by wheel friction inherent in skid-steer robots   
2. Battery voltage drop under load, which reduces the available control authority

![](image/5e2860a0369946350c09739ca7dd2d44852083629671fbc4554f5b7dc29d2c24.jpg)

The process noise for the voltage error states should be how much the voltage can be expected to drop. The heading error state should be the encoder model uncertainty.

# 12.5.2 Torque derivation

The equation can be obtained using two definitions for torque.

$$\boldsymbol {\tau} = \mathbf {r} \times \mathbf {F}$$

First start by defining the torque on the pendulum bob using the force due to gravity.

$$\boldsymbol {\tau} = \mathbf {l} \times \mathbf {F} _ {g}$$

where l is the length vector of the pendulum and $\mathbf { F } _ { g }$ is the force due to gravity.

For now just consider the magnitude of the torque on the pendulum.

$$| \tau | = - m g l \sin \theta$$

where $m$ is the mass of the pendulum, g is the acceleration due to gravity, l is the length of the pendulum and θ is the angle between the length vector and the force due to gravity.

Next rewrite the angular momentum.

$$\mathbf {L} = \mathbf {r} \times \mathbf {p} = m \mathbf {r} \times (\boldsymbol {\omega} \times \mathbf {r})$$

Again just consider the magnitude of the angular momentum.

$$| \mathbf {L} | = m r ^ {2} \omega| \mathbf {L} | = m l ^ {2} \frac {d \theta}{d t}\frac {d}{d t} | \mathbf {L} | = m l ^ {2} \frac {d ^ {2} \theta}{d t ^ {2}}$$

According to ${ \begin{array} { r } { { \boldsymbol { \tau } } = { \frac { d \mathbf { L } } { d t } } } \end{array} } $ , we can just compare the magnitudes.

$$- m g l \sin \theta = m l ^ {2} \frac {d ^ {2} \theta}{d t ^ {2}}- \frac {g}{l} \sin \theta = \frac {d ^ {2} \theta}{d t ^ {2}}\ddot {\theta} = - \frac {g}{l} \sin \theta$$

which is the same result from force analysis.

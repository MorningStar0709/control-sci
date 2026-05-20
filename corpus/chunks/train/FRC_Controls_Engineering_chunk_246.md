# 8.7.5 Cross track error controller

Figures 8.6 and 8.7 show the tracking performance of the linearized differential drive controller for a given trajectory. The performance-effort trade-off can be tuned rather intuitively via the Q and R gains. However, if the x and y error cost are too high, the x and y components of the controller will fight each other, and it will take longer to converge to the path. This can be fixed by applying a clockwise rotation matrix to the global tracking error to transform it into the robot’s coordinate frame.

$$
^ R \left[ \begin{array}{c} e _ {x} \\ e _ {y} \\ e _ {\theta} \end{array} \right] = \left[ \begin{array}{c c c} \cos \theta & \sin \theta & 0 \\ - \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right] ^ {G} \left[ \begin{array}{c} e _ {x} \\ e _ {y} \\ e _ {\theta} \end{array} \right]
$$

where the the superscript R represents the robot’s coordinate frame and the superscript G represents the global coordinate frame.

With this transformation, the x and y error cost in LQR penalize the error ahead of the robot and cross-track error respectively instead of global pose error. Since the crosstrack error is always measured from the robot’s coordinate frame, the model used to compute the LQR should be linearized around θ = 0 at all times.

$$
\mathbf {A} = \left[ \begin{array}{l l l l l} 0 & 0 & - \frac {v _ {l} + v _ {r}}{2} \sin 0 & \frac {1}{2} \cos 0 & \frac {1}{2} \cos 0 \\ 0 & 0 & \frac {v _ {l} + v _ {r}}{2} \cos 0 & \frac {1}{2} \sin 0 & \frac {1}{2} \sin 0 \\ 0 & 0 & 0 & - \frac {1}{2 r _ {b}} & \frac {1}{2 r _ {b}} \\ 0 & 0 & 0 & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \\ 0 & 0 & 0 & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \end{array} \right]

\mathbf {A} = \left[ \begin{array}{c c c c c} 0 & 0 & 0 & \frac {1}{2} & \frac {1}{2} \\ 0 & 0 & \frac {v _ {l} + v _ {r}}{2} & 0 & 0 \\ 0 & 0 & 0 & - \frac {1}{2 r _ {b}} & \frac {1}{2 r _ {b}} \\ 0 & 0 & 0 & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \\ 0 & 0 & 0 & \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} & \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} \end{array} \right]
$$

Theorem 8.7.4 — Linear time-varying differential drive controller. Let the differential drive dynamics be of the form $\dot { \mathbf { x } } = f ( \mathbf { x } ) + \mathbf { B } \mathbf { u }$ where

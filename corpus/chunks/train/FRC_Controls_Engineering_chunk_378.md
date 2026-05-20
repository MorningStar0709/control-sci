# 12.3.1 Equations of motion

We want to derive an equation for the flywheel angular acceleration $\dot { \omega } _ { f }$ given an input voltage V , which we can integrate to get flywheel angular velocity.

We will start with the equation derived earlier for a DC motor, equation (12.3).

$$V = \frac {\tau_ {m}}{K _ {t}} R + \frac {\omega_ {m}}{K _ {v}}$$

Solve for the angular acceleration. First, we’ll rearrange the terms because from inspection, V is the model input, $\omega _ { m }$ is the state, and $\tau _ { m }$ contains the angular acceleration.

$$V = \frac {R}{K _ {t}} \tau_ {m} + \frac {1}{K _ {v}} \omega_ {m}$$

Solve for $\tau _ { m }$

$$
\begin{array}{l} V = \frac {R}{K _ {t}} \tau_ {m} + \frac {1}{K _ {v}} \omega_ {m} \\ \frac {R}{K _ {t}} \tau_ {m} = V - \frac {1}{K _ {v}} \omega_ {m} \\ \end{array}
\tau_ {m} = \frac {K _ {t}}{R} V - \frac {K _ {t}}{K _ {v} R} \omega_ {m}
$$

Since $\tau _ { m } G = \tau _ { f }$ and $\omega _ { m } = G \omega _ { f }$ ,

$$\left(\frac {\tau_ {f}}{G}\right) = \frac {K _ {t}}{R} V - \frac {K _ {t}}{K _ {v} R} (G \omega_ {f})\frac {\tau_ {f}}{G} = \frac {K _ {t}}{R} V - \frac {G K _ {t}}{K _ {v} R} \omega_ {f}\tau_ {f} = \frac {G K _ {t}}{R} V - \frac {G ^ {2} K _ {t}}{K _ {v} R} \omega_ {f} \tag {12.16}$$

The torque applied to the flywheel is defined as

$$\tau_ {f} = J \dot {\omega} _ {f} \tag {12.17}$$

where $J$ is the moment of inertia of the flywheel and $\dot { \omega } _ { f }$ is the angular acceleration. Substitute equation (12.17) into equation (12.16).

$$(J \dot {\omega} _ {f}) = \frac {G K _ {t}}{R} V - \frac {G ^ {2} K _ {t}}{K _ {v} R} \omega_ {f}\dot {\omega} _ {f} = \frac {G K _ {t}}{R J} V - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega_ {f}\dot {\omega} _ {f} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega_ {f} + \frac {G K _ {t}}{R J} V$$

We’ll relabel $\omega _ { f }$ as $\omega$ for convenience.

$$\dot {\omega} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega + \frac {G K _ {t}}{R J} V \tag {12.18}$$

This model will be converted to state-space notation in section 6.10.

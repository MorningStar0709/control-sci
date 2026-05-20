# 6.10.5 Flywheel model without encoder

In the FIRST Robotics Competition, we can get the current drawn for specific channels on the power distribution panel. We can theoretically use this to estimate the angular velocity of a DC motor without an encoder. We’ll start with the flywheel model derived earlier as equation (12.18).

$$\dot {\omega} = \frac {G K _ {t}}{R J} V - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega\dot {\omega} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \omega + \frac {G K _ {t}}{R J} V$$

Next, we’ll derive the current I as an output.

$$V = I R + \frac {\omega}{K _ {v}}I R = V - \frac {\omega}{K _ {v}}I = - \frac {1}{K _ {v} R} \omega + \frac {1}{R} V$$

Therefore,

Theorem 6.10.2 — Flywheel state-space model without encoder.

$$\dot {\mathbf {x}} = \mathbf {A x} + \mathbf {B u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}$$

x = ω = angular velocity y = I = current u = V = voltage

$$\mathbf {A} = - \frac {G ^ {2} K _ {t}}{K _ {v} R J} \tag {6.19}\mathbf {B} = \frac {G K _ {t}}{R J} \tag {6.20}\mathbf {C} = - \frac {1}{K _ {v} R} \tag {6.21}\mathbf {D} = \frac {1}{R} \tag {6.22}$$

Notice that in this model, the output doesn’t provide any direct measurements of the state. To estimate the full state (also known as full observability), we only need the outputs to collectively include linear combinations of every state[13]. We’ll revisit this in chapter 9 with an example that uses range measurements to estimate an object’s orientation.

The effectiveness of this model’s observer is heavily dependent on the quality of the current sensor used. If the sensor’s noise isn’t zero-mean, the observer won’t converge to the true state.

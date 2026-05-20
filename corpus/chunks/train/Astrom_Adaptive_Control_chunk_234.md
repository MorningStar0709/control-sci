# Self-tuning Feedforward Control

Feedforward control is a very useful way to reduce the influence of known disturbances. Examples of measurable disturbances can be temperatures and concentrations in incoming product streams in chemical processes, outdoor temperature in climate control systems, and thickness of the paper in paper machines. Command signals can also be interpreted as a measurable disturbance. The controller in Eq. (3.2) can be interpreted as feedforward from the command signal. To use feedforward, it is necessary to know the dynamics of the process. It is, however, also possible to establish self-tuning feedforward compensation. One way to do this is to postulate a model structure of the form

$$y (t + d) = R ^ {*} u (t) + S ^ {*} y (t) + T ^ {*} v (t) + \varepsilon (t + d)$$

where $v(t)$ is the measurable disturbance acting on the system. The signal v could also be the reference value. The polynomials $R^{*}$ , $S^{*}$ , and $T^{*}$ are estimated in the usual way, and the control law is chosen to be

$$u (t) = - \frac {S ^ {*}}{R ^ {*}} y (t) - \frac {T ^ {*}}{R ^ {*}} v (t)$$

Self-tuning feedforward control has been used successfully in many industrial applications.

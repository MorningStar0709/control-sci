# Ship Steering Dynamics

Simple ship steering dynamics were presented in connection with the discussion of gain scheduling in Section 9.5. That section detailed how the dynamics vary with the velocity of the ship and showed how the variations could be reduced by gain scheduling. It has been shown by hydrodynamic theory that the average increase in drag due to yawing and rudder motions can be approximately described by

$$\frac {\Delta R}{R} = k \left(\bar {\psi} ^ {2} + \lambda \bar {\delta} ^ {2}\right) \tag {12.2}$$

where R is the drag and $\bar{\psi}^{2}$ and $\bar{\delta}^{2}$ denote the mean square of heading error and rudder angle amplitude, respectively. The parameters k and $\lambda$ will depend on the ship and its operating conditions. The following numerical values are typical for a tanker:

$$k = 0. 0 1 4 \mathrm{deg} ^ {2} \quad \lambda = 1 / 1 2$$

It is thus natural to use the criterion

$$V - \frac {1}{T} \int_ {0} ^ {T} \left(\left(\psi (t) - \psi_ {\mathrm{ref}}\right) ^ {2} + \lambda \delta^ {2} (t)\right) d t \tag {12.3}$$

as a basis for the design and evaluation of autopilots for steady-state course keeping. The disturbances acting on the system are due to wind, waves, and currents. A detailed characterization of the disturbances and their effect on the ship's motion is difficult. In a linearized model, disturbances appear as additive terms. It is common practice to describe them as random signals; the waves have a narrow band spectrum. The center frequency and the amplitude may vary significantly.

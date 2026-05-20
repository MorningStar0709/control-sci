# Specifications

To obtain a robust controller, it is very important that specifications be chosen in a sensible way. With a pole placement design, this means that the desired closed-loop poles have to be chosen with care. Poles that are too fast will give controllers that are very sensitive. This can be understood from the following expression, which gives a sufficient condition for stability of a pole placement design:

$$\left| H (z) - H _ {0} (z) \right| < \left. \frac {H (z) T (z)}{H _ {m} (z) S (z)} \right|$$

In this expression, H is the pulse transfer function of model used to design the controller, $H_{0}$ is the pulse transfer function of the true plant, $H_{m} = B_{m}/A_{m}$ is the desired response, and S and T are the controller polynomials. The inequality should hold on the unit circle. The condition implies that high model precision is required for those frequencies at which the desired closed-loop system has significantly higher gain than the model.

A reasonable way to determine the closed-loop poles is to make the observation that it is difficult to obtain a crossover frequency that is significantly higher than the frequency at which the plant has a phase lag of $180^{\circ}-270^{\circ}$ . Notice that these frequencies can conveniently be determined by a relay feedback experiment.

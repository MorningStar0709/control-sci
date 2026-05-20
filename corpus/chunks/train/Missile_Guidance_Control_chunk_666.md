Missile State Runge–Kutta Integration: The Runge–Kutta integration method is a fourth-order multistep integration technique that was derived from a Taylor series expansion. It allows for a high degree of accuracy while requiring an acceptable number of calculations to complete the integration. In order to perform an integration, the model sets the integration time $\Delta t$ as the smaller of the flight-section-referenced integration step size and the missile-state update time interval over which to perform the integration. When integrating over the interval from time t to time $t + \Delta t$ in the missile flyout, the method calculates the state properties at the beginning of the interval, halfway through, and then at the end of the interval. Four coefficients are calculated in updating the missile state at these different points in the interval. These coefficients are calculated for each missile state parameter being integrated: time-inflight, total missile mass, position components, and velocity components. They are then combined, and the missile’s state at the end of the interval is then extracted. In order to illustrate the Runge–Kutta technique, the missile interim state at time t is stored in temporary variables:

$$t _ {R K} = t,M _ {R K} = M _ {T},X _ {R K n} = X _ {n},V _ {R K n} = V _ {n}, \tag {6.268}$$

where

$$t _ {R K} = \text { Runge - - Kutta missile time of flight [sec]},t = \text { missile time of flight } [ \sec ],M _ {T} = \text { total missile mass } [ \mathrm{kg} ],M _ {R K} = \text { Runge - - Kutta missile mass [kg]},X _ {R K n} = \text { Runge - - Kutta missile position in } n \text {-direction [m] },X _ {n} = \text { missile position in } E C I n \text {-direction [m] },V _ {n} = \text { missile velocity in } E C I n \text {-direction} [ \mathrm{m/sec} ],V _ {R K n} = \text { Runge - - Kutta missile velocity in } n \text {-direction [m / sec] }.$$

These interim state values are then used to calculate the acceleration A as shown above. The first of the four Runge–Kutta (RK) state coefficients is then calculated by the following relations:

$$t _ {K 1} = \Delta t,M _ {K 1} = - B _ {R} \times \Delta t,X _ {K 1 n} = V _ {R K n} \times \Delta t,V _ {K 1 n} = A _ {n} \times \Delta t, \tag {6.269}$$

where

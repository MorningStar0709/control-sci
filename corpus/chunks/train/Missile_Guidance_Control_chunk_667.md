$$t _ {K 1} = \text { Runge - - Kutta coefficient 1 for missile time of flight } \Delta [ \sec ],M _ {K 1} = \text { Runge - - Kutta coefficient 1 for missile burned mass [kg]},B _ {R} = \text { missile fuel burn rate } [ \mathrm{kg/sec} ],X _ {K 1 n} = \text { Runge - - Kutta coefficient 1 for missile position } \Delta \text { in } n \text {-direction [m] },A _ {n} = \text { total acceleration in } E C I n \text {-direction} [ \mathrm{m} / \sec^ {2} ],\Delta t = \text { integration time } [ \sec ].$$

The interim missile state parameters are now updated using the first Runge–Kutta coefficients:

$$t _ {R K} = t + \frac {1}{2} t _ {K 1},M _ {R K} = M _ {T} + \frac {1}{2} M _ {K 1},X _ {R K n} = X _ {n} + \frac {1}{2} X _ {K 1 n},V _ {R K n} = V _ {n} + \frac {1}{2} V _ {K 1 n}, \tag {6.270}$$

where

$$t _ {R K} = \text { Runge - - Kutta missile time of flight [sec]},t = \text { missile time of flight } [ \sec ].$$

The missile state at the end of the interval is then calculated using the state values at the beginning of the interval and all four of the Runge–Kutta coefficients [12]:

$$t _ {R K} = t + \left(t _ {K 1} + 2 t _ {K 2} + 2 t _ {K 3} + t _ {K 4}\right) / 6. 0, \tag {6.271a}M _ {R K} = M _ {T} + \left(M _ {K 1} + 2 M _ {K 2} + 2 M _ {K 3} + M _ {K 4}\right) / 6. 0, \tag {6.271b}X _ {R K n} = X _ {n} + \left(X _ {K 1 n} + 2 X _ {K 2 n} + 2 X _ {K 3 n} + X _ {K 4 n}\right) / 6. 0, \tag {6.271c}V _ {R K n} = V _ {n} + \left(V _ {K 1 n} + 2 V _ {K 2 n} + 2 V _ {K 3 n} + V _ {K 4 n}\right) / 6. 0, \tag {6.271d}$$

where all the parameters have already been defined above. This entire procedure is repeated until the missile impacts with the target. Finally, it is noted that impact is defined as having occurred when the descending missile’s altitude is less than the target altitude.

In Section 6.5.3 the missile control system was discussed with particular emphasis on pitch/steering control for atmospheric exit. In some ballistic missiles, steering is effected by pitch and yaw commands determined from the gravity-free accelerations and velocities to be gained. Normally, pitch and yaw commands are issued after firststage ignition. For the first few seconds of powered flight, steering is employed for purposes of launch recovery, in order to provide a (prescribed) given orientation to the missile axis. Steering based on the guidance equations is then dominant for the remainder of the powered trajectory.

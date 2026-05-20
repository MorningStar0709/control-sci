Since $p r$ and dr measurements are uncorrelated from satellite to satellite, updates can be applied independently. Therefore, 4-pr updates can be applied as independent measurements with variance σ pr2, ${ \sigma _ { p r } } ^ { 2 }$

$$K = P H [ H ^ {T} P H + \sigma_ {p r} ^ {2} ] ^ {- 1}.$$

(Note that no matrix inversion is necessary to calculate K.)

• Similarly, the same is true for 4-dr updates.   
• This implementation significantly reduces computation.

(8 × scalar measurement updates takes significantly less computation than 1 × 8-element vector update.)

Next, we need to define the state and measurement noise matrices, Q and R. These are defined as follows:

State Noise Q: State noise represents effects of unmodeled GPS system errors on states:

Atmospheric effects.

Ephemeris and clock errors.

Selective availability.

Measurement Noise R: Combination of receiver and user clock noise:

$$R _ {p r} = 1 5 \mathrm{m(C/Acode)},R _ {d r} = 1 \mathrm{cm}.$$

Lastly, we must consider the state propagation process. For the state propagation, the following facts are observed:

• P r and dr updates provided every second.

For navigation, position and velocity updates are generally required more frequently. Therefore, P r and dr updates must propagate between seconds:

$$P (k T + \Delta t) = P (k T) + V (k T) \Delta t + A (k T) (\Delta t ^ {2} / 2),V (k T + \Delta t) = V (k T) + A (k T) \Delta t,$$

(Note: A = acceleration, V = velocity.)

In designing a Kalman filter for GPS, the following facts should be considered:

• An 11-state filter is the optimal Kalman implementation for dynamic environments.   
• Reducing the number of states reduces the computational load.   
• There is a trade-off between optimal implementation and computational cost.

An 8-state Kalman filter design would be sufficient in a low dynamic environment, such as land or marine navigation.

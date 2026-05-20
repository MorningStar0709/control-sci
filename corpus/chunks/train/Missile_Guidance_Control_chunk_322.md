# White Noise Roll Rate

The above formulation involves the use of a total of ten state variables (i.e., 3 positions, 3 velocities, 3 accelerations, and one roll rate). However, it may be reasonable to use a model in which the roll rate is assumed to be white noise; that is, (4.90c) is replaced by

$$\omega = w _ {\omega}. \tag {4.99}$$

In this case the number of state variables is reduced to nine. Thus, if we simply omit the roll-rate noise $w _ { \omega }$ , the estimator will exclude any random out-of-plane maneuvers.

The scheme described above is believed to provide a reasonable approach to the three-dimensional target maneuver estimation problem. Although the derivation is relatively complex, the final result does not appear unreasonable computationally, especially in view of the fact that it is probably difficult to achieve good three-dimensional tracking with fewer than nine state variables. It could prove necessary to introduce more state variables if one wished to estimate such rates as gyro drift rates, etc. Finally, it is recommended that such a scheme be simulated and tested against realistic maneuvers.

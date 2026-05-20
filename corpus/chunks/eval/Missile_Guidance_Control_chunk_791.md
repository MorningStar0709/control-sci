$$\hat {\mathbf {x}} _ {k} (+) = \hat {\mathbf {x}} _ {k} (-) + K _ {k} [ \mathbf {z} _ {k} - H _ {k} \hat {\mathbf {x}} _ {k} (-) ]$$

Error Covariance Update:

$$P _ {k} (+) = [ I - K _ {k} H _ {k} ] P _ {k} (-).$$

Kalman Gain Matrix:

$$K _ {k} = P _ {k} (-) H _ {k} ^ {T} [ H _ {k} P _ {k} (-) H _ {k} ^ {T} + R _ {k} ] ^ {- 1}.$$

(Note: The superscript T denotes matrix transposition.)

In Section 7.3 it was stated that the INS for the cruise missile can be modeled with 10 states. In integrated GPS/INS applications, Kalman filters of 15–24 state variables have been shown to be suitable (i.e., optimal). For the reasons mentioned earlier, tightly coupled GPS/INS systems are commonly used in such applications.

In a typical GPS/INS application, the following state variables can be chosen:

3-Axis INS Error Model:

3 Position error states,   
3 Velocity error states,   
3 Platform tilts,   
3 Gyroscope drift rate errors,   
3 Accelerometer errors (biases).

GPS Error Model:

3 User position components,

3 User velocity components,

1 User clock bias,

1 User clock bias rate.

Of course, the final selection of the appropriate state variables will depend on the mission requirements, computational load, accuracy, cost, etc. In some applications, an 11-state Kalman filter would be required. These states are:

3 position, 3 velocity, and 2 clock states required for navigation solution from pseudorange (pr) and delta-range (dr).   
• 3 acceleration states required for propagation of velocity between measurement updates (required in a dynamic environment).

Mathematically, or in the Kalman filter notation, these states can be expressed as follows:

• States: $\mathbf { x } ^ { T } = [ p _ { x } p _ { y } p _ { z } v _ { x } v _ { y } v _ { z } b _ { u } r _ { u } a _ { x } a _ { y } a _ { z } ] ,$   
• Propagation:

$$
\Phi = \left[ \begin{array}{c c c} I _ {4} & I _ {4} & \frac {1}{2} I _ {3} \\ 0 & I _ {4} & I _ {3} \\ 0 & 0 & I _ {3} \end{array} \right]
$$

• Pseudorange (pr) Update: $H _ { p r } ^ { T } = [ 1 _ { i } ^ { T } 1 ~ 0 ^ { T } 0 ^ { T } ] , i = 1 , \ldots , 4 ,$   
• Delta-range (dr) Update: $H _ { d r } ^ { \hat { T } } = [ 0 ^ { T } 1 _ { i } ^ { T } 1 ~ 0 ^ { T } ] , i = 1 , \ldots , 4 ,$   
• Initial Variance: $P _ { o } = E \{ \hat { \mathbf { x } } _ { o } \hat { \mathbf { x } } _ { o } ^ { T } \}$ ,

Initial position and time uncertainty.

Initial velocity and clock rate uncertainty (dynamic dependent).

Initial acceleration uncertainty (dynamic dependent).

For the Kalman measurement updates, the following facts are noted:

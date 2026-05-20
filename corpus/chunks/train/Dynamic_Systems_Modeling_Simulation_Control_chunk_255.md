# Example 5.17

Consider the electromechanical DC motor system presented in Chapter 3 and Examples 5.6 and 5.7. Draw the complete block diagram of the DC motor using transfer functions to represent the armature circuit and mechanical rotor dynamics. The desired system output is angular velocity of the rotor, ??.

The mathematical model of the DC motor consists of two linear, coupled, first-order ODEs

$$L \dot {I} + R I = e _ {\text { in }} (t) - K _ {b} \omega \tag {5.117}J \dot {\omega} + b \omega = K _ {m} I - T _ {L} \tag {5.118}$$

We choose to utilize the first-order model of the mechanical rotor (5.118) because the desired system output is angular velocity ??. The transfer function for the armature circuit can be developed by considering the right-hand side of Eq. (5.117) as input $u _ { 1 }$

$$L \dot {I} + R I = u _ {1} \tag {5.119}$$

Therefore, the transfer function for the armature circuit is

$$\frac {1}{L s + R} = \frac {I (s)}{U _ {1} (s)} \tag {5.120}$$

where the input to the circuit transfer function is $u _ { 1 } = e _ { \mathrm { i n } } ( t ) - K _ { b } \omega _ { \mathrm { \ell } }$ , or the “net voltage” comprised the source voltage $e _ { \mathrm { i n } } ( t )$ minus the “back-emf” voltage $K _ { b } \omega$ . Similarly, the mechanical rotor transfer function can be developed from Eq. (5.118) by defining the net torque input $u _ { 2 } = K _ { m } I - T _ { L }$

$$J \dot {\omega} + b \omega = u _ {2} \tag {5.121}$$

The mechanical system transfer function is

$$\frac {1}{J s + b} = \frac {\Omega (s)}{U _ {2} (s)} \tag {5.122}$$

where $\mathcal { L } \left\{ \omega ( t ) \right\} = \Omega ( s )$ is the Laplace transform of angular velocity. The input to the mechanical transfer function is the net torque, which is motor torque $K _ { m } I$ minus the load torque $T _ { L }$ .

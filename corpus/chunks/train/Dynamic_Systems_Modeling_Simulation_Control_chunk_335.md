# Engineering Applications

6.13 Recall that Problem 2.19 in Chapter 2 presented a nonlinear model of “stick-slip” friction for mechanical systems. This problem will demonstrate how the dynamic response of a simple mechanical system is affected by the choice of the friction force model. The mathematical model of a simple 1-DOF mechanical system is

$$m \ddot {x} + F _ {f} + k x = F _ {a} (t)$$

where m is the mass, $F _ { f }$ is the friction force, k is the stiffness (spring) coefficient, x is the displacement of mass m from static equilibrium (in m), and $F _ { a } ( t )$ is the applied force. Obtain the dynamic responses using Simulink for the two friction models:

1) Linear viscous friction: $F _ { f } = b \dot { x }$   
2) Nonlinear stick-slip friction: $F _ { f } = [ F _ { C } + ( F _ { \mathrm { s t } } - F _ { C } ) \exp ( - \lvert \dot { x } \rvert / c ) ] \operatorname { s g n } ( \dot { x } ) + b \dot { x }$

The system parameters are $m = 2 \mathrm { k g } , k = 8 0 0 \mathrm { N } / \mathrm { m } , b = 2 5 \mathrm { N } \mathrm { - s } / \mathrm { m } , F _ { \mathrm { s t } } = 1 . 2 \mathrm { N }$ (stiction force), $F _ { C } = 1 \mathrm { N }$ (Coulomb friction force), c = 0.002 m/s (velocity coefficient). The external force $F _ { a } ( t )$ is a 15-N step function applied at time $t = 0 . 2 { \ : } \mathrm { s }$ . The mass is initially at rest in static equilibrium. Plot the dynamic responses $x ( t )$ obtained using both friction models on the same plot. In addition, plot the friction force $F _ { f } ( t )$ from both simulations on the same plot. Let the total simulation time be 1.8 s and use the fixed-step, fourth-order Runge–Kutta solver (ode4) with a step size of 0.001 s. On the basis of your simulation results describe the differences between the responses with the two friction models.

6.14 Figure P6.14 shows a 1-DOF model of an automotive suspension system, where mass m is one-quarter of the vehicle’s mass, and the stiffness and damper elements represent the suspension system. The displacement $x _ { \mathrm { i n } } ( t )$ is the position of the wheel/axle assembly, and it is considered to be the known input to the system. Displacement of mass m is measured from its static equilibrium position. The system parameters are $m = 1 1 0 0 \mathrm { k g } , k = 6 5 , 0 0 0 \mathrm { N / m }$ , and the damper force of the shock absorber is modeled by the nonlinear equation

$$F _ {d} = \frac {4 5 0 0 \dot {z}}{\sqrt {\dot {z} ^ {2} + v ^ {2}}} \quad (\mathrm{inN})$$

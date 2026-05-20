# Engineering Applications

10.24 Figure P10.24 shows a closed-loop control system for the pneumatic servomechanism [8] studied in Problems 6.24 and 9.26. This highly nonlinear system has been linearized about a nominal pressure, volume, and mid-point piston position (x = 0) to produce the transfer function $G _ { P } ( s )$ for the pneumatic servo:

$$\text { Pneumatic servo: } \quad G _ {P} (s) = \frac {7 . 0 0 3 (1 0 ^ {6})}{s (s ^ {2} + 2 8 . 3 s + 1 5 , 8 9 0)} = \frac {X (s)}{U (s)}$$

where x(t) is the position of the piston/load mass (in meters) and u(t) is the position of the spool valve (in meters). See Problems 6.24 and 9.26 for a diagram of the pneumatic servo. An electromechanical solenoid is used to actuate the valve position u(t). Because the response of the solenoid–valve combination is so much faster than the pneumatic servo, we can replace it with a constant gain $K _ { V } = 2 . 2 ( 1 0 ^ { - 4 } )$ ) m/V.

a. Plot the root locus using MATLAB if the controller is a simple gain, i.e., $G _ { C } ( s ) = K _ { P }$ . Use the root locus to show that a P-controller does not provide much flexibility for obtaining a good closed-loop response.   
b. Use MATLAB’s rlocus and/or rlocfind commands to compute the maximum gain $K _ { P }$ that results in a marginally stable closed-loop system.

c. Suppose the controller gain setting is $G _ { C } ( s ) = K _ { P } = 1 0 \mathrm { V / m }$ . Compute the steady-state error for the ramp input $x _ { \mathrm { r e f } } ( t ) = 0 . 0 0 8 t \ : \mathrm { m }$ .   
d. Plot the root locus if we use the PD controller $G _ { C } ( s ) = K ( s + 5 )$ . Has inserting the PD controller changed either the closed-loop stability or closed-loop damping when compared to the P-controller? Explain.   
e. A standard control scheme for pneumatic servomechanisms is the “position–velocity–acceleration” (PVA) controller, which has the form $G _ { C } ( s ) = K _ { a } s ^ { 2 } + K _ { \nu } s + K _ { P }$ (see Reference 8). Use MATLAB to plot the root locus using the PVA controller $G _ { C } ( s ) = K ( s ^ { 2 } + 3 0 s + 2 0 0 )$ . How has the PVA control scheme changed the stability and damping of the closed-loop system compared to the P- and PD controllers?

![](image/14c79d16948c580154e7883c7305d9611f3bfb35ff3bb3c7ac944f85d8aaa81f.jpg)

<details>
<summary>flowchart</summary>

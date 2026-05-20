# MATLAB Problems

8.9 Rework parts (a), (b), (c), (f), (i), and (j) of Problem 8.1 using MATLAB’s residue command to compute the residues of the partial-fraction expansion and then determine the inverse Laplace transform in order to find y(t).   
8.10 Rework all parts (a)– (j) of Problem 8.1 using MATLAB’s Symbolic Math Toolbox command ilaplace to directly compute y(t).   
8.11 Use MATLAB’s residue or ilaplace command to obtain the capacitor voltage response $e _ { C } ( t )$ for the RC circuit described in Problem 8.6.   
8.12 Use MATLAB’s residue or ilaplace command to obtain the angular velocity response ??(t) of the single-disk mechanical system described in Problem 8.7.   
8.13 Use MATLAB’s residue or ilaplace command to obtain the charge response q(t) of the RLC circuit described in Problem 8.8.   
8.14 A simple 1-DOF mechanical system has the following transfer function:

$$G (s) = \frac {Y (s)}{U (s)} = \frac {0 . 2 5}{s ^ {2} + 2 s + 1 0}$$

where position y(t) is in m. The system is initially at rest, $y ( 0 ) = \dot { y } ( 0 ) = 0$ , and the applied force is a step function $u ( t ) = 4 U ( t ) \mathrm { N } .$ .

a. Determine the system response using Laplace methods.   
b. Use MATLAB or Simulink to verify your analytical answer in part (a) and plot the analytical and numerical solutions on the same plot.

8.15 Repeat Problem 8.14 with the following initial conditions: y(0) = −0.04 m and ẏ (0) = 0.01 m/s. The input force is a 4-N step function.

8.16 Figure P8.16 shows a mass–damper system (no stiffness). Displacement x is measured from an equilibrium position where the damper is at the “neutral” position. The external force $f _ { a } ( t )$ is an impulse with weight 0.1 N-s, or $f _ { a } ( t ) = 0 . 1 \delta ( t )$ N. The system parameters are mass m = 0.5 kg and viscous friction coefficient $b = 3 ~ \mathrm { N - s / m }$ and the system is initially at rest.

![](image/ab94bff2f1c2f2352e098a3968d9e08088da2a2aa84c21bd4eb0975f5bba81d8.jpg)

<details>
<summary>text_image</summary>

f_a(t)
m
x
b
</details>

Figure P8.16

a. Determine the impulse response x(t) using Laplace transform methods.   
b. Use MATLAB or Simulink to verify your answer in part (a). Plot x(t).

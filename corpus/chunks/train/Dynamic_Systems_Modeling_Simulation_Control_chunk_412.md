7.21 Use MATLAB or Simulink to verify your sketch of the RC circuit response in Problem 7.6. Plot output voltage $e _ { O } ( t )$ .   
7.22 A simple 1-DOF mechanical system has the following transfer function

$$G (s) = \frac {Y (s)}{U (s)} = \frac {0 . 2 5}{s ^ {2} + 2 s + 9}$$

where the position of the mass y(t) is in meters. The system is initially at rest, $y ( 0 ) = \dot { y } ( 0 ) = 0$ , and the applied force is a step function $u ( t ) = 4 \mathrm { N }$ .

a. Accurately sketch the system response y(t) and label all important performance criteria on your sketch.   
b. Use MATLAB or Simulink to verify your sketch in part (a). Plot y(t) from the numerical solution.

7.23 Repeat Problem 7.22 with the following initial conditions and input function: $y ( 0 ) = 0 . 0 4 \mathrm { m } , \dot { y } ( 0 ) = 0$ , and zero input force u(t) = 0 for t ≥ 0.   
7.24 Figure P7.24 shows a simple 1-DOF, frictionless, rotational mechanical system. The disk moment of inertia is $\mathbf { \bar { \sigma } } _ { J } = 0 . 2 \mathrm { k g } \mathbf { - } \mathrm { m } ^ { 2 }$ and the torsional spring constant for the shaft is k = 100 N-m/rad. Angular displacement ?? is zero when the shaft is untwisted. The disk is initially at rest (equilibrium) when the sinusoidal input torque $T _ { \mathrm { i n } } ( t ) = 0 . 5$ sin 3t N-m is applied.

![](image/659c60cd338bf881069509954d141fcbe8807fcc80931fd29ef71975342efbfe.jpg)

<details>
<summary>text_image</summary>

Torque, T_in(t)
Disk, J
θ
Flexible
shaft, k
</details>

Figure P7.24

a. Determine the general form for the complete response ??(t) (you do not have to compute the exact solution with numerical values for the coefficients).   
b. Use MATLAB or Simulink to obtain a numerical solution and plot ??(t) (use a simulation time of 10 s). Does the numerical solution match the general form of the analytical solution from part (a)? Explain your answer.

7.25 Consider again the impulse response shown by Fig. P7.11 for Problem 7.11. Develop a simple linear model of the mechanical system using the approximate values for damping ratio ?? and undamped natural frequency $\omega _ { n }$ that were determined in Problem 7.11 (the mass is 0.2 kg). Use Simulink to simulate the impulse response, and adjust the magnitude and duration of the pulse input force (i.e., impulse) in order to match Fig. P7.11. What is the “strength” or “weight” of the impulse?

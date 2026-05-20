# MATLAB Problems

9.14 Use MATLAB’s abs and angle commands to compute the magnitude and phase angle of the sinusoidal transfer function in Problem 9.2 with input frequency ?? = 2 rad/s. Verify your answer using MATLAB’s bode command to compute the magnitude and phase angle for this input frequency.   
9.15 Use MATLAB to plot the Bode diagram for the 1-DOF mechanical system in Problem 9.11 (Fig. P9.11). Estimate the frequency response for the position input $x _ { \mathrm { i n } } ( t ) = 0 . 0 4$ sin 50t m by reading the Bode diagram (indicate the frequency response parameters on the plot of the Bode diagram). Obtain a more accurate answer by using MATLAB’s bode command with left-hand-side arguments for computing magnitude and phase angle.

9.16 Use MATLAB to plot the Bode diagram of the 1-DOF mechanical system in Problem 9.11 and estimate the bandwidth, resonant frequency, and peak transmissibility.   
9.17 Use MATLAB or Simulink to simulate the mechanical system in Problem 9.11 for the position input $x _ { \mathrm { i n } } ( t ) = 0$ .04 sin 50t m. Assume that the system is initially at rest at time $t = 0$ . Plot mass position x(t) and input $x _ { \mathrm { i n } } ( t )$ on the same plot and determine the frequency-response equation for $x _ { \mathrm { s s } } ( t )$ from the simulation results.   
9.18 Use MATLAB to verify the solutions to Problem 9.13 and the 1-DOF mechanical system shown in Fig. P9.13: (a) the frequency response $x _ { \mathrm { s s } } ( t )$ given the input $f _ { a } ( t ) = 2$ sin 8t N, and (b) the frequency ?? that results in the maximum amplitude of the frequency response.   
9.19 Use MATLAB to plot two Bode diagrams for the vibration isolation system described in Problem 9.13 and Fig. P9.13. The first Bode diagram is for the transfer function $G _ { 1 } ( s ) = X ( s ) / F _ { a } ( s )$ where the output is mass displacement x(t). The second Bode diagram is for the transfer function $G _ { 2 } ( s ) = F _ { T } ( s ) / F _ { a } ( s )$ ) where the output is the force transmitted to the base, $f _ { T } ( t )$ .

[Hint: Relate the transmitted force to the displacement and motion of mass m and use transfer function $G _ { 1 } ( s )$ to derive transfer function $G _ { 2 } ( s ) .$ ]

Compare the resonant frequencies and bandwidths of the two Bode diagrams. In addition, use the Bode diagrams to estimate the steady-state amplitudes of the displacement and transmitted force at very low input frequencies. Do these low-frequency results make sense intuitively? Explain your answer.

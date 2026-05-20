6.7 Write a MATLAB script (M-file) that executes the Simulink simulation for the mechanical system in Problem 6.6 for input frequencies ranging from ?? = 1 rad/s (0.16 Hz) to ?? = 100 rad/s (15.92 Hz) in increments of 1 rad/s. Store the ratios of the output/input amplitudes but use only the last one-third of the simulation response data (the so-called steady-state response) for each input frequency [Hint: to do this, compute the ratio $x _ { \mathrm { { e n d } } } / x _ { \mathrm { { i n } } }$ by using the command max(x\_end) $/ \mathrm { { m a x } ( \mathbf { x } \_ i n ) }$ ) where x\_end is the last one-third of the system response x(t)]. Plot the output/input amplitude ratio vs. input frequency, and based on your plot, summarize how the mechanical system’s displacement response x(t) varies with input frequency ??. This problem is an example of a system’s frequency response, where the system input is a periodic function (such as a sinusoidal input function).   
6.8 An RLC circuit with a parallel bypass resistor (Problems 3.10 and 5.11) is shown in Fig. P6.8. At time t = 0 the circuit has zero current in both loops and the capacitor C has a stored charge of 0.01 C. The system parameters are R = 0.4 Ω, R = 0.2 Ω, C = 0.04 F, and $L = 0 . 0 1$ H. Use Simulink to obtain the system response where the source voltage is a sinusoidal function, $e _ { \mathrm { i n } } ( t ) = 0 . 5$ sin 10t V. A voltmeter is used to measure the voltage across the capacitor C. Plot Simulink’s prediction of the voltmeter output for a simulation time of 1.5 s.

![](image/cdf375d09958bbbfcfdcf9669d31ec9effcf42d0dcf7a2b1f4c9321db9386916.jpg)

<details>
<summary>text_image</summary>

R₁
R₂ L
eᵢₙ(t) C
+ -
</details>

Figure P6.8

6.9 Use the MATLAB command lsim to obtain the voltage response for the system in Problem 6.8.   
6.10 A series RL circuit with a nonlinear inductor is shown in Fig. P6.10. Recall that the following nonlinear function for inductor current was used in Problem 3.11 in Chapter 3

$$I _ {L} (\lambda) = 9 7. 3 \lambda^ {3} + 4. 2 \lambda \quad (\text { amps, A })$$

where ?? is the flux linkage. Use Simulink to obtain the dynamic response for current $I _ { L } ( t )$ if the source voltage is a 4-V step function, that is, $e _ { \mathrm { i n } } ( t ) = 4 U ( t ) \mathrm { V } .$ The RL circuit has zero energy stored at time $t = 0$ and the resistance is $R = 1 . 2 \Omega$ . Plot current $I _ { L }$ vs. time.

![](image/1f269fcafc893f8c331b4071e847671d41835226b0a048289f55273797580507.jpg)

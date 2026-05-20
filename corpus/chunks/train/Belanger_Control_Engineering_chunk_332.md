# Example 6.8 (dc Servo)

In Example 6.2, the dc servo of Example 2.1 (Chapter 2) was shown to have a dc steady-state error to a unit load torque of -2.000/k, with pure-gain feedback. The Root Locus design of Example 5.6 sets k at 0.657 to satisfy dynamics specifications. Modify the design, using a lag compensator, so that the dc steady-state error to a load torque of 0.01 Nm is $0.5^{\circ}$ (= .00875 rad) in magnitude.

Solution A Bode plot of the loop gain with $k = 0.657$ shows that the crossover frequency is $\omega_{c} = 1.030 \, \mathrm{rad/s}$ , with a phase margin of $64.2^{\circ}$ . To meet the specification,

$$\left| e _ {s s} \right| = \frac {2 . 0 0}{k _ {0}} (. 0 1) = . 0 0 8 7 5$$

or

$$k _ {0} = 2. 2 8.$$

Clearly, the pure-gain controller with k = 0.657 cannot meet the requirement. If the dc gain is to be 2.28, the lag compensator dc gain must be

$$k _ {0} = G _ {c} (j 0) = 2. 2 8 /. 6 5 7 = 3. 4 7.$$

From Equation 6.29,

$$
\begin{array}{l} k _ {1} = k _ {0} - 1 \\ = 3. 4 7 - 1 = 2. 4 7. \\ \end{array}
$$

The value of $a \ll 1$ is to be selected so as not to cause appreciable changes in the stability margin. Some trial and error may be necessary. With a = 0.1, from Equation 6.30,

$$
\begin{array}{l} T = \frac {1}{1 . 0 3 0} \sqrt {\frac {2 . 4 7 ^ {2}}{. 0 1} - 1} \\ \approx \frac {1}{1 . 0 3 0} \frac {2 . 4 7}{. 1} = 2 4. 0 \mathrm{s}. \\ \end{array}
$$

From Equation 6.28, the complete compensator, including the original gain of 0.657, is

$$G _ {c} (s) = 2. 2 8 \frac {6 . 9 2 s + 1}{2 4 . 0 s + 1}.$$

The new phase margin is $58.4^{\circ}$ , and the crossover is 1.039 rad/s. Figure 6.19 (MATLAB step) shows closed-loop responses to a step load torque of -0.01 Nm with and without the lag compensator, and Figure 6.20 shows the response to a unit step in the set point $\theta_{d}$ for the compensated system.

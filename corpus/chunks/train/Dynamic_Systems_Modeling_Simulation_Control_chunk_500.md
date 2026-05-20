# Example 9.8

Consider again the 1-DOF rotational mechanical system presented in Fig. 9.9 (Example 9.3). Compute the resonant frequency $\omega _ { r }$ and use the Bode diagram to determine the frequency response for a sinusoidal input torque $T _ { \mathrm { i n } } ( t ) = 1 . 5$ sin 18t N-m.

Recall that the transfer function of the rotational mechanical system is

$$G (s) = \frac {1}{0 . 2 s ^ {2} + 1 . 6 s + 6 5} = \frac {\Theta (s)}{T _ {\mathrm{in}} (s)} \tag {9.53}$$

We can express Eq. (9.53) in the standard form for a second-order system

$$G (s) = \frac {5}{s ^ {2} + 8 s + 3 2 5}$$

Clearly, the DC gain is 5∕325 = 0.0154, or −36.3 dB. It is important to note that the DC gain is a small value because the system transfer function relates the torque input to the angular displacement, and hence a constant 1 N-m torque input will result in a 0.0154 rad angular deflection at steady state. We see that the undamped natural frequency is $\omega _ { n } = { \sqrt { 3 2 5 } } = 1 8 . 0 2 7 8$ rad/s and the damping ratio is $\zeta = 0 . 2 2 1 9$ . Using Eq. (9.52) the resonant frequency is

$$\omega_ {r} = \omega_ {n} \sqrt {1 - 2 \zeta^ {2}} = 1 7. 1 1 7 2 \mathrm{rad/s}$$

The frequency response of the mechanical system with an input amplitude of 1.5 N-m and input frequency ?? = 18 rad/s is

$$\theta_ {\mathrm{ss}} (t) = | G (j 1 8) | 1. 5 \sin (1 8 t + \phi) \tag {9.54}$$

We can use MATLAB to construct the Bode diagram of the second-order mechanical system, and the resulting diagram is shown in Fig. 9.26. Note that the low-frequency asymptote is about −36 dB and the resonant peak occurs at a frequency of about 17 rad/s, which match our previous calculations. The magnitude and phase at the input frequency ?? = 18 rad/s are shown on the respective plots in Fig. 9.26, and their exact values can be computed using the MATLAB bode command:

![](image/2c8ccad078dcddac4cadb01d4b5194b3ef483e47d6ed13dfe3f0604a72db6019.jpg)  
Figure 9.26 Bode diagram of the rotational mechanical system (Example 9.8).

>> sysG = tf(5, [1 8 325 ]) % create transfer function G(s)
>> w = 18; % desired input frequency, rad/s
>> [mag, phase] = bode(sysG, w) % compute exact |G(j18)| and ∠G(j18)
>> magdB = 20*log10 (mag) % compute magnitude in decibels

Converting the Bode-plot magnitude of −29.2 dB to an absolute-value magnitude and phase angle to radians, we obtain G( j18) = 0.0347 and ?? = −1.5639 rad, respectively. Hence, the frequency response (9.54) becomes

$$\theta_ {\mathrm{ss}} (t) = 0. 0 5 2 1 \sin (1 8 t - 1. 5 6 3 9) \mathrm{rad}$$

which is the same result obtained in Example 9.3. In summary, the mechanical system in this example is essentially being driven at its undamped natural frequency $\omega _ { n } .$ , which is slightly higher than its resonant frequency of 17.12 rad/s. The frequency response and resonant frequency are relatively easy to compute if an accurate Bode diagram is available.

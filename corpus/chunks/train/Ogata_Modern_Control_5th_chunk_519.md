Noting that the addition of a lag compensator modifies the phase curve of the Bode diagram, we must allow $5 ^ { \circ }$ to $1 2 ^ { \circ }$ to the specified phase margin to compensate for the modification of the phase curve.Since the frequency corresponding to a phase margin of $4 0 ^ { \circ }$ is 0.7 radsec, the new gain crossover frequency (of the compensated system) must be chosen near this value. To avoid overly large time constants for the lag compensator,we shall choose the corner frequency $\omega = 1 / T$ (which corresponds to the zero of the lag compensator) to be 0.1 radsec. Since this corner frequency is not too far below the new gain crossover frequency,the modification in the phase curve may not be small.Hence,we add about $1 2 ^ { \circ }$ to the given phase margin as an allowance to account for the lag angle introduced by the lag compensator.The required phase margin is now $5 2 ^ { \circ }$ .The phase angle of the uncompensated open-loop transfer function $\mathrm { i } \mathrm { s } - 1 2 8 ^ { \circ }$ at about $\omega = 0 . 5 \mathrm { r a d / s e c }$ . So we choose the new gain crossover frequency to be 0.5 radsec.To bring the magnitude curve down to 0 dB at this new gain crossover frequency,the lag compensator must give the necessary attenuation, which in this case is –20 dB. Hence,

$$2 0 \log {\frac {1}{\beta}} = - 2 0$$

or

$$\beta = 1 0$$

The other corner frequency $\omega = 1 ( \beta T )$ , which corresponds to the pole of the lag compensator, is then determined as

$$\frac {1}{\beta T} = 0. 0 1 \mathrm{rad/sec}$$

Thus, the transfer function of the lag compensator is

$$G _ {c} (s) = K _ {c} (1 0) \frac {1 0 s + 1}{1 0 0 s + 1} = K _ {c} \frac {s + \frac {1}{1 0}}{s + \frac {1}{1 0 0}}$$

Since the gain K was determined to be 5 and $\beta$ was determined to be 10, we have

$$K _ {c} = \frac {K}{\beta} = \frac {5}{1 0} = 0. 5$$

The open-loop transfer function of the compensated system is

$$G _ {c} (s) G (s) = \frac {5 (1 0 s + 1)}{s (1 0 0 s + 1) (s + 1) (0 . 5 s + 1)}$$

The magnitude and phase-angle curves of $G _ { c } ( j \omega ) G ( j \omega )$ are also shown in Figure 7–104.

The phase margin of the compensated system is about 40°, which is the required value. The gain margin is about 11 dB, which is quite acceptable. The static velocity error constant is $5 \sec ^ { - 1 }$ , as required. The compensated system, therefore, satisfies the requirements on both the steady state and the relative stability.

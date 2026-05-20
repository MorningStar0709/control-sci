# Example 8.2 Sampled approximations of transfer function

Consider a continuous-time system with the transfer function

$$G (s) = \frac {(s + 1) ^ {2} (s ^ {2} + 2 s + 4 0 0)}{(s + 5) ^ {2} (s ^ {2} + 2 s + 1 0 0) (s ^ {2} + 3 s + 2 5 0 0)}$$

Let $H(z)$ be the pulse-transfer function representing the algorithm in Fig. 8.1. The transmission properties of the digital filter in Fig. 8.1 depend on the nature of the D-A converter. If it is assumed that the converter keeps the output constant between the sampling periods, the transmission properties of the filter are described by

$$\hat {G} (s) = \frac {1}{s h} (1 - e ^ {- s h}) H (e ^ {s h})$$

where the pulse-transfer function H depends on the approximation used. Figure 8.4 shows Bode diagrams of H for the different digital filters obtained by step equivalence, ramp equivalence, and Tustin's method. The sampling period is 0.03 s in all cases. This implies that the Nyquist frequency is 105 rad/s. All methods except Tustin's give a good approximation of the amplitude curve. The frequency distortion by Tustin's method is noticeable at the notch at 20 rad/s and very clear at the resonance at 50 rad/s.

The step-equivalence method gives a noticeable phase error. This corresponds approximately to a time delay of half a sampling interval. Ramp equivalence gives a negligible phase error. The phase curve for Tustin's approximation also deviates because of the frequency warping. Notice that all approximations suffer from the time delay due to the sample and hold. Ramp equivalence gives the best approximation of both amplitude and phase.

![](image/e15599d2f31dfa362a184d4c43b7dc890e3edc686c7945928dd6c71492413895.jpg)  
Figure 8.4 Bode diagrams of a continuous-time transfer function $G(s)$ and different sampled approximations $H(e^{sh})$ , continuous-time transfer function (solid), ramp invariance (dashed-dotted), step invariance (dashed), and Tustin's approximation (dotted).

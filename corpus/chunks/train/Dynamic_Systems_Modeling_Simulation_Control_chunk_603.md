| Frequency, ω, rad/s | Magnitude, dB (PD controller) | Magnitude, dB (Lead controller) | Phase, deg (PD controller) | Phase, deg (Lead controller) |
| --- | --- | --- | --- | --- |
| 0.1 | ~0 | ~0 | ~0 | ~0 |
| 1 | ~2 | ~3 | ~10 | ~5 |
| 10 | ~10 | ~8 | ~60 | ~30 |
| 100 | ~30 | ~10 | ~90 | ~20 |
| 1000 | ~50 | ~10 | ~90 | ~0 |
</details>

Figure 10.47 Bode diagrams of PD controller transfer function 0.25(s + 4) and lead-controller transfer function 3.75(s + 4)∕(s + 15).

The control gains K and $K _ { 1 }$ for the PD and lead controllers have been selected so that both controllers have unity DC gains and hence they both exhibit a low-frequency magnitude of 0 dB, as shown in Fig. 10.47. Because both controllers have a zero at s = −4, both phase plots exhibit an increase in phase (“phase lead”) at frequencies near 4 rad/s. The lead controller’s pole at s = −15 contributes phase lag as frequency approaches 15 rad/s and hence the lead controller’s zero/pole pair results in a net zero phase change. The corner frequency of the numerator of the lead controller is always less than the corner frequency of the denominator so that the filter introduces phase lead at low frequencies. The PD controller, on the other hand, consists of a zero only and hence the phase continually increases from zero to $+ 9 0 ^ { \circ }$ at high frequencies. Note that the zero/pole pair of the lead controller causes the high-frequency magnitude to level off at $2 0 \log _ { 1 0 } ( 3 . 7 5 ) =$ 11.48 dB. Because the PD controller’s sinusoidal transfer function is $G _ { C } ( j \omega ) = 0 . 2 5 ( j \omega + 4 )$ , its magnitude continues to increase unbounded with frequency, as shown in Fig. 10.47. The magnitude plot in Fig. 10.47 shows that a pure PD controller has the undesirable trait of greatly amplifying a feedback signal that contains high-frequency noise.

In summary, the lead controller demonstrates the desirable anticipatory characteristic of PD control as demonstrated by the positive phase lead shown in Fig. 10.47. Hence, a lead controller will add damping and reduce settling time just like a PD controller. However, unlike PD control, the lead controller does not amplify high-frequency signals. For these reasons, a lead controller (zero/pole pair) is often used instead of a pure PD controller.

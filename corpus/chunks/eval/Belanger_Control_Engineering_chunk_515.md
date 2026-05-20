Figure 8.17 shows the $H^{\infty}$ design (MATLAB hinfsyn), which clearly does not meet the specifications. This leads us to ask whether the specifications can be met at all; some may have to be relaxed, or perhaps other measurements are required.

To answer that question, we multiply both $z_{2}$ and $z_{3}$ and the measurement noise by 0.0001. In effect, we allow the transmissions to $\ell_{1}$ and u to be $10^{4}$ times larger than specified. The results of the design are shown in Figures 8.18a and b and prove that, by relaxing the specifications and using a very low-noise measurement, the acceleration specification is indeed feasible. Note that the transmission that comes closest to violating the 0-db maximum is that from n to a; all others are well below the limit. This is an indication that the critical element may be the measurement noise rather than the actuator amplitude u or the spring extension $\ell_{1}$ .

By trial and error, we tighten the constraints. The final design has $z_{2}$ (pertaining to $\ell_{1}$ ) as originally defined, $z_{3}$ (pertaining to u) multiplied by 0.01, and the noise n multiplied by $10^{-5}$ , as opposed to the original 0.01. Results are shown in Figures 8.19a and b. The graphs show that, indeed, the measurement will have to be very fine—unless, that is, the spectrum of n falls off rapidly beyond about 10 rad/s. The actuator will be called upon to supply more force than originally expected, especially near 8 to 10 rad/s.

Figure 8.20 shows the quantity $\left|\frac{0.5}{j\omega}T_{\gamma ga}(j\omega)\right|$ and the TACV specification against which it is to be compared. The design is seen to meet the objectives, although barely.

![](image/2f8c762c19e639afed1376192973a73a50e319e8eef6462f5aa76ba80333734c.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | w to a (dB) | w to u (dB) | w to ℓ₁ (dB) |
| --- | --- | --- | --- |
| 0.1 | -110 | -105 | -140 |
| 1 | -80 | -90 | -140 |
| 10 | -20 | -60 | -150 |
| 100 | -10 | -80 | -170 |
| 1000 | -30 | -100 | -190 |
</details>

Figure 8.18a and b Weighted transmissions, reduced constraints

![](image/30c018e4f90afb6054ee9f17417928b81d5dd693fa8aaffa13673158cce13fc1.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | n to a (dB) | n to u (dB) | n to ℓ₁ (dB) |
| --- | --- | --- | --- |
| 10⁻¹ | -70 | -180 | -180 |
| 10⁰ | -65 | -185 | -185 |
| 10¹ | -50 | -150 | -170 |
| 10² | -30 | -120 | -140 |
| 10³ | -20 | -100 | -120 |
</details>

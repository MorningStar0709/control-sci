<details>
<summary>line</summary>

| ω | φ |
| --- | --- |
| 0.01/T | 0° |
| 0.1/T | 0° |
| 1/T | 45° |
| 10/T | 90° |
</details>

Quadratic Factors $[ 1 ~ + ~ 2 \zeta ( j \omega / \omega _ { n } ) ~ + ~ ( j \omega / \omega _ { n } ) ^ { 2 } ] ^ { \mp 1 }$ . Control systems often possess quadratic factors of the form

$$G (j \omega) = \frac {1}{1 + 2 \zeta \left(j \frac {\omega}{\omega_ {n}}\right) + \left(j \frac {\omega}{\omega_ {n}}\right) ^ {2}} \tag {7-7}$$

If $\zeta > 1$ , this quadratic factor can be expressed as a product of two first-order factors with real poles. If $0 < \zeta < 1$ , this quadratic factor is the product of two complexconjugate factors.Asymptotic approximations to the frequency-response curves are not accurate for a factor with low values of $\zeta .$ . This is because the magnitude and phase of the quadratic factor depend on both the corner frequency and the damping ratio $\zeta .$ .

The asymptotic frequency-response curve may be obtained as follows: Since

$$2 0 \log \left| \frac {1}{1 + 2 \zeta \left(j \frac {\omega}{\omega_ {n}}\right) + \left(j \frac {\omega}{\omega_ {n}}\right) ^ {2}} \right| = - 2 0 \log \sqrt {\left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) ^ {2} + \left(2 \zeta \frac {\omega}{\omega_ {n}}\right) ^ {2}}$$

for low frequencies such that $\omega \ll \omega _ { n }$ , the log magnitude becomes

$$- 2 0 \log 1 = 0 \mathrm{dB}$$

The low-frequency asymptote is thus a horizontal line at 0 dB. For high frequencies such that $\omega \gg \omega _ { n }$ , the log magnitude becomes

$$- 2 0 \log \frac {\omega^ {2}}{\omega_ {n} ^ {2}} = - 4 0 \log \frac {\omega}{\omega_ {n}} \mathrm{dB}$$

The equation for the high-frequency asymptote is a straight line having the slope –40 dBdecade, since

$$- 4 0 \log \frac {1 0 \omega}{\omega_ {n}} = - 4 0 - 4 0 \log \frac {\omega}{\omega_ {n}}$$

The high-frequency asymptote intersects the low-frequency one at $\omega = \omega _ { n }$ , since at this frequency

$$- 4 0 \log \frac {\omega_ {n}}{\omega_ {n}} = - 4 0 \log 1 = 0 \mathrm{dB}$$

This frequency, $\omega _ { n } \mathrm { . }$ , is the corner frequency for the quadratic factor considered.

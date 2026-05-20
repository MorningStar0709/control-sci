$$\underline {{\sigma}} [ P ^ {- 1} (j \omega) ] = \frac {1}{\overline {{\sigma}} [ P (j \omega) ]} \gg 1$$

Similarly, the controller gain, ${ \overline { { \sigma } } } ( K )$ , should also be kept not too large in the frequency range where the loop gain is small in order not to saturate the actuators. This is because for small loop gain $\overline { { \sigma } } ( L _ { o } ( j \omega ) ) \ll 1$ or $\overline { { \sigma } } ( L _ { i } ( j \omega ) ) \ll 1$

$$u = K S _ {o} (r - n - d) - T _ {i} d _ {i} \approx K (r - n - d)$$

Therefore, it is desirable to keep $\overline { { \sigma } } ( K )$ not too large when the loop gain is small.

To summarize the above discussion, we note that good performance requires in some frequency range, typically some low-frequency range $( 0 , \omega _ { l } )$ ,

$$\underline {{\sigma}} (P K) \gg 1, \underline {{\sigma}} (K P) \gg 1, \underline {{\sigma}} (K) \gg 1$$

and good robustness and good sensor noise rejection require in some frequency range, typically some high-frequency range $( \omega _ { h } , \infty )$ ,

$$\overline {{\sigma}} (P K) \ll 1, \overline {{\sigma}} (K P) \ll 1, \overline {{\sigma}} (K) \leq M$$

where M is not too large. These design requirements are shown graphically in Figure 6.2. The specific frequencies ωl and $\omega _ { h }$ depend on the specific applications and the knowledge one has of the disturbance characteristics, the modeling uncertainties, and the sensor noise levels.

![](image/7fe51d01b79684df6253a410158e4f7fb5d1bad9b316e5f44fc42176582f300b.jpg)

<details>
<summary>text_image</summary>

σ̅(L)
ω₁
ωₕ
log ω
σ̅(L)
</details>

Figure 6.2: Desired loop gain

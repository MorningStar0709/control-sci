Motivated from these observations, we will focus for the moment on the multiplicative description of uncertainty. We will assume that $P _ { \Delta }$ in equation (8.2) remains a strictly proper FDLTI system for all ∆. More general perturbations (e.g., time varying, infinite dimensional, nonlinear) can also be covered by this set provided they are given appropriate “conic sector” interpretations via Parseval’s theorem. This connection is developed in [Safonov, 1980] and [Zames, 1966] and will not be pursued here.

When used to represent the various high-frequency mechanisms mentioned previously, the weighting functions in equation (8.2) commonly have the properties illustrated in Figure 8.2. They are small ( 1) at low frequencies and increase to unity and above at higher frequencies. The growth with frequency inevitably occurs because phase uncertainties eventually exceed ±180 degrees and magnitude deviations eventually exceed the nominal transfer function magnitudes. Readers who are skeptical about this reality are encouraged to try a few experiments with physical devices.

![](image/11f8d0c2c372702a1d77bfe11de135b703352925b6643d41f8b4b8b2fe4fd26c.jpg)

<details>
<summary>text_image</summary>

nominal model
log ω
actual model
</details>

Figure 8.2: Typical behavior of multiplicative uncertainty: $p _ { \delta } ( s ) = [ 1 + w ( s ) \delta ( s ) ] p ( s )$

Also note that the representation of uncertainty in equation (8.2) can be used to include perturbation effects that are in fact certain. A nonlinear element may be quite accurately modeled, but because our design techniques cannot effectively deal with the nonlinearity, it is treated as a conic sector nonlinearity.1 As another example, we may deliberately choose to ignore various known dynamic characteristics in order to achieve a simple nominal design model. One such instance is the model reduction process discussed in the last chapter.

Example 8.1 Let a dynamical system be described by

$$P (s, \alpha , \beta) = \frac {1 0 ((2 + 0 . 2 \alpha) s ^ {2} + (2 + 0 . 3 \alpha + 0 . 4 \beta) s + (1 + 0 . 2 \beta))}{(s ^ {2} + 0 . 5 s + 1) (s ^ {2} + 2 s + 3) (s ^ {2} + 3 s + 6)}, \quad \alpha , \beta \in [ - 1, 1 ]$$

Then for each frequency, all possible frequency responses with varying parameters α and $\beta$ are in a box, as shown in Figure 8.3. We can also obtain an unstructured uncertainty bound for this system. In fact, we have

Figure 7–29 Polar plot showing the resonant peak and resonant frequency $\omega _ { r }$ .   
![](image/2428d94b89e7851dc0c8fde0be4ec77c573f9c13dc160fa8ea71ad745a7913f3.jpg)

<details>
<summary>text_image</summary>

Im
ω = ∞
ω = 0
0
Re
Resonant
peak
ωₙ
ωᵣ
</details>

Figure 7–30

Polar plot of

$$1 + 2 \zeta \left(j \frac {\omega}{\omega_ {n}}\right) + \left(j \frac {\omega}{\omega_ {n}}\right) ^ {2} \text { for } \zeta > 0.$$

![](image/eb84aeae84f6a2da0ee2a486fc691e2ef36df5fbd4281b1f8420c688998a095c.jpg)

<details>
<summary>text_image</summary>

Im
∞
ω
ω = 0
0
1
Re
</details>

Next, consider the following sinusoidal transfer function:

$$
\begin{array}{l} G (j \omega) = 1 + 2 \zeta \left(j \frac {\omega}{\omega_ {n}}\right) + \left(j \frac {\omega}{\omega_ {n}}\right) ^ {2} \\ = \left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right) + j \left(\frac {2 \zeta \omega}{\omega_ {n}}\right) \\ \end{array}
$$

The low-frequency portion of the curve is

$$\lim _ {\omega \rightarrow 0} G (j \omega) = 1 \angle 0 ^ {\circ}$$

and the high-frequency portion is

$$\lim _ {\omega \rightarrow \infty} G (j \omega) = \infty \underline {{{1 8 0 ^ {\circ}}}}$$

Since the imaginary part of $G ( j \omega )$ is positive for $\omega > 0$ and is monotonically increasing, and the real part of $G ( j \omega )$ is monotonically decreasing from unity, the general shape of the polar plot of $G ( j \omega )$ is as shown in Figure 7–30. The phase angle is between $0 ^ { \circ }$ and $1 8 0 ^ { \circ }$ .

EXAMPLE 7–8 Consider the following second-order transfer function:

$$G (s) = \frac {1}{s (T s + 1)}$$

Sketch a polar plot of this transfer function.

Since the sinusoidal transfer function can be written

$$G (j \omega) = \frac {1}{j \omega (1 + j \omega T)} = - \frac {T}{1 + \omega^ {2} T ^ {2}} - j \frac {1}{\omega (1 + \omega^ {2} T ^ {2})}$$

the low-frequency portion of the polar plot becomes

$$\lim _ {\omega \rightarrow 0} G (j \omega) = - T - j \infty$$

and the high-frequency portion becomes

$$\lim _ {\omega \rightarrow \infty} G (j \omega) = 0 - j 0$$

Figure 7–31 Polar plot of 1/Cjv(1+jvT)D.   
![](image/738b7d84daa948e87e128709a4df03dd5d17cc5080596cf31fdc9ccbdd4df363.jpg)

<details>
<summary>text_image</summary>

-T
ω
ω
0
Im
∞
0
Re
</details>

If v approaches infinity, the magnitude of $G ( j \omega )$ approaches zero and the phase angle approaches –90°. The polar plot of this transfer function is a semicircle as the frequency v is varied from zero to infinity, as shown in Figure 7–26(a). The center is located at 0.5 on the real axis, and the radius is equal to 0.5.

To prove that the polar plot of the first-order factor $G ( j \omega ) = 1 / ( 1 + j \omega T )$ is a semicircle, define

$$G (j \omega) = X + j Y$$

Figure 7–26

(a) Polar plot of 1/(1+jvT); (b) plot of G(jv) in X-Y plane.

![](image/f828cac0c33f7065df82901f0f5bf94743ea363611ccc47c4b9cc6fe6c5cf4be.jpg)

<details>
<summary>text_image</summary>

Im
ω = ∞
0
ωT
1 + ω²T²
1
0.5
ω = 0
G(j₁T̅)
ωT = 1
Re
G(j₁T̅)
</details>

(a)

![](image/caf6cf9f083d9c9d730a46d8959ddef177d59a996fd101a64efcc34354c8a1da.jpg)

<details>
<summary>text_image</summary>

Y
ω →
ω = -∞
0 0.5 1 X
ω = ∞ ω = 0
ω ← ω
</details>

(b)

where

$$X = \frac {1}{1 + \omega^ {2} T ^ {2}} = \text { real part of } G (j \omega)Y = \frac {- \omega T}{1 + \omega^ {2} T ^ {2}} = \text { imaginary part of } G (j \omega)$$

Then we obtain

![](image/b8f93b6f2f056574de7df75fbb0751ba219570d5ba96393b2f28e6f4a3da8c0e.jpg)

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

Figure 7–27   
Polar plot of $1 + j \omega T .$ .

$$\left(X - \frac {1}{2}\right) ^ {2} + Y ^ {2} = \left(\frac {1}{2} \frac {1 - \omega^ {2} T ^ {2}}{1 + \omega^ {2} T ^ {2}}\right) ^ {2} + \left(\frac {- \omega T}{1 + \omega^ {2} T ^ {2}}\right) ^ {2} = \left(\frac {1}{2}\right) ^ {2}$$

Thus, in the X-Y plane $G ( j \omega )$ is a circle with center at $X = { \textstyle { \frac { 1 } { 2 } } } , Y = 0$ and with radius $\frac { 1 } { 2 }$ , as shown in Figure 7–26(b). The lower semicircle corresponds to $0 \leq \omega \leq \infty .$ , and the upper semicircle corresponds to $- \infty \leq \omega \leq 0$ .

The polar plot of the transfer function $1 + j \omega T$ is simply the upper half of the straight line passing through point (1,0) in the complex plane and parallel to the imaginary axis, as shown in Figure 7–27. The polar plot of $1 + j \omega T$ has an appearance completely different from that of $1 / ( 1 + j \omega T )$ .

Quadratic Factors $[ 1 ~ + ~ 2 \zeta ( j \omega / \omega _ { n } ) ~ + ~ ( j \omega / \omega _ { n } ) ^ { 2 } ] ^ { \mp 1 }$ . The low- and high-frequency portions of the polar plot of the following sinusoidal transfer function

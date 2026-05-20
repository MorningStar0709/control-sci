# 7–11 LEAD COMPENSATION

We shall first examine the frequency characteristics of the lead compensator. Then we present a design technique for the lead compensator by use of the Bode diagram.

Characteristics of Lead Compensators. Consider a lead compensator having the following transfer function:

$$K _ {c} \alpha \frac {T s + 1}{\alpha T s + 1} = K _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\alpha T}} \quad (0 < \alpha < 1)$$

where a is the attenuation factor of the lead compensator. It has a zero at $s = - 1 / T$ and a pole at $s = - 1 / ( \alpha T )$ . Since $0 < \alpha < 1$ , we see that the zero is always located to the right of the pole in the complex plane. Note that for a small value of a the pole is located far to the left. The minimum value of a is limited by the physical construction of the lead compensator. The minimum value of a is usually taken to be about 0.05. (This means that the maximum phase lead that may be produced by a lead compensator is about $6 5 ^ { \circ } . )$ [See Equation (7–25).]

Figure 7–91 Polar plot of a lead compensator $\alpha ( j \omega T + 1 ) / ( j \omega \alpha T + 1 ) .$ where $0 < \alpha < 1$ .   
![](image/00a5794d01885a6c2e76870a5aa8bd11416143a10443756c6156efcf2dd44462.jpg)

<details>
<summary>text_image</summary>

Im
ωm
½ (1 - α)
φm
ω = 0
ω = ∞
0
α
1
Re
½ (1 + α)
</details>

Figure 7–91 shows the polar plot of

$$K _ {c} \alpha \frac {j \omega T + 1}{j \omega \alpha T + 1} \quad (0 < \alpha < 1)$$

with $K _ { c } = 1$ . For a given value of a, the angle between the positive real axis and the tangent line drawn from the origin to the semicircle gives the maximum phase-lead angle, $\phi _ { m }$ . We shall call the frequency at the tangent point $\omega _ { m }$ . From Figure 7–91 the phase angle at $\omega = \omega _ { m } \mathrm { i s } \phi _ { m }$ , where

$$\sin \phi_ {m} = \frac {\frac {1 - \alpha}{2}}{\frac {1 + \alpha}{2}} = \frac {1 - \alpha}{1 + \alpha} \tag {7-25}$$

Equation (7–25) relates the maximum phase-lead angle and the value of a.

Figure 7–92 shows the Bode diagram of a lead compensator when $K _ { c } = 1$ and $\alpha = 0 . 1$ . The corner frequencies for the lead compensator are $\omega = 1 / T$ and $\omega = 1 / ( \alpha T ) = 1 0 / T$ . By examining Figure 7–92, we see that $\omega _ { m }$ is the geometric mean of the two corner frequencies, or

$$\log \omega_ {m} = \frac {1}{2} \left(\log \frac {1}{T} + \log \frac {1}{\alpha T}\right)$$

![](image/e8e903914aebb0670dcb5a163cf80ada5af2ff7eed3f3979dfd8fc5612a0c88c.jpg)

# 6.2.5 Stability Margins

The Nyquist plot shows the gain and the phase simultaneously. It is clear that both must be taken into account to ascertain the relationship of the Nyquist locus to the critical $(-1,0)$ point. When working with Bode plots, in particular, it is easier to have separate gain and phase conditions. The gain and phase margins, known together as the stability margins, are precisely such conditions. Figure 6.12 illustrates their definitions with a Nyquist plot corresponding to a stable closed-loop system. The gain margin is the value of gain $k$ that would cause the locus $kL(j\omega)$ to traverse the $(-1,0)$ point; it is determined from the intersection of the Nyquist plot with the negative real axis. In Figure 6.12, a gain $k = 1 / x_1 > 1$ would move point $A$ to the critical point, so there is a gain margin of $1 / x_1$ .

The phase margin is the phase lag (i.e., negative angle) that, when applied to every point of the locus $L(j\omega)$ , would cause its Nyquist locus to traverse the critical point. The phase margin is determined from the intersection of the Nyquist plot with the circle $|L(j\omega)| = 1$ , i.e., the circle of unit radius centered at the origin. In Figure 6.12, a phase lag of $\theta_{1}$ added to the locus would move point B to the critical point, so the phase margin is $\theta_{1}$ .

In some cases, there may be two gain or phase margins. Consider, for example, the Nyquist plot of Figure 6.13, for a plant with one RHP pole. For stability we must have N = -1, so the $(-1, 0)$ point must be located as shown, between $-x_{1}$ and $-x_{2}$ . A gain $k > 1/x_{2}$ could cause instability, as would $k < 1/x_{1}$ . Thus, there are two gain margins: an upper margin $1/x_{2} > 1$ , and a lower margin $1/x_{1} < 1$ .

![](image/925149b2d0609ed403f91b44e2c17d04dfc6963911197caebf7f6e0c044b791e.jpg)

<details>
<summary>text_image</summary>

-1
-x₁
A
θ₁
B
</details>

Figure 6.12 Illustrating gain and phase margins

![](image/9bb843489d3f94a6a12b95eee8f13581a3f6770e2aadaf6590a532b8b659b3c9.jpg)

<details>
<summary>text_image</summary>

-x₁
-1
-x₂
</details>

Figure 6.13 Nyquist plot of a system unit with upper and lower phase margins

![](image/138cd98efd14617be7f737aec853a3790821d485b5a913908800ea14a9c8b775.jpg)

<details>
<summary>text_image</summary>

-1
</details>

Figure 6.14 Nyquist plot showing good stability margins, but poor stability

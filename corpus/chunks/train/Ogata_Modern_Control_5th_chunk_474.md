![](image/2de11411c05dc54fbb5184617a928a2549317c36e9dd983850b6f19b43be8c52.jpg)

<details>
<summary>text_image</summary>

G Plane
Im
-1
0
Re
G(jω)
</details>

(b)

Phase and Gain Margins. Figure 7–66 shows the polar plots of $G ( j \omega )$ for three different values of the open-loop gain K. For a large value of the gain $K$ , the system is unstable.As the gain is decreased to a certain value, the $G ( j \omega )$ locus passes through the $- 1 + j 0$ point. This means that with this gain value the system is on the verge of instability, and the system will exhibit sustained oscillations. For a small value of the gain $K ,$ , the system is stable.

In general, the closer the $G ( j \omega )$ locus comes to encircling the $- 1 + j 0$ point, the more oscillatory is the system response. The closeness of the $G ( j \omega )$ locus to the $- 1 + j 0$ point can be used as a measure of the margin of stability. (This does not apply, however, to conditionally stable systems.) It is common practice to represent the closeness in terms of phase margin and gain margin.

Phase margin: The phase margin is that amount of additional phase lag at the gain crossover frequency required to bring the system to the verge of instability.The gain crossover frequency is the frequency at which $\left| G ( j \omega ) \right|$ @, the magnitude of the openloop transfer function, is unity. The phase margin $\gamma$ is $1 8 0 ^ { \circ }$ plus the phase angle $\phi$ of the open-loop transfer function at the gain crossover frequency, or

$$\gamma = 1 8 0 ^ {\circ} + \phi$$

![](image/c2971143d316d507778351644bbf37938e182403e20fb465694307c746b38e21.jpg)

<details>
<summary>line</summary>

| Re | Im (K : Large) | Im (K : Small) |
| --- | --- | --- |
| -1 | ~-0.5 | ~-0.3 |
| 0 | 0 | 0 |
</details>

Figure 7–66

Polar plots of

$$\frac {K (1 + j \omega T _ {a}) (1 + j \omega T _ {b}) \cdots}{(j \omega) (1 + j \omega T _ {1}) (1 + j \omega T _ {2}) \cdots}.$$

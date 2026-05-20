where parameter $\alpha_{1}$ is known and $\alpha_{2}$ and $k = \theta_{3} / (h^{2}\theta_{1}\theta_{2})$ are unknown.

The observation about the structure of the sampled model for small sampling periods is a consequence of a general result about how poles and zeros are transformed by sampling. If $\alpha_{i}$ is a pole of a continuous-time system, then the sampled system has a pole at $\exp(\alpha_{i}h)$ . There are no simple, exact formulas for transforming the zeros. For short sampling periods, however, a zero $\beta_{i}$ is approximately transformed to $\exp(\beta_{i}h)$ . If d is the pole excess of the continuous-time system, there will be d-1 additional zeros of the sampled system. The limiting positions of these zeros as the sampling period goes to zero are given by Theorem 6.9 in Chapter 6. In this way it is possible to use prior information in terms of poles and zeros both for continuous-time self-tuners and for discrete-time self-tuners with a short sampling period.

Example 2.18 shows that how the process model is parameterized is crucial. Different parameterizations can be attempted. This is illustrated by an example.

![](image/b64f5d7bccdce111d577d76f9f50938ee54654ab4b5b747b21ad6d70002bd881.jpg)

<details>
<summary>text_image</summary>

u
C
x₂
L
x₁
R
y
</details>

Figure 2.14 The circuit in Example 2.19.

where parameter $\alpha > 0$ is introduced to avoid difficulties when $\varphi$ is small. Notice that we have written the equation in such a way that it also holds when $\theta$ is a vector; in that case, $\varphi$ is also a vector of the same dimension.

If we repeat the analysis of the thought experiment, we find that Eq. (5.13) is replaced by

$$s + \gamma \frac {\varphi^ {o} u _ {c} ^ {o}}{\alpha + \varphi^ {o T} \varphi^ {o}} k G (s) = 0$$

Since $\varphi^{o}$ is proportional to $u_{c}^{o}$ , the roots of this equation will not change much with the signal levels. The adaptation rule given by Eq. (5.16) is called the normalized MIT rule. The improved performance with this algorithm is illustrated in Fig. 5.9. A comparison with Fig. 5.8 shows that normalization is useful.

![](image/0317c48404026d00c70a030dc63088874668c21719835e89c7695496bb9293ba.jpg)

<details>
<summary>line</summary>

| Time | y | y_m |
| --- | --- | --- |
| 0 | -0.1 | -0.1 |
| 20 | -0.1 | 0.1 |
| 40 | -0.1 | -0.1 |
| 60 | -0.1 | 0.1 |
| 80 | -0.1 | -0.1 |
| 100 | -0.1 | 0.1 |
</details>

![](image/68bd400fd5a1739935e0f9f22879c37b38b515e4af06a13aaf22901111bd0fa7.jpg)

<details>
<summary>line</summary>

| Time | y | y_m |
| --- | --- | --- |
| 0 | -0.5 | 1.0 |
| 20 | -1.0 | 1.0 |
| 40 | -1.0 | 1.0 |
| 60 | -1.0 | 1.0 |
| 80 | -1.0 | 1.0 |
| 100 | -1.0 | 1.0 |
</details>

![](image/d8a0c0c67f548519b26abc702cfbe74648ece4d03e1fc6bd22d3f802a39688c7.jpg)

<details>
<summary>line</summary>

| Time | y | y_m |
| --- | --- | --- |
| 0 | 0 | 0 |
| 20 | -5 | 5 |
| 40 | -5 | 5 |
| 60 | -5 | 5 |
| 80 | -5 | 5 |
| 100 | -5 | 5 |
</details>

Figure 5.9 Simulation of the MRAS in Example 5.5 with the normalized MIT rule. The command signal is a square wave with the amplitude (a) 0.1, (b) 1, and (c) 3.5. Compare with Fig. 5.8. The model output $y_{m}$ is a dashed line; the process output is a solid line. The parameters used are $k = a_{1} = a_{2} = \theta^{0} = 1$ , $\alpha = 0.001$ , and $\gamma = 0.1$ .

Notice that the normalized adjustment rule performs very well even in the cases in which difficulties were encountered with the MIT rule. It is in fact possible to make the modified adjustment rule work very well over a wide range of command signal amplitudes. Notice that the normalization is obtained automatically with algorithms based on parameter estimation. (Compare with Example 2.16.)

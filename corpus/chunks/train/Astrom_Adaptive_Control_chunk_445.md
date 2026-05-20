# Averaging

The command signal $u_{c}$ is the only external signal; hence $v = u_{c}$ . Furthermore, $\varphi^{T} = \left( u_{c} - y \right)$ . To obtain the averaging equations, the transfer functions $G_{ev}$ and $G_{\varphi v}$ are first calculated:

$$
\begin{array}{l} G _ {e v} = \frac {\hat {\theta} _ {1} G}{1 + \hat {\theta} _ {2} G} - G _ {m} \\ G _ {\varphi \nu} ^ {T} = \left( \begin{array}{c c} - 1 & \frac {\hat {\theta} _ {1} G}{1 + \hat {\theta} _ {2} G} \end{array} \right) \\ \end{array}
$$

By using Lemma 6.5 the averaged equations can now be written as

$$\frac {d \bar {\theta} _ {1}}{d t} = - \frac {\gamma u _ {0} ^ {2}}{2} R e \left\{\frac {\bar {\theta} _ {1} G (i \omega)}{1 + \bar {\theta} _ {2} G (i \omega)} - G _ {m} (i \omega) \right\} \tag {6.60}\frac {d \bar {\theta} _ {2}}{d t} = \frac {\gamma u _ {0} ^ {2}}{2} R e \left\{\left(\frac {\bar {\theta} _ {1} G (i \omega)}{1 + \bar {\theta} _ {2} G (i \omega)} - G _ {m} (i \omega)\right) \frac {\bar {\theta} _ {1} G (- i \omega)}{1 + \bar {\theta} _ {2} G (- i \omega)} \right\}$$

![](image/612b6acd889513c39452a95700cd1a0f83ce176bb74a0fd4003399e0976b16a0.jpg)

<details>
<summary>line</summary>

| Time | θ̂₁ | θ̂₂ |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 10 | ~1.0 | ~0.5 |
| 20 | ~1.1 | ~0.7 |
| 40 | ~1.2 | ~0.8 |
| 60 | ~1.3 | ~0.9 |
| 80 | ~1.4 | ~1.0 |
| 100 | ~1.5 | ~1.1 |
</details>

Figure 6.11 Parameter estimates and their approximation by the averaging method. The dashed lines show the equilibrium values of the gains.

![](image/70db26c6a98ad2aa086437e984e9d34aaaf2e44a11e15d0a88793cfeeae0371e.jpg)

<details>
<summary>line</summary>

| Time | y | y_m | e |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 5 | -1.0 | -1.0 | -0.5 |
| 10 | 0.0 | 0.0 | 0.0 |
| 15 | 1.0 | 1.0 | 0.0 |
| 20 | 0.0 | 0.0 | 0.0 |
</details>

![](image/e06c343cab76cf80fb474e7e920ac54c9ff656605abe7b10f778bb9d16448db7.jpg)

<details>
<summary>line</summary>

| Time | y | e |
| --- | --- | --- |
| 50 | -0.5 | 0.0 |
| 52 | 1.0 | 0.0 |
| 54 | -0.5 | 0.0 |
| 56 | -1.0 | 0.0 |
| 58 | 1.0 | 0.0 |
| 60 | -0.5 | 0.0 |
| 62 | -1.0 | 0.0 |
| 64 | 1.0 | 0.0 |
| 66 | -0.5 | 0.0 |
| 68 | -1.0 | 0.0 |
| 70 | 0.5 | 0.0 |
</details>

Figure 6.12 System output y (solid line) and the output of the reference model $y_{m}$ (dashed line) and error e for Example 6.9 for t=0–20 and t=50–70.

Notice that these equations are valid also when G is a general transfer function, that is, G does not need to satisfy Eq. (6.56).

# EXAMPLE 2.13 : Model structure

In this example, parameter c in Eq. (2.53) has the value -0.5. Figure 2.8(a) shows the estimates of parameters a and b. The estimates do not converge to their true values. This is because the equation error $e(t) + ce(t - 1)$ is not white noise. The assumptions in Theorem 2.2 are thus violated. Figure 2.8(b) shows the estimates when the extended least squares (ELS) method is used. All three parameters a, b, and c are then estimated, and the estimates converge to the true values. When only a and b are estimated by using the least-squares

![](image/97ab9cf5a4da7568a24ac60558e941b092d4a74e51a9d2984679093c2f6f62f4.jpg)

<details>
<summary>line</summary>

| Time | Ê | Ê' |
| --- | --- | --- |
| 0 | 1.0 | -1.0 |
| 200 | 0.5 | -1.0 |
| 400 | 0.5 | -1.0 |
| 600 | 0.5 | -1.0 |
| 800 | 0.5 | -1.0 |
| 1000 | 0.5 | -1.0 |
</details>

![](image/d212488c996ce7b713570bfa98c14c59d5181afac2520938b4ba1bab81880a3c.jpg)

<details>
<summary>line</summary>

| Time | a | ĉ | b̂ |
| --- | --- | --- | --- |
| 0 | -1.0 | -0.5 | 0.5 |
| 200 | -1.0 | -0.5 | 0.5 |
| 400 | -1.0 | -0.5 | 0.5 |
| 600 | -1.0 | -0.5 | 0.5 |
| 800 | -1.0 | -0.5 | 0.5 |
| 1000 | -1.0 | -0.5 | 0.5 |
</details>

Figure 2.8 Estimated parameters when the model (2.53) is simulated with c = -0.5 by using (a) LS and (b) ELS.

![](image/a16d3dbb128b27a0edb8eb8f68ad1442d52269b53bcb909243226e280f49671e.jpg)  
Figure 2.9 Estimates when the control signal is generated through feedback (a) $u(t) = -0.2y(t)$ and (b) $u(t) = -0.32y(t - 1)$ .

method, the estimates and the P-matrix at time t = 1000 are

$$
\binom {\hat {a} (1 0 0 0)} {\hat {b} (1 0 0 0)} = \binom {- 0. 7 0 2} {0. 6 9 7} \quad P (1 0 0 0) = \left( \begin{array}{c c} 0. 7 1 0 & 1. 4 3 5 \\ 1. 4 3 5 & 3. 9 0 3 \end{array} \right) \cdot 1 0 ^ {- 3}
$$

The elements in the P-matrix are small. This would indicate good accuracy if the process had fulfilled the assumptions about the noise structure. Theorem 2.2 gives the following estimates of the standard deviation of $\hat{a}$ and $\hat{b}$ :

$$
\begin{array}{l} \sigma_ {\hat {a}} = 0. 5 \sqrt {7 . 1 0} \cdot 1 0 ^ {- 2} = 0. 0 1 3 \\ \sigma_ {\tilde {b}} = 0. 5 \sqrt {3 9 . 0 3} \cdot 1 0 ^ {- 2} = 0. 0 3 1 \\ \end{array}
$$

It is thus deceptive to judge the accuracy of the estimates by only looking at the P-matrix. It is necessary that the data be generated from a model of the form (2.12) to use the P-matrix for accuracy estimates.

If we did not observe that the equation error is not white, we could thus be strongly misled. One possibility to avoid mistakes is to also compute the correlation of the equation error and check whether it is white noise. □

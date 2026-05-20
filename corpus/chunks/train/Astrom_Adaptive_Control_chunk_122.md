# EXAMPLE 2.12 Excitation

The need for persistency of excitation is illustrated in this example. A simulation of the estimates when the input is a unit pulse at t = 50 is shown in Fig. 2.7(a). The estimate $\hat{a}$ appears to converge to the correct value, but the estimate $\hat{b}$ does not. The reason for this is that information about the a parameter is obtained through the excitation by the noise. Information about the b parameter is obtained only through the pulse that is not persistently exciting.

In Fig. 2.7(b) the experiment is repeated, but the input is now a square wave of unit amplitude and a period of 100 samples. Both $\hat{a}$ and $\hat{b}$ will converge to their true values, because the input is persistently exciting. The absolute values of the elements of $P(t)$ are decreasing with time. For the simulation in

![](image/0e8f2b804c2fbd5bf18967bc1e00c35d501bfd790434bda930392be059149015.jpg)

<details>
<summary>line</summary>

| Time | ã | b̂ |
| --- | --- | --- |
| 0 | -1.0 | 0.5 |
| 200 | -1.0 | 0.5 |
| 400 | -1.0 | 0.5 |
| 600 | -1.0 | 0.5 |
| 800 | -1.0 | 0.5 |
| 1000 | -1.0 | 0.5 |
</details>

![](image/2aaf320faf026f1d57fb75c98e85cf240851a40a51e0e4eeb9b7d758e7e33318.jpg)

<details>
<summary>line</summary>

| Time | Ê | â |
| --- | --- | --- |
| 0 | 1.0 | -1.0 |
| 200 | 0.5 | -1.0 |
| 400 | 0.5 | -1.0 |
| 600 | 0.5 | -1.0 |
| 800 | 0.5 | -1.0 |
| 1000 | 0.5 | -1.0 |
</details>

Figure 2.7 The estimated (solid line) and true (dashed line) parameter values in estimating the parameters in the model (2.53). The input signal $u(t)$ is (a) a unit pulse at t = 50, (b) a unit amplitude square wave with period 100.

Fig. 2.7(b) we have

$$
\binom {\hat {a} (1 0 0 0)} {\hat {b} (1 0 0 0)} = \binom {- 0. 7 9 6} {0. 5 1 1} \quad P (1 0 0 0) = \left( \begin{array}{c c} 0. 5 5 0 & 1. 1 1 4 \\ 1. 1 1 4 & 3. 2 5 8 \end{array} \right) \cdot 1 0 ^ {- 3}
$$

According to Theorem 2.2 this implies the following standard deviations for the estimates:

$$
\begin{array}{l} \sigma_ {\hat {a}} = 0. 5 \sqrt {5 . 5 0} \cdot 1 0 ^ {- 2} = 0. 0 1 2 \\ \sigma_ {\hat {b}} = 0. 5 \sqrt {3 2 . 5 8} \cdot 1 0 ^ {- 2} = 0. 0 2 9 \\ \end{array}
$$

The estimates are thus well within one standard deviation of their true values.

□

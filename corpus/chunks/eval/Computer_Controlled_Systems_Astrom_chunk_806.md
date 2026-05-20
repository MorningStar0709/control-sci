# Example 13.4 Recursive estimation

Consider the process

$$y (k) + a y (k - 1) = b u (k - 1) + e (k)$$

with a = -0.8 and b = 0.5. The variance of the noise e is 0.25. The input signal is assumed to be a PRBS signal with amplitude ±1. The input and the output data are shown in Fig. 13.4. The recursive equations (13.10) to (13.12) have been used to estimate a and b. The estimates are shown in Fig. 13.5 when the initial values of the parameters are zero and when $P(0)$ is 10 times the unit matrix. The estimates are after a few observations close to the true values. For the data in Fig. 13.4 we have

![](image/ddea0fcb6c653ea531a39cacface313b4159365ebfc3cd3b2b7c51ead4a1369b.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 1 |
| 500 | -5 | -1 |
| 1000 | 0 | 1 |
| 1500 | -5 | -1 |
| 2000 | 0 | 1 |
| 2500 | -5 | -1 |
| 3000 | 0 | 1 |
| 3500 | -5 | -1 |
| 4000 | 0 | 1 |
| 4500 | -5 | -1 |
| 500 | 0 | 1 |
</details>

Figure 13.4 Input-output data for the process in Example 13.4.

$$
\binom {\hat {a} (5 0 0)} {\hat {b} (5 0 0)} = \binom {- 0. 7 9 9} {0. 5 1 3} \quad P (5 0 0) = \left( \begin{array}{c c} 0. 8 8 0 & 1. 5 6 0 \\ 1. 5 6 0 & 4. 7 7 1 \end{array} \right) \cdot 1 0 ^ {- 3}
$$

From Theorem 13.2 we get the following standard deviations for the estimates

$$\sigma_ {\dot {\alpha}} = 0. 5 \sqrt {8 . 8 0} \cdot 1 0 ^ {- 2} = 0. 0 1 5\sigma_ {b} = 0. 5 \sqrt {4 7 . 7 1} \cdot 1 0 ^ {- 2} = 0. 0 3 5$$

![](image/91ded3bd0fdb58098e3e2aa22d2617d0ddea5385c5e9b0c421bb27276e08ef20.jpg)

<details>
<summary>line</summary>

| Time | Parameter b | Parameter a |
| --- | --- | --- |
| 0 | ~0.5 | ~-1.0 |
| 500 | ~0.5 | ~-1.0 |
</details>

Figure 13.5 Recursive-parameter estimates when (13.10) to (13.12) are used on the data shown in Fig. 13.4. The true values are indicated by the dashed lines.

![](image/c3559514a42ece38feb7d6bd665be3ec05400096dd06573320b25d2a34071e7b.jpg)

<details>
<summary>line</summary>

| Time | Parameter estimates (δ) | Parameter estimates (α) |
| --- | --- | --- |
| 0 | 0 | -1 |
| 500 | 1 | -1 |
</details>

Figure 13.6 Recursive-parameter estimates for the system in Example 13.4 when the input is a unit pulse at time t = 25. The true values are indicated by the dashed lines.

The estimates are well within one standard deviation of their their true values. Now assume that the input signal is changed from a PRBS signal to a unit pulse at time t = 25. The estimates for the new experiment are shown in Fig. 13.6. The estimate of b is now very poor because the input signal is not sufficiently exciting. The estimate of a is, however, better because the output is excited by the noise and thus the output contains information about the parameter a.

The influence of feedback is illustrated in the next example.

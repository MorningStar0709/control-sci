(c)   
![](image/a642e0562cf5f00c52d718bde711c9cef0c8ece0bfe5c7e14b50a3cd58c76ec9.jpg)

<details>
<summary>line</summary>

| Time | u | y |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 5 | 1.0 | 0.0 |
| 10 | 1.0 | 0.0 |
| 15 | 1.0 | 0.0 |
| 20 | 1.0 | 0.0 |
</details>

(d)   
![](image/16d6f7585ac11f54eda901a6ecb0c4479d8f12e691b132b860a96e804391687d.jpg)

<details>
<summary>line</summary>

| Time | u | y | u_c |
| --- | --- | --- | --- |
| 0 | 0.0 | 1.0 | 1.0 |
| 5 | 0.0 | 0.0 | 1.0 |
| 10 | 0.0 | 0.0 | 1.0 |
| 15 | 0.0 | 0.0 | 1.0 |
| 20 | 0.0 | 0.0 | 1.0 |
</details>

Figure 11.2 Output, reference value, and control signal for the system in Example 11.1. The measurement disturbance has the frequency $\omega_{d} = 11.3$ rad/s. (a) $\omega_{B} = 25$ rad/s; (b) $\omega_{B} = 6.28$ rad/s; (c) $\omega_{B} = 6.28$ rad/s and the regulator compensated for a delay of $0.7h$ ; (d) $\omega_{B} = 2.51$ rad/s and the regulator compensated for a delay of $1.7h$ .

Example 11.1 shows that it is important to use an anti-aliasing filter and that the filter has to be considered in the design. For a Bessel filter, however, it is sufficient to approximate the filter by a time delay. The additional dynamics cause no principle problems for an adaptive controller because all parameters are estimated. However, inclusion of the prefilter dynamics will increase the model order significantly. In the particular case of Example 11.1 the model will increase from second order to sixth order. This means that the number of parameters that we have to estimate increases from 4 to 12. A simple way to reduce the number of parameters is to approximate the prefilter by a delay. It is then sufficient to estimate five parameters of the model

$$y (t) + a _ {1} y (t - h) + a _ {2} y (t - 2 h) =b _ {0} u (t - d h) + b _ {1} u (t - d h - h) + b _ {2} u (t - d h - 2 h)$$

where the value of $d$ depends on the bandwidth of the filter (see Table 11.2).

It is cumbersome and costly to change the bandwidth of an analog prefilter. This poses problems for systems in which the sampling rate has to be changed. A nice implementation in such a case is to use dual rate sampling. A high fixed sampling rate is used together with a fixed analog prefilter. A digital filter is then used to filter the signal at a slower rate when that is needed. This implies that fewer parameters have to be estimated.

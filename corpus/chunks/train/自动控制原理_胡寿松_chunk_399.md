| t | e(t) |
| --- | --- |
| 0 | 0 |
| Peak | High |
| Low | Low |
</details>

(a)

![](image/81ba39ba50f6259d0bb2e2f62cfbc86bdb5785f914157eb3f0546259720906a0.jpg)

<details>
<summary>bar</summary>

| t | δ_T(t) |
| --- | --- |
| T | 0 |
| 3T | 0 |
| 5T | 0 |
| >5T | 0 |
</details>

(b)

![](image/157078823f79ccc9ac38602cd78a7596604073a22879e5f0016e2ad46e2c1b08.jpg)

<details>
<summary>line</summary>

| t | e*(t) |
| --- | --- |
| 0 | 0 |
| > 0 | Decreasing from peak to baseline |
</details>

(c)   
图 7-11 理想采样过程

因为理想单位脉冲序列 $\delta_{T}(t)$ 可以表示为

$$\delta_ {T} (t) = \sum_ {n = 0} ^ {\infty} \delta (t - n T) \tag {7-2}$$

其中 $\delta(t-nT)$ 是出现在时刻 t=nT、强度为 1 的单位脉冲，故式(7-1)可以写为

$$e ^ {*} (t) = e (t) \sum_ {n = 0} ^ {\infty} \delta (t - n T)$$

由于 $e(t)$ 的数值仅在采样瞬时才有意义，所以上式又可表示为

$$e ^ {*} (t) = \sum_ {n = 0} ^ {\infty} e (n T) \delta (t - n T) \tag {7-3}$$

值得注意，在上述讨论过程中假设了

$$e (t) = 0, \quad \forall t < 0$$

因此脉冲序列从零开始。这个前提在实际控制系统中，通常都是满足的。

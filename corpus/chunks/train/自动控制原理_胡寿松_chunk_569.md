$$
\left\{ \begin{array}{l} \omega_ {1} = 4, \\ A _ {1} = 1. 1, \end{array} \right. \quad \left\{ \begin{array}{l} \omega_ {2} = 4 \\ A _ {2} = 2. 3 \end{array} \right.
$$

根据周期运动稳定性判据知， $A_{1}$ 和 $\omega_{1}$ 对应不稳定的周期运动； $A_{2}$ 和 $\omega_{2}$ 对应稳定的周期运动。当初始条件或外扰动使 $A < A_{1}$ 时，则系统运动不存在自振荡，稳态误差 $|e| < h$ ；当初始条件或外扰动使 $A > A_{1}$ 时，则系统产生自振荡， $e(t) = 1.146\sin4t$ 。

2) $G_{c}(s) = \frac{0.25 + 1}{0.03s + 1} \cdot \frac{1}{8.3}$ 为无源超前网络，系统线性部分为 $G(s)G_{c}(s)$ 。 $\Gamma_{\alpha G_c}$ 曲线如图8-51中曲线②所示，其中穿越频率为

![](image/40314bad5947642d5e753715822d9916f6e7d9b92c382bd739e801ab4bcc6cb3.jpg)

<details>
<summary>text_image</summary>

- \frac{1}{N(A)} ①
-1 -0.785 γ_m γ
ω
ω'
-0.226
0
j
j
</details>

图 8-51 例 8-7 非线性系统的频率特性

$$\omega_ {x} = 1 1. 9 7G _ {c} (\mathrm{j} \omega_ {x}) G (\mathrm{j} \omega_ {x}) = - 0. 2 2 6$$

由于 $\Gamma \alpha_{c}$ 曲线不包围 $-\frac{1}{N(A)}$ 曲线，系统稳定。取 $A$ 为定值，由 $\left|G_{c}(\mathrm{j}\omega_{c})G(\mathrm{j}\omega_{c})N(A)\right| = 1$ ，可以解得 $\omega_{c}$ ，则相角裕度为

$$\gamma (A) = 1 8 0 ^ {\circ} - \underline {{{/ G _ {c} (\mathrm{j} \omega_ {c}) G (\mathrm{j} \omega_ {c})}}}$$

特殊地，取 $A = A_{m}$ ，相应地相角裕度为 $\gamma_{m}$ ，约为 $30^{\circ}$ 左右，而由图8-51可知

$$\gamma (A) \geqslant \gamma_ {m}$$

因此加入串联超前校正网络，可以使非线性系统消除自振，且使系统具有一定的相角裕度。当然也可以通过减小线性部分的增益消除自振，但这样做会使系统响应的快速性降低。

本例两种 $G_{c}(s)$ 情况下的误差响应如图 8-52 所示。

![](image/00677eaa23236a4fee1ce87f6a873efd968531fae5f5efa341bff737db7b2d42.jpg)

<details>
<summary>line</summary>

| t | e(t) |
| --- | --- |
| 0.0 | 2.0 |
| 1.0 | -1.5 |
| 2.0 | 1.3 |
| 3.0 | -1.2 |
| 4.0 | -1.0 |
| 5.0 | 1.2 |
| 6.0 | -1.1 |
| 7.0 | 1.0 |
| 8.0 | -1.2 |
| 9.0 | -1.3 |
| 10.0 | 1.2 |
</details>

(a) $G_{c}(s) = 1$

![](image/45a4aca60f3a60591697b57fb446285b1117e776d25d5f380b18e8a449669ca6.jpg)

<details>
<summary>line</summary>

| t | e(t) |
| --- | --- |
| 0.0 | 2.0 |
| 1.0 | 1.6 |
| 2.0 | 1.5 |
| 3.0 | 1.45 |
| 4.0 | 1.45 |
| 5.0 | 1.45 |
| 6.0 | 1.45 |
| 7.0 | 1.45 |
| 8.0 | 1.45 |
| 9.0 | 1.45 |
| 10.0 | 1.45 |
</details>

图 8-52 例 8-7 非线性系统的时间响应(MATLAB)

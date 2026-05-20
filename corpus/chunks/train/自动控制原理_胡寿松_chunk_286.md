# 1) 若 $G(s)H(s)$ 无虚轴上极点。

$\Gamma_{GH}$ 在 $s=j\omega,\omega\in[0,+\infty)$ 时，对应开环幅相曲线；

$\Gamma_{GH}$ 在 $s = \infty \mathrm{e}^{\mathrm{j}\theta}, \theta \in [0^{\circ}, +90^{\circ}]$ 时，对应原点 $(n > m$ 时)或 $(K^{*}, j0)$ 点 $(n = m$ 时）， $K^{*}$ 为系统开环根轨迹增益。

2) 若 $G(s)H(s)$ 有虚轴极点。当开环系统含有积分环节时，设

$$G (s) H (s) = \frac {1}{s ^ {\nu}} G _ {1} (s) \quad (\nu > 0, | G _ {1} (\mathrm{j} 0) | \neq \infty) \tag {5-67}$$

有

$$A (0 _ {+}) = \infty , \quad \varphi (0 _ {+}) = \underline {{{G (\mathrm{j} 0 _ {+}) H (\mathrm{j} 0 _ {+})}}} = \nu \times (- 9 0 ^ {\circ}) + \underline {{{G _ {1} (\mathrm{j} 0 _ {+})}}} \tag {5-68}$$

于是在原点附近，闭合曲线 $\Gamma$ 为 $s = \varepsilon \mathrm{e}^{\mathrm{j}\theta},\theta \in [0^{\circ}, + 90^{\circ}]$ ，且有 $G_{1}(\varepsilon \mathrm{e}^{\mathrm{j}\theta}) = G_{1}(\mathrm{j}0)$ ，故

$$G (s) H (s) \mid_ {s = e e ^ {j \theta}} \approx \infty \quad e ^ {j \left(\left\lfloor \frac {1}{e ^ {\nu} e ^ {j \theta}} + \right\rfloor G _ {1} (e e ^ {j \theta})\right)} = \infty e ^ {j [ \nu \times (- \theta) + \left\lfloor G _ {1} (j 0) \right]} \tag {5-69}$$

对应的曲线为从 $G_{1}(\mathrm{j}0)$ 点起，半径为 $\infty$ 、圆心角为 $\nu \times (-\theta)$ 的圆弧，即可从 $G(\mathrm{j}0_{+})H(\mathrm{j}0_{+})$ 点起逆时针作半径无穷大、圆心角为 $\nu \times 90^{\circ}$ 的圆弧，如图5-32(a)中虚线所示。

![](image/1030a9b4ae0b28b184594dfb83cd20fbc5a42106511d374ee389d7762355d56c.jpg)

<details>
<summary>text_image</summary>

j
ν=1
G(j∞)H(j∞)G(j0)H(j0)
0
ω
G(j0+)H(j0+)
</details>

(a)

![](image/fdb2e555cf87146695a42b0ffc4d28dadae4e69f867c81459ec613dcaf19545f.jpg)

<details>
<summary>text_image</summary>

G(jω_{n-})H(jω_{n-})
j
ν₁=3
0
ω
G(jω_{n+})H(jω_{n+})
</details>

(b)   
图 5-32 $F(s)$ 平面的半闭合曲线

当开环系统含有等幅振荡环节时，设

$$G (s) H (s) = \frac {1}{(s ^ {2} + \omega_ {n} ^ {2}) ^ {\nu_ {1}}} G _ {1} (s) \qquad (\nu_ {1} > 0, | G _ {1} (\pm \mathrm{j} \omega_ {n}) | \neq \infty) \tag {5-70}$$

考虑 s 在 $j\omega_{n}$ 附近沿 $\Gamma$ 运动时， $\Gamma_{GH}$ 的变化为

$$s = \mathrm{j} \omega_ {n} + \varepsilon \mathrm{e} ^ {\mathrm{j} \theta}, \quad \theta \in [ - 9 0 ^ {\circ}, + 9 0 ^ {\circ} ] \tag {5-71}$$

因为 $\varepsilon$ 为正无穷小量，所以式(5-70)可写为

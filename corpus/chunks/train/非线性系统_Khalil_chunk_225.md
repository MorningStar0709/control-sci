斜率 = s₂
ψ(y)
-δ
斜率 = s₂
δ
y
斜率 = s₁
ψ(a sin θ)
β
π
θ
a y
π
θ
</details>

图7.15 分段线性函数

![](image/089e90cab56b294228d30fc7e51b9332c7bb0a3122bd24e9c661e7d0a53638d8.jpg)

<details>
<summary>line</summary>

| a | Ψ(a) |
| --- | --- |
| 0 | 1 |
| s₁ | > s₂ |
| > s₂ | < s₂ |
</details>

![](image/74f6ef8912dff1910c7cfe58490fee19ee1e582fd3f06858a9236d2bf989ce6c.jpg)

<details>
<summary>line</summary>

| a | Ψ(a) |
| --- | --- |
| 0 | 0 |
| s₁ | > s₂ |
</details>

图 7.16 图 7.15 中分段线性函数的描述函数

例 7.8 考虑一个奇对称非线性特性, 对于所有 $y \in R$ , 满足扇形区域条件

$$\alpha y ^ {2} \leqslant y \psi (y) \leqslant \beta y ^ {2}$$

描述函数 $\Psi(a)$ 满足下界

$$\Psi (a) = \frac {2}{\pi a} \int_ {0} ^ {\pi} \psi (a \sin \theta) \sin \theta d \theta \geqslant \frac {2 \alpha}{\pi} \int_ {0} ^ {\pi} \sin^ {2} \theta d \theta = \alpha$$

和上界 $\Psi (a) = \frac{2}{\pi a}\int_0^\pi \psi (a\sin \theta)\sin \theta d\theta \leqslant \frac{2\beta}{\pi}\int_0^\pi \sin^2\theta d\theta = \beta$

因此 $\alpha \leqslant \Psi (a)\leqslant \beta ,\forall a\geqslant 0$

△

方程(7.29)可写为

$$\{\operatorname{Re} [ G (j \omega) ] + j \operatorname{Im} [ G (j \omega) ] \} \Psi (a) + 1 = 0$$

因为描述函数 $\Psi(a)$ 是实函数, 这个方程等效于下面两个实方程:

$$1 + \Psi (a) \operatorname{Re} [ G (j \omega) ] = 0 \tag {7.31}\operatorname{Im} [ G (j \omega) ] = 0 \tag {7.32}$$

因为方程(7.32)与 $a$ 无关, 所以可先求解 $\omega$ , 以确定可能的振荡频率。再对每个解 $\omega$ , 对 $a$ 解方程(7.31)。注意, 可能的振荡频率完全由传递函数 $G(s)$ 决定, 它们与非线性特性 $\psi(\cdot)$ 无关。非线性特性仅决定相应 $a$ 的值, 即可能的振荡幅度。如下面几个例题所示, 可以通过这一步骤用解析法解低阶传递函数。

例7.9 设

$$G (s) = \frac {1}{s (s + 1) (s + 2)}$$

并考虑两个非线性特性:正负号非线性和饱和非线性。通过简单运算可写出 $G(j\omega)$ 的表达式为

$$G (j \omega) = \frac {- 3 \omega - j (2 - \omega^ {2})}{9 \omega^ {3} + \omega (2 - \omega^ {2}) ^ {2}}$$

方程(7.32)的形式为 $\frac{(2 - \omega^2)}{9\omega^3 + \omega(2 - \omega^2)^2} = 0$

该方程有一个正根 $\omega = \sqrt{2}$ 。注意，对方程(7.32)的每个正根都存在一个模值相等的负根。这里只考虑正根的情况，还要注意 $\omega = 0$ 时的根没有意义，因为它不产生非平凡周期解。在 $\omega = \sqrt{2}$ 时计算 $\operatorname{Re}[G(j\omega)]$ 的值，并代入方程(7.31)，得 $\Psi(a) = 6$ 。到此为止，除了未给出的非线性 $\psi (\cdot)$ ，我们已经收集到所有的必要信息。现在考虑正负号非线性特性。在例7.6中已求出 $\Psi (a) = 4 / \pi a$ ，因此 $\Psi (a) = 6$ 有唯一解 $a = 2 / 3\pi$ 。现在可以说由 $G(s)$ 和正负号非线性特性构成的非线性系统可能振荡，其频率接近 $\sqrt{2}$ ，振幅（在非线性特性输入端）接近 $2 / 3\pi$ 。下面考虑饱和非线性特性。从例7.7已知，对所有 $a$ ，有 $\Psi (a)\leqslant 1$ ，因此 $\Psi (a) = 6$ 无解。所以，由 $G(s)$ 和饱和非线性特性构成的非线性系统不会产生持续振荡。

例7.10 设 $G(s) = \frac{-s}{s^2 + 0.8s + 8}$

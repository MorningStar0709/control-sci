开环幅相曲线的终点：

$$G (\mathrm{j} \infty) H (\mathrm{j} \infty) = 0 / - 3 6 0 ^ {\circ}$$

由开环频率特性表达式知， $G(\mathrm{j}\omega)H(\mathrm{j}\omega)$ 的虚部不为零，故与实轴无交点。注意到开环系统含有等幅振荡环节 $(\zeta = 0)$ ，当 $\omega$ 趋于 $\omega_{n}$ 时， $A(\omega_{n})$ 趋于无穷大，而相频特性

$$\varphi (\omega_ {n -}) \approx - 9 0 ^ {\circ} - \tan^ {- 1} T \omega_ {n} > - 1 8 0 ^ {\circ}; \quad \omega_ {n -} = \omega_ {n} - \varepsilon , \quad \varepsilon > 0\varphi (\omega_ {n +}) \approx - 9 0 ^ {\circ} - \tan^ {- 1} T \omega_ {n} - 1 8 0 ^ {\circ}; \quad \omega_ {n +} = \omega_ {n} + \varepsilon , \quad \varepsilon > 0$$

即 $\varphi (\omega)$ 在 $\omega = \omega_{n}$ 的附近，相角突变 $-180^{\circ}$ ，幅相曲线在 $\omega_{n}$ 处呈现不连续现象。作系统开环概略幅相曲线如图5-23所示。

根据以上例子,可以总结绘制开环概略幅相曲线的规律如下:

1) 开环幅相曲线的起点, 取决于比例环节 K 和系统积分或微分环节的个数 $\nu$ (系统型别)。

$\nu<0$ , 起点为原点。

$\nu=0$ , 起点为实轴上的点 K 处 (K 为系统开环增益, 注意 K 有正负之分)。

$\nu>0$ , 设 $\nu=4k+i(k=0,1,2,\cdots;i=1,2,3,4)$ ，则 K>0 时为 $i\times(-90^{\circ})$ 的无穷远处，K<0 时为 $i\times(-90^{\circ})-180^{\circ}$ 的无穷远处。

![](image/a7f1f2f1619f712077e73cd734e89e6544b153fab3be24b5ff41143a29ad0f4f.jpg)

<details>
<summary>text_image</summary>

j
ω=ωₙ₊
ω = ωₙ₋
ω = ωₙ₋
arctanTωₙ
0
</details>

图 5-23 例 5-5 系统开环概略幅相曲线

2）开环幅相曲线的终点，取决于开环传递函数分子、分母多项式中最小相位环节和非最小相位环节的阶次和。

设系统开环传递函数的分子、分母多项式的阶次分别为 $m$ 和 $n$ , 记除 $K$ 外, 分子多项式中最小相位环节的阶次和为 $m_{1}$ , 非最小相位环节的阶次和为 $m_{2}$ , 分母多项式中最小相位环节的阶次和为 $n_{1}$ , 非最小相位环节的阶次和为 $n_{2}$ , 则有

$$
m = m _ {1} + m _ {2}n = n _ {1} + n _ {2}
\varphi (\infty) = \left\{ \begin{array}{l l} {[ (m _ {1} - m _ {2}) - (n _ {1} - n _ {2}) ] \times 9 0 ^ {\circ},} & K > 0 \\ {[ (m _ {1} - m _ {2}) - (n _ {1} - n _ {2}) ] \times 9 0 ^ {\circ} - 1 8 0 ^ {\circ},} & K <   0 \end{array} \right. \tag {5-51}
$$

特殊地，当开环系统为最小相位系统时，若

$$n = m, \quad G (\mathrm{j} \infty) H (\mathrm{j} \infty) = K ^ {*} \tag {5-52}n > m, \quad G (\mathrm{j} \infty) H (\mathrm{j} \infty) = 0 / (n - m) \times (- 9 0 ^ {\circ}) \tag {5-53}$$

其中 $K^{*}$ 为系统开环根轨迹增益。

3）若开环系统存在等幅振荡环节，重数 $l$ 为正整数，即开环传递函数具有下述形式：

$$G (s) H (s) = \frac {1}{\left(\frac {s ^ {2}}{\omega_ {n} ^ {2}} + 1\right) ^ {l}} G _ {1} (s) H _ {1} (s)$$

$G_{1}(s)H_{1}(s)$ 不含 $\pm \mathrm{j}\omega_{n}$ 的极点，则当 $\omega$ 趋于 $\omega_{n}$ 时， $A(\omega)$ 趋于无穷，而

$$
\begin{array}{l} \varphi (\omega_ {n -}) \approx \varphi_ {1} (\omega_ {n}) = \underline {{{{G _ {1} (\mathrm{j} \omega_ {n}) H _ {1} (\mathrm{j} \omega_ {n})}}}} \\ \varphi (\omega_ {n +}) \approx \varphi_ {1} (\omega_ {n}) - l \times 1 8 0 ^ {\circ} \\ \end{array}
$$

即 $\varphi(\omega)$ 在 $\omega=\omega_{n}$ 附近，相角突变 $-l\times180^{\circ}$ 。

# 例 9.11 继电器非线性的描述函数

找出图 9.6b 所示的继电器或符号函数的描述函数且定义

$$
\operatorname{sgn} (x) = \left\{ \begin{array}{l l} + 1 & , x > 0 \\ 0 & , x = 0 \\ - 1 & , x <   0 \end{array} \right.
$$

![](image/45dd4f051c63009af89f32153df97474c861633a3ad36e25daf4531eeb025716.jpg)

<details>
<summary>line</summary>

| a | K_eq |
| --- | --- |
| 0 | 1.0 |
| 1 | 1.0 |
| 2 | 0.6 |
| 3 | 0.4 |
| 4 | 0.3 |
| 5 | 0.25 |
| 6 | 0.2 |
| 7 | 0.18 |
| 8 | 0.15 |
| 9 | 0.13 |
| 10 | 0.12 |
</details>

图 9.26 k=N=1 时饱和非线性的描述函数

解答。对于任意大小的输入，输出都是幅值为 N 的方波，因此， $Y_{1}=\frac{4N}{\pi}$ 且 $K_{eq}=\frac{4N}{\pi a}$ 。如果我们让 $k\to+\infty$ ，那么同样可以从式(9.29)得到此解。对于小角度，有

$$\arcsin (\frac {N}{a k}) \approx \frac {N}{a k}$$

因此，由式 $（9.27）$ ，我们有

$$K _ {\mathrm{eq}} (a) = \frac {2}{\pi} \Big (k \Big (\frac {N}{a k} \Big) + \frac {N}{a} \Big) = \frac {4 N}{\pi a} \tag {9.30}$$

前述的两个非线性是无记忆的。接下来，我们考虑有记忆的非线性。许多应用中都能找到有记忆的非线性，包括磁性记录设备，机械系统中和电子电路中的间隙。考虑图9.27所示的双稳态的电子电路，这种电子电路叫做施密特（Schmitt）触发器（Sedra和Smith，1991）。这种电路具有记忆。参考图9.28，如果电路处于 $v_{out}=+N$ 的状态，那么正的 $v_{in}$ 值不会改变状态。为了将电路状态“触发”到 $v_{out}=-N$ ，我们必须使 $v_{in}$ 的负向值足够大，从而可使v的值为负。阈值为 $h=\frac{NR_{1}}{R_{2}}$ 。施密特触发器通常用于航天器控制（Bryson，1984）。下面，我们求滞环非线性的描述函数。

![](image/91f25cf2865d848008b731b08bc5599a0a6e64fd17a8e2e9980f63a6c416a573.jpg)

<details>
<summary>text_image</summary>

R₁
R₂
v
v_in +
-
+
-
v_out
</details>

图 9.27 施密特触发器电路

![](image/dd0d6176584d313b887d24d41c40f0af7fe08fbdd8979117289f044f08cfa548.jpg)

<details>
<summary>text_image</summary>

+N
-Vout
-h O h
-Vin
-N
</details>

图 9.28 施密特触发器电路的滞环非线性

# 例 7.17 引入参考输入

对于在 $x_{1}$ 处引入的阶跃指令信号，计算产生零稳态误差所需的增益，并针对例 7.14 中的振荡器画出当 $\omega_{0}=1$ 时所对应的单位阶跃响应。

解答。将式(7.71)的矩阵(因为 $y=x_{1}$ ，所以 $\omega_{0}=1$ ， $C=[1\quad0]$ )代入式(7.97)，得到

$$
\left[ \begin{array}{l l l} 0 & 1 & 0 \\ - 1 & 0 & 1 \\ 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} N _ {x} \\ N _ {u} \end{array} \right] = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] \tag {7.100}
$$

解为(在 Matlab 中 $x=a\backslash b$ ，其中 a, b 分别为左侧和右侧的矩阵)

$$
\mathbf {N} _ {x} = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right]
N _ {u} = 1
$$

对于给定的控制律，有

$$
\boldsymbol {K} = \left[ \begin{array}{l l} 3 \omega_ {0} ^ {2} & 4 \omega_ {0} \end{array} \right] = \left[ \begin{array}{l l} 3 & 4 \end{array} \right]
\overline {{{N}}} = N _ {u} + \mathbf {K N} _ {x} = 4 \tag {7.101}
$$

相应的阶跃响应曲线如图 7.16 所示（利用 Matlab 中的 step 函数）。

值得注意的是，控制律由式(7.98b)和式(7.99)给出。虽然这些表达式在理论上是等价的，但是在实际中它们是有差异的，式(7.98b)比式(7.99)对参数误差具有更强的鲁棒性，尤其是被控对象有一个极点在原点位置，且系统为1型时。下面这一例子非常清晰的说明了这一差异。

![](image/2a1959533ea1c2c089065f4f944f06705bf9910a8cf4cc243a8b7fc35214f10c.jpg)

<details>
<summary>line</summary>

| 时间/s | x₁ | x₂ | u/4 | u_ss |
| --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 1 | 0.8 | 0.6 | 0.7 | 0.0 |
| 2 | 1.0 | 0.3 | 0.2 | 0.0 |
| 3 | 1.0 | 0.1 | 0.0 | 0.0 |
| 4 | 1.0 | 0.0 | 0.0 | 0.0 |
| 5 | 1.0 | 0.0 | 0.0 | 0.0 |
| 6 | 1.0 | 0.0 | 0.0 | 0.25 |
| 7 | 1.0 | 0.0 | 0.0 | 0.25 |
</details>

图 7.16 振荡器对参考输入的阶跃响应

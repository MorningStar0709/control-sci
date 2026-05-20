# 例 7.30 带有降阶估计器的直流伺服系统的再设计

使用相同的控制极点，但利用降阶估计器，为例7.29中的直流伺服系统设计一个补偿器，取 $\omega_{n}=6rad/s,\quad\zeta=0.707$ ，并将估计器极点配置在 $-4.24\pm4.24j$ 的位置。

解答。降阶估计器相应的极点为

$$\mathrm{pe} = [ - 4. 4 2 + 4. 4 2 * \mathrm{j}; - 4. 2 4 - 4. 2 4 * \mathrm{j} ]$$

将系统矩阵分块，有

$$
\left[ \begin{array}{l l} A _ {\mathrm{aa}} & A _ {\mathrm{ab}} \\ A _ {\mathrm{ba}} & A _ {\mathrm{bb}} \end{array} \right] = \left[ \begin{array}{c c c} - 1 0 & 1 & 0 \\ - 1 6 & 0 & 1 \\ 0 & 0 & 0 \end{array} \right], \quad \left[ \begin{array}{l} B _ {\mathrm{a}} \\ B _ {\mathrm{b}} \end{array} \right] = \left[ \begin{array}{l} 0 \\ 0 \\ 1 0 \end{array} \right]
$$

解估计器误差的特征多项式为

$$\det (s \boldsymbol {I} - \boldsymbol {A} _ {\mathrm{bb}} + \boldsymbol {L A} _ {\mathrm{ab}}) = \alpha_ {\mathrm{e}} (s)$$

(用 place 函数) 求得

$$
\boldsymbol {L} = \left[ \begin{array}{c} 8. 5 \\ 3 6 \end{array} \right]
$$

由式(7.178)计算出补偿器传递函数为

$$D _ {\mathrm{cr}} (s) = 2 0. 9 3 \frac {(s - 0 . 7 3 5) (s + 1 . 8 7 1)}{(s + 0 . 9 9 0 \pm 6 . 1 2 0 \mathrm{j})}$$

该系统相应的根轨迹如图 7.43 所示。注意，这次得到的是非最小相位稳定的补偿器以及一个零度的根轨迹。由于所选增益都必须使所有闭环极点位于左半平面，所以根轨迹位于右半平面就不会引起麻烦。

![](image/41abe6765bcad5ea126c8609e7dec9aaa7939144ff32a58a0ee91df8e38d5b10.jpg)

<details>
<summary>line</summary>

| Re(s) | Im(s) |
| --- | --- |
| -8 | 6 |
| -7 | 5 |
| -6 | 4 |
| -5 | 3 |
| -4 | 2 |
| -3 | 1 |
| -2 | 0 |
| -1 | -1 |
| 0 | -2 |
| 1 | -3 |
| 2 | -4 |
| 3 | -5 |
| 4 | -6 |
</details>

图 7.43 直流伺服系统降阶控制器的根轨迹

下面尝试用对称根轨迹方法作为对该系统进行控制设计的另外一种途径。

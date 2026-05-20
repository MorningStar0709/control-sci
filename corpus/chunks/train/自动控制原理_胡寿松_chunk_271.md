| Real Axis | Imaginary Axis | Region |
| --- | --- | --- |
| -0.4 | 0.6 | ω |
| 0.4 | -0.6 | ω |
| 0.8 | -0.4 | K>0 |
| -0.2 | 0.6 | K<0 |
</details>

图 5-18 例 5-1 系统概略开环幅相曲线 (MATLAB)

幅值变化 $A(0_{+}) = \infty, A(\infty) = 0$

相角变化

$$
\begin{array}{l} \left\lfloor \frac {1}{j \omega}: - 9 0 ^ {\circ} \sim - 9 0 ^ {\circ} \right. \\ \left\lfloor \frac {1}{1 + \mathrm{j} T _ {1} \omega}: \quad 0 ^ {\circ} \sim - 9 0 ^ {\circ} \right. \\ \left\lfloor \frac {1}{1 + \mathrm{j} T _ {2} \omega}: \quad 0 ^ {\circ} \sim - 9 0 ^ {\circ} \right. \\ \angle K: \quad 0 ^ {\circ} \sim 0 ^ {\circ} \\ \varphi (\omega): \quad - 9 0 ^ {\circ} \sim - 2 7 0 ^ {\circ} \\ \end{array}
$$

起点处 $\operatorname{Re}[G(\mathrm{j}0_{+})H(\mathrm{j}0_{+})] = -K(T_1 + T_2)$

$$\operatorname{Im} \left[ G (\mathrm{j} 0 _ {+}) H (\mathrm{j} 0 _ {+}) \right] = - \infty$$

与实轴的交点

令 $\operatorname{Im}[G(\mathrm{j}\omega)H(\mathrm{j}\omega)] = 0$ ，得 $\omega_{r} = \frac{1}{\sqrt{T_1T_2}}$ ，于是

$$G (\mathrm{j} \omega_ {x}) H (\mathrm{j} \omega_ {x}) = \operatorname{Re} [ G (\mathrm{j} \omega_ {x}) H (\mathrm{j} \omega_ {x}) ] = - \frac {K T _ {1} T _ {2}}{T _ {1} + T _ {2}}$$

由此做系统开环幅相曲线，如图5-19中曲线①所示。图中虚线为开环幅相曲线的低频渐近线。由于开环幅相曲线用于系统分析时不需要准确知道渐近线的位置，故一般根据 $\varphi(0_{+})$ 取渐近线为坐标轴，图中曲线②为相应的开环概略幅相曲线。

例 5-2 中系统型次即开环传递函数中积分环节个数 $\nu=1$ ，若分别取 $\nu=2,3$ 和 4，则根据积分环节的相角，可将图 5-19 曲线分别绕原点旋转 $-90^{\circ}, -180^{\circ}$ 和 $-270^{\circ}$ ，即可得相应的开环概略幅相曲线，如图 5-20 所示。

![](image/ce3cff2d7c650726a85e08fd997bd3af521947ecef82a4ae4ebb07e6bbc2da0d.jpg)

<details>
<summary>other</summary>

| Point | Real Axis | Imaginary Axis |
| --- | --- | --- |
| ① | -2.0 | -2.5 |
| ② | -0.4 | -6.0 |
</details>

图 5-19 例 5-2 系统概略开环幅相曲线  
![](image/cf1aab926afbb22708317a3a4524062bb7476db07cae3ff5c45eee5cc9554196.jpg)

<details>
<summary>other</summary>

| Point | Real Axis | Imaginary Axis |
| --- | --- | --- |
| ω | -2.5 | -3.0 |
| v=1 | -2.0 | -2.0 |
| v=2 | -1.0 | 1.0 |
| v=3 | 1.5 | 0.0 |
| v=4 | 0.5 | -2.0 |
</details>

图 5-20 $\nu=1,2,3,4$ 时系统开环概略幅相曲线(MATLAB)

例 5-3 已知单位反馈系统开环传递函数为

$$G (s) = \frac {K (\tau s + 1)}{s (T _ {1} s + 1) (T _ {2} s + 1)}; \quad K, T _ {1}, T _ {2}, \tau > 0$$

试绘制系统概略开环幅相曲线。

解 系统开环频率特性为

$$G (\mathrm{j} \omega) = \frac {- \mathrm{j} K [ 1 - T _ {1} T _ {2} \omega^ {2} + T _ {1} \pi \omega^ {2} + T _ {2} \pi \omega^ {2} + \mathrm{j} \omega (\tau - T _ {1} - T _ {2} - T _ {1} T _ {2} \pi \omega^ {2}) ]}{\omega (1 + T _ {1} ^ {2} \omega^ {2}) (1 + T _ {2} ^ {2} \omega^ {2})}$$

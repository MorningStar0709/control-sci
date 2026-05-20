开环幅相曲线的起点 $G(j0_{+})=\infty/-90^{\circ}$ ，终点 $G(j\infty)=0/-180^{\circ}$ 。

与实轴的交点：当 $\tau < \frac{T_1T_2}{T_1 + T_2}$ 时，得

$$
\left\{ \begin{array}{l} \omega_ {x} = \frac {1}{\sqrt {T _ {1} T _ {2} - T _ {1} \tau - T _ {2} \tau}} \\ G (\mathrm{j} \omega_ {x}) = - \frac {K (T _ {1} + T _ {2}) (T _ {1} T _ {2} - T _ {1} \tau - T _ {2} \tau + \tau^ {2})}{(T _ {1} T _ {2} - T _ {1} \tau - T _ {2} \tau + T _ {1} ^ {2}) (T _ {1} T _ {2} - T _ {1} \tau - T _ {2} \tau + T _ {2} ^ {2})} \end{array} \right.
$$

变化范围：

$\tau > \frac{T_1 T_2}{T_1 + T_2}$ 时，开环幅相曲线位于第 III 象限或第 IV 与第 III 象限；

$\tau < \frac{T_1T_2}{T_1 + T_2}$ 时，开环幅相曲线位于第III象限与第II象限。

开环概略幅相曲线如图 5-21 所示。

应该指出,由于开环传递函数具有一阶微分环节,系统开环幅相曲线有凹凸现象,因为绘制的是概略幅相曲线,故这一现象无须准确反映。

例5-4 已知系统开环传递函数为

$$G (s) H (s) = \frac {K (- \tau s + 1)}{s (T s + 1)}; \quad K, \tau , T > 0$$

试概略绘制系统开环幅相曲线。

解 系统开环频率特性为

$$G (\mathrm{j} \omega) H (\mathrm{j} \omega) = \frac {K [ - (T + \tau) \omega - \mathrm{j} (1 - T \tau \omega^ {2}) ]}{\omega (1 + T ^ {2} \omega^ {2})}$$

开环幅相曲线的起点：

![](image/cf18cc958d8e93982ea32295cedb2754e80d3a1055829321505451b6addfa48e.jpg)

<details>
<summary>other</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -20 | -10 |
| -18 | -8 |
| -16 | -6 |
| -14 | -4 |
| -12 | -2 |
| -10 | 0 |
| -8 | 2 |
| -6 | 4 |
| -4 | 6 |
| -2 | 8 |
| 0 | 10 |
</details>

图 5-21 例 5-3 系统开环概略幅相曲线 (MATLAB)

$$A (0 _ {+}) = \infty , \varphi (0 _ {+}) = - 9 0 ^ {\circ}$$

开环幅相曲线的终点： $A(\infty) = 0, \varphi (\infty) = -270^{\circ}$

与实轴的交点：令虚部为零，解得

$$\omega_ {x} = \frac {1}{\sqrt {T \tau}}, \quad G (\mathrm{j} \omega_ {x}) H (\mathrm{j} \omega_ {x}) = - K \tau$$

因为 $\varphi (\omega)$ 从 $-90^{\circ}$ 单调减至 $-270^{\circ}$ ，故幅相曲线在第III与第II象限间变化。

开环概略幅相曲线如图 5-22 所示。

在例 5-4 中, 系统含有非最小相位一阶微分环节, 称开环传递函数含有非最小相位环节的系统为非最小相位系统, 而开环传递函数全部由最小相位环节构成的系统称为最小相位系统。比较例 5-2、例 5-3 和例 5-4 可知, 非最小相位环节的存在将对系统的频率特性产生一定的影响, 故在控制系统分析中必须加以重视。

例 5-5 设系统开环传递函数为

$$G (s) H (s) = \frac {K}{s (T s + 1) (s ^ {2} / \omega_ {n} ^ {2} + 1)}; \quad K, T > 0$$

试绘制系统开环概略幅相曲线。

![](image/14dc122920c2985ae5a15456a06749c54ec8a1a8c441ddd3e59898bd521f34ea.jpg)

<details>
<summary>other</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -3.0 | -10 |
| -2.5 | -4 |
| -2.0 | 0 |
| 0 | 0 |
</details>

图 5-22 例 5-4 系统概略幅相曲线 (MATLAB)

解 系统开环频率特性为

$$G (\mathrm{j} \omega) H (\mathrm{j} \omega) = \frac {- K (T \omega + \mathrm{j})}{\omega (1 + T ^ {2} \omega^ {2}) \left(1 - \frac {\omega^ {2}}{\omega_ {n} ^ {2}}\right)}$$

开环幅相曲线的起点：

$$G (\mathrm{j} 0 _ {+}) H (\mathrm{j} 0 _ {+}) = \infty \angle - 9 0 ^ {\circ}$$

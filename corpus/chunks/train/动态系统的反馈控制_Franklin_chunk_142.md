# 例 3.16 受激励微分方程

求微分方程 $\ddot{y}(t)+5\dot{y}(t)+4y(t)=3$ 的解，其中 $y(0)=\alpha,\dot{y}(0)=\beta$ 。

解答。利用式(3.41)和式(3.42)对该微分方程的两边进行拉普拉斯变换，得

$$s ^ {2} Y (s) - s \alpha - \beta + 5 [ s Y (s) - \alpha ] + 4 Y (s) = \frac {3}{s}$$

解得 $Y(s)$ 为

$$Y (s) = \frac {s (s \alpha + \beta + 5 \alpha) + 3}{s (s + 1) (s + 4)}$$

运用消去法进行部分分式展开，有

$$Y (s) = \frac {\frac {3}{4}}{s} - \frac {\frac {3 - \beta - 4 \alpha}{3}}{s + 1} + \frac {\frac {3 - 4 \alpha - 4 \beta}{1 2}}{s + 4}$$

因此可得时间函数为

$$y (t) = \left(\frac {3}{4} + \frac {- 3 + \beta + 4 \alpha}{3} \mathrm{e} ^ {- t} + \frac {3 - 4 \alpha - 4 \beta}{1 2} \mathrm{e} ^ {- 4 t}\right) 1 (t)$$

将该解进行二次微分，并代回原微分方程，可验证该解满足原微分方程。

如果初始条件都是零，解是特别简单的。

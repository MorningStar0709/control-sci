# 10.5.3 最优轨迹的设计

不失一般性，最优轨迹可在定点运动-摆线运动轨迹的基础上进行优化。摆线运动的表达式如下：

$$\theta_ {\mathrm{r}} = \left(\theta_ {\mathrm{d}} - \theta_ {0}\right) \left[ \frac {t}{T _ {\mathrm{E}}} - \frac {1}{2 \pi} \sin \left(\frac {2 \pi t}{T _ {\mathrm{E}}}\right) \right] + \theta_ {0} \tag {10.11}$$

式中， $T_{E}$ 为摆线周期； $\theta_{0}$ 和 $\theta_{d}$ 分别为角的初始角度和目标角度。

由于差分进化算法是一种离散型的算法，因此需要对连续型的参考轨迹式（10.11）进行等时间隔采样，取时间间隔为 $\frac{T_{\mathrm{E}}}{2n}$ ，则可得到离散化的参考轨迹为

$$\overline {{{\theta}}} _ {r} = \left[ \overline {{{\theta}}} _ {r, 0}, \overline {{{\theta}}} _ {r, 1}, \dots , \overline {{{\theta}}} _ {r, 2 n - 1}, \overline {{{\theta}}} _ {r, 2 n} \right] \tag {10.12}$$

式中， $\overline{\theta}_{r,j}$ 为在时刻 $t=\frac{j}{2n}T_{E}$ 对于 $\theta_{r}$ 的采样值 $(j=0,1,\ldots,2n)$ ; $\overline{\theta}_{r}$ 是离散的参考轨迹。

定义 $\Delta \overline{\theta}_j(k)$ 为与参考轨迹的偏差（ $j = 1,2,\dots,n - 1$ ）， $k$ 表示差分进化算法中的第 $k$ 次迭代，则得

$$\overline {{\theta}} _ {\mathrm{op} j} (k) = \overline {{\theta}} _ {\mathrm{r}, j} + \Delta \overline {{\theta}} _ {j} (k) \tag {10.13}$$

式中， $\overline{\theta}_{\mathrm{opj}}(k)$ 为在时刻 $t=\frac{j}{2n}T_{E}$ 由差分进化算法的第 k 次迭代得到的关节角的修正角度。

![](image/ae9f915b4b84f750825bf76761c2f0441f3bf3e56f2c61e43751b240ec4f062b.jpg)

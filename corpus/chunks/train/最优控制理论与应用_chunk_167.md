# 9.3 奇异最优控制的算法

求解奇异最优控制的算法有很多,其中较为成熟的方法是正则化方法,也就是利用摄动方法把一个奇异问题化成为相应的非奇异问题,这种摄动应使非奇异问题的解在某种意义上能逼近原来的奇异问题的解。所采用的正则化方法是一个很简单的方法,这就是在性能指标中的被积函数上加上一项 $\frac{1}{2}\varepsilon_{k}u^{T}u$ ,其中 $\varepsilon_{k}$ 是一个正的小量,其效果是对最优性能指标作了一个微小摄动。下面介绍一下正则化方法。

如下的受控系统

$$\dot {x} = f _ {1} (x, t) + f _ {u} (x, t) \boldsymbol {u} \tag {9-39}x \left(t _ {0}\right) = x _ {0}$$

其中控制 $\pmb{u}(t)$ 受不等式约束

$$\mid u _ {j} (t) \mid \leqslant 1, \text {对所有} t \in [ t _ {0}, t _ {\mathrm{f}} ], j = 1, 2, \dots , r \tag {9-40}$$

性能指标为

$$J [ \boldsymbol {u} (\cdot) ] = S (x (t _ {\mathrm{f}})) + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} L (x, t) \mathrm{d} t \tag {9-41}$$

这里 $t_0, t_f$ 已知。 $f_1, f_u, L$ 和 $S$ 对每个自变量至少是一次连续可微的。问题是选择满足约束式(9-40)的分段连续函数 $\pmb{u}(\cdot)$ ，使 $J$ 最小。

如无进一步的假设,这类问题的最优控制函数是由 Bang-Bang 弧及奇异子弧所组成的。解正常最优控制问题,目前已有一些有效的计算方法。而计算奇异控制的方法的基本思想是在性能指标的被积函数中增加 $\frac{1}{2}\varepsilon_{k}u^{T}u$ 项,将性能指标式(9-41)修改为

$$J [ \boldsymbol {u} (\cdot), \varepsilon_ {k} ] = S (x (t _ {\mathrm{f}})) + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} (L (x, t) +\frac {1}{2} \varepsilon_ {k} \boldsymbol {u} ^ {\mathrm{T}} \boldsymbol {u}) \mathrm{d} t \tag {9-42}$$

问题就变成非奇异的了。然后利用解非奇异最优控制的算法来解修改后的非奇异问题。可以证明，当 $\lim_{k\to \infty}\varepsilon_k = 0$ 时， $J[\pmb{u}(\cdot),\pmb{\varepsilon}_k]$ 将收敛以于式(9-41)的最小值。采用此种方法并不需要预先知道是否有奇异弧、奇异弧的段数及所在位置。算法的步骤如下：

第一步：选择一个起始值 $\varepsilon_{1}>0$ 和一个标称控制函数 $\overline{\boldsymbol{u}}(\cdot)$ 。

第二步：解所得的正则问题 $(k=1)$ ，得到最小化的控制函数 $u_{k}(\cdot)$ 。

第三步：选择 $\varepsilon_{k + 1} < \varepsilon_k$ （例如 $\varepsilon_{k + 1} = \frac{1}{10}\varepsilon_k$ ），并令 $\overline{\pmb{u}}_{k + 1}(\cdot) = \pmb{u}_k(\cdot)$ ， $k = k + 1$ ，重复步骤2，直至 $\varepsilon_k < \sigma$ 停止运算，其中 $\sigma$ 是一个预先规定的小正数。

剩下的问题需要证明算法的收敛性。为此，先作两个假设：

假设1：设 $U$ 是定义在 $[t_0, t_f]$ 上，且满足式(9-40)约束的 $r$ 维分段连续函数的集合，且有

$$\inf _ {\boldsymbol {u} (\cdot)} J [ \boldsymbol {u} (\cdot) ] = \min _ {\boldsymbol {u} (\cdot)} J [ \boldsymbol {u} (\cdot) ] = \gamma_ {0} \tag {9-43}$$

该假设说明,式(9-41)性能指标 J 的下确界存在,且等于 J 的最小值 $\gamma_{0}$ 。

假设 2: 对于 $u(\cdot) \in U$ , 有

$$\inf _ {\boldsymbol {u} (\cdot)} J [ \boldsymbol {u} (\cdot), \varepsilon_ {k} ] = J [ \boldsymbol {u} ^ {*} (\cdot), \varepsilon_ {k} ] \tag {9-44}$$

其中 $u^{*}(\cdot)$ 是使式(9-42)为最小的控制。

在上述两个假设的条件下,有如下收敛定理。

定理 对于任意正的序列 $\{\varepsilon_k\}, \varepsilon_k > \varepsilon_{k+1} > 0$ ，且 $\lim_{k \to \infty} \varepsilon_k = 0$ ，那么在上

述两个假设条件下,有

$$\lim _ {k \rightarrow \infty} J [ \boldsymbol {u} (\cdot), \varepsilon_ {k} ] = \gamma_ {0} \tag {9-45}$$

定理表明, 当 $k$ 趋于 $\infty$ 时, 算法的解逐渐趋于原来奇异问题的解。实际上, $\varepsilon_{k}$ 降低到足够小的数值时, 可以得到原奇异解的一个相当好的近似。然而, 当 $\varepsilon_{k}$ 太小时, 常常会造成数值计算上的困难, 为克服此种困难, 人们提出了一些改进的算法。除此之外, 用广义梯度法和函数空间拟牛顿法计算奇异解也是可行的。

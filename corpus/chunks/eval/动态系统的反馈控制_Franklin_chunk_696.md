# A.1 拉普拉斯变换

拉普拉斯变换可用于研究反馈系统的全响应问题，包括暂态响应。它与傅里叶变换相比，傅里叶变换主要考虑的是系统的稳态响应。在许多应用中，定义 $f(t)$ 的拉普拉斯变换是很有用的，记 $\mathcal{L}_{-}\{f(t)\} = F(s)$ ，作为一个复变量 $s = \sigma_1 + \mathrm{j}\omega$

$$F (s) \stackrel {\mathrm{def}} {=} \int_ {0 ^ {-}} ^ {\infty} f (t) \mathrm{e} ^ {- s t} \mathrm{d} t \tag {A.1}$$

这里使用 $0^{-}$ （即恰在 $t = 0$ 之前的值）作为积分下限，可认为是单向或单边拉普拉斯变换 $\Theta$ 如果函数 $f(t)$ 有指数阶拉普拉斯变换，那意味着存在一个实数 $\sigma_{1}$ 使得

$$\lim _ {t \to \infty} | f (t) \mathrm{e} ^ {- \sigma_ {1} t} | = 0 \tag {A.2}$$

被积函数中的指数衰减项提供了一个固定的衰减因子。这意味着当 $t \to \infty$ 时， $f(t)$ 不趋于零，选择足够大的 $\sigma_1$ ，使得 $f$ 的增长率小于指数项的增长率。例如， $a\mathrm{e}^{bt}$ 是指数序列，而 $\mathrm{e}^{t^2}$ 不是指数序列。如果对于 $s_0 = \sigma_0 + \mathrm{j}\omega_0$ ， $F(s)$ 存在，那么对任意满足

$$\operatorname{Re} (s) \geqslant \sigma_ {0} \tag {A.3}$$

$F(s)$ 也存在。使 $F(s)$ 存在的 $\sigma_0$ 的最小值称为收敛横坐标。恰好使 $\operatorname{Re}(s) \geqslant \sigma_0$ 的定义域称为收敛域。一般来说，双边拉普拉斯变换是在一个特定的区间上存在：

$$\alpha < \operatorname{Re} (s) < \beta \tag {A.4}$$

即此式定义了一个收敛区间。表 A.2 给出了一些拉普拉斯变换对。表中的每一项都是由拉普拉斯变换定理直接得到的 $^{①}$ 。

# 1) 拉普拉斯变换的存在性

如果拉普拉斯积分收敛，则函数 $f(t)$ 的拉普拉斯变换存在。若存在一个正实常数 $\sigma$ ，使得函数 $\mathrm{e}^{-\sigma t}|f(t)|$ 在 $t$ 趋于无穷大时趋于零，则称函数 $f(t)$ 为指数级的。

如果 $f(t)$ 在 t>0 范围内的每一个有限区间上分段连续，且当 t 趋于无穷大时函数 $f(t)$ 为指数级的，则 $f(t)$ 的拉普拉斯积分是收敛的。

如果 $\sigma >\sigma_{c}$ ，函数 $\mathrm{e}^{-\alpha t}|f(t)|$ 满足 $\mathrm{lime}^{-\alpha t}|f(t)|\to 0$ ，且有

$$\lim _ {t \to \infty} ^ {- \alpha t} | f (t) | \to \infty , \quad \forall \sigma < \sigma_ {c}$$

则 $\sigma_{c}$ 的值称为收敛横坐标。

对于函数 $f(t) = A\mathrm{e}^{-\alpha t}$ ，若

$$\lim _ {t \rightarrow \infty} e ^ {- a t} | A e ^ {- a t} | \rightarrow \infty , \quad \forall \sigma > - \alpha$$

则收敛横坐标 $\sigma_{c}=\alpha$ 。只有当 s 的实部 $\sigma$ 大于收敛横坐标 $\sigma_{c}$ 时，积分 $\int_{0}^{\infty}f(t)e^{-st}dt$ 才是收敛的。因此，必须将算子 s 选定为一个能使上述积分收敛的常数。

从函数 $F(s)$ 的极点来看, 收敛横坐标 $\sigma_{c}$ 相当于 s 平面内 $F(s)$ 最右边的极点的实部。例如

$$F (s) = \frac {K (s + 3)}{(s + 1) (s + 2)}$$

则 $\sigma_{c} = -1$ 。可以看出，对于 $t, \sin \omega t$ 和 $t \sin \omega t$ 这样一些函数，其收敛横坐标为零；对于 $\mathrm{e}^{-\sigma t}, t \mathrm{e}^{-\sigma t}$ 和 $\mathrm{e}^{-\sigma t} \sin \omega t$ 这样一些函数，其收敛横坐标为 $-\sigma$ 。但是，对于那些比指数函数增加得更快的函数，不可能找到合适的收敛横坐标值。因此，像 $\mathrm{e}^{t^2}$ 和 $t \mathrm{e}^{t^2}$ 这类函数，不能进

行拉普拉斯变换。

应当指出，在物理上可以实现的信号，总是可以进行拉普拉斯变换的。

# 9.5 互联系统

在分析非线性动力学系统的稳定性时,分析的复杂性随着系统阶数的增加而迅速增加,这就促使我们寻找能简化分析的方法。如果能按照低阶子系统的互联建立系统模型,则可分两步进行稳定性分析。第一步是将系统分解成更小的孤立子系统,并分析每个子系统的稳定性,而不考虑它们之间的连接;第二步,合并第一步得到的结果,得出互联系统的稳定性。在这一节中将说明如何通过寻找互联系统的李雅普诺夫函数来实现上述构想。

考虑互联系统 $\dot{x}_{i}=f_{i}(t,x_{i})+g_{i}(t,x),\quad i=1,2,\cdots,m$ (9.32)

其中， $x_{i}\in R^{n_{i}},n_{1}+\cdots+n_{m}=n,x=\left[x_{1}^{\mathrm{T}},\cdots,x_{m}^{\mathrm{T}}\right]^{\mathrm{T}}$ 。假设 $f_{i}$ 和 $g_{i}$ 足够光滑，保证在所感兴趣的定义域内对于所有初始条件解是局部存在的和唯一的，且有

$$f _ {i} (t, 0) = 0, \quad g _ {i} (t, 0) = 0, \quad \forall i$$

使原点 $x = 0$ 是系统的一个平衡点。忽略互联项 $g_{i}$ ，系统分解成 $m$ 个孤立子系统：

$$\dot {x} _ {i} = f _ {i} (t, x _ {i}) \tag {9.33}$$

其中每个子系统都在其原点 $x_{i} = 0$ 有一个平衡点。首先对于每个孤立子系统，寻找建立使其原点一致渐近稳定的李雅普诺夫函数。假设对于每个孤立子系统，我们能成功地找到一个正定递减的李雅普诺夫函数 $V_{i}(t,x_{i})$ ，沿其孤立子系统(9.33)轨线的导数是负定的，则函数

$$V (t, x) = \sum_ {i = 1} ^ {m} d _ {i} V _ {i} (t, x _ {i}), d _ {i} > 0$$

对正常数 $d_{i}$ 所有取值是 $m$ 个孤立子系统的复合李雅普诺夫函数。如果把互联系统(9.32)看成孤立子系统(9.33)的一个扰动，就有理由把 $V(t,x)$ 看成系统(9.32)的一个备选李雅普诺夫函数。 $V(t,x)$ 沿系统(9.32)轨线的导数由下式给出：

$$\dot {V} (t, x) = \sum_ {i = 1} ^ {m} d _ {i} \left[ \frac {\partial V _ {i}}{\partial t} + \frac {\partial V _ {i}}{\partial x _ {i}} f _ {i} (t, x _ {i}) \right] + \sum_ {i = 1} ^ {m} d _ {i} \frac {\partial V _ {i}}{\partial x _ {i}} g _ {i} (t, x)$$

由于 $V_{i}$ 是第 i 个孤立子系统的李雅普诺夫函数, 所以方程右边的第一项是负定的, 但一般来说第二项是不定的, 这种情况与 9.1 节中研究的扰动系统相似。因此, 可以对这个问题进行最坏情况分析, 这里 $\left[\partial V_{i}/\partial x_{i}\right]g_{i}$ 有界, 为一个非负上界。现在用 9.1 节介绍的二次型李雅普诺夫函数说明这一思想。假设对于 $i=1,2,\cdots,m, V_{i}(t,x_{i})$ 对于所有 $t\geqslant0$ 和 $\|x\|<r$ , 满足

$$\frac {\partial V _ {i}}{\partial t} + \frac {\partial V _ {i}}{\partial x _ {i}} f _ {i} (t, x _ {i}) \leqslant - \alpha_ {i} \phi_ {i} ^ {2} \left(x _ {i}\right) \tag {9.34}\left\| \frac {\partial V _ {i}}{\partial x _ {i}} \right\| \leqslant \beta_ {i} \phi_ {i} (x _ {i}) \tag {9.35}$$

其中， $\alpha_{i}$ 和 $\beta_{i}$ 为正常数， $\phi_{i}: R^{n_{i}} \to R$ 是正定且连续的。进一步假设对于所有 $t \geqslant 0$ 和 $\|x\| < r$ ，互联项 $g_{i}(t, x)$ 满足边界

$$\left\| g _ {i} (t, x) \right\| \leqslant \sum_ {j = 1} ^ {m} \gamma_ {i j} \phi_ {j} \left(x _ {j}\right) \tag {9.36}$$

$\gamma_{ij}$ 为非负常数。这样， $V(t,x) = \sum_{i = 1}^{m}d_{i}V_{i}(t,x_{i})$ 沿互联系统(9.32)轨线的导数满足不等式

$$\dot {V} (t, x) \leqslant \sum_ {i = 1} ^ {m} d _ {i} \left[ - \alpha_ {i} \phi_ {i} ^ {2} (x _ {i}) + \sum_ {j = 1} ^ {m} \beta_ {i} \gamma_ {i j} \phi_ {i} (x _ {i}) \phi_ {j} (x _ {j}) \right]$$

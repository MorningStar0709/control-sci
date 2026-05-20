# 7.2 间接法

（一）边界迭代法 这个方法的特点是逐步改善对缺少的初始条件

的估计,以满足规定的边界条件。它的原理如下。

利用哈密顿函数 $H$ 取极小的方法

$$\frac {\partial H (\boldsymbol {X} , \boldsymbol {U} , \boldsymbol {\lambda} , t)}{\partial \boldsymbol {U}} = \mathbf {0}$$

可解出 $U$ ，将它表示为 $\pmb{X}$ 和 $\pmb{\lambda}$ 的函数，即

$$\boldsymbol {U} = \boldsymbol {U} (\boldsymbol {X}, \boldsymbol {\lambda}, t) \tag {7-64}$$

将所求得的 $U = U(X, \lambda, t)$ 代入正则方程 (7-1)，消去正则方程中的 U。
再引入增广状态 $Y(t) \in \mathbb{R}^{2n}$

$$
\boldsymbol {Y} (t) \triangleq \left[ \begin{array}{l} \boldsymbol {X} (t) \\ \boldsymbol {\lambda} (t) \end{array} \right] \tag {7-65}
$$

则正则方程(7-1)可写成

$$\dot {\boldsymbol {Y}} = \boldsymbol {g} (\boldsymbol {Y}, t) \tag {7-66}$$

g 一般是非线性向量函数。设式(7-65)有 n 个已知初始条件 $X(t_{0}) = X_{0}$ ，n 个终端条件已知，设为 $x_{i}(t_{\mathrm{f}})(i=1,\cdots,q)$ 和 $\lambda_{i}(t_{\mathrm{f}})(i=q+1,\cdots,n)$ ，这是混合式的两点边值条件（参见例3-6），用边界迭代法也很易处理。定义

$$\mathbf {Z} (t) \triangleq \left[ x _ {1} (t), \dots , x _ {q} (t), \lambda_ {q + 1} (t), \dots , \lambda_ {n} (t) \right] ^ {\mathrm{T}} \tag {7-67}$$

显然， $Z(t_{\mathrm{f}})$ 是已知的，设 $\mathbf{Z}(t_{\mathrm{f}}) = \mathbf{Z}_{\mathrm{f}}$ 。

设由 $X(t_{0})$ 、 $\lambda(t_{0})$ 出发积分正则方程(7-66)，求得解 $Y(t)$ ，从中抽出 n 个分量构成 $Z(t)$ 。显然 $Z(t_{\mathrm{f}})$ 的值将随 $\lambda(t_{0})$ 而变，记成

$$\boldsymbol {Z} \left(t _ {\mathrm{f}}\right) = \boldsymbol {\Psi} \left[ \boldsymbol {\lambda} \left(t _ {0}\right) \right] \tag {7-68}$$

因 $\pmb{\lambda}(t_0)$ 未知，用一个估计值 $\hat{\pmb{\lambda}}(t_0)$ 得到的解为

$$\hat {\mathbf {Z}} \left(t _ {\mathrm{f}}\right) = \Psi \left[ \hat {\lambda} \left(t _ {0}\right) \right] \tag {7-69}$$

因 $\hat{\pmb{\lambda}}(t_0)$ 估计得不一定准确，故 $\hat{\pmb{Z}}(t_{\mathrm{f}})$ 一般不等于给定值 $\mathbf{Z}_{\mathrm{f}}$ 。

将式(7-68)在 $\boldsymbol{\lambda}(t_{0})=\hat{\boldsymbol{\lambda}}(t_{0})$ 处展开为泰勒级数，保留一次项，得

$$\boldsymbol {Z} \left(t _ {\mathrm{f}}\right) = \boldsymbol {\Psi} \left[ \hat {\boldsymbol {\lambda}} \left(t _ {0}\right) \right] + \frac {\partial \boldsymbol {\Psi}}{\partial \boldsymbol {\lambda} ^ {\mathrm{T}} \left(t _ {0}\right)} \left[ \boldsymbol {\lambda} \left(t _ {0}\right) - \hat {\boldsymbol {\lambda}} \left(t _ {0}\right) \right] \tag {7-70}$$

其中， $\frac{\partial \Psi}{\partial \pmb{\lambda}^{\mathrm{T}}}$ 是 $n \times n$ 维矩阵，称为敏感矩阵或转移矩阵。

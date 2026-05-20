如果线性向量微分方程 (2.3.2) 的 $n$ 个解 $\varphi_1(t), \varphi_2(t), \cdots, \varphi_n(t)$ 在 $(r_1, r_2)$ 内线性独立，则称之为方程 (2.3.2) 的一个基本解组.

由基本解组构成的矩阵 $\left[\varphi_{1}(t),\varphi_{2}(t),\cdots,\varphi_{n}(t)\right]$ 称为微分方程 (2.3.2) 的一个基本解矩阵。显然，微分方程 (2.3.2) 的基本解矩阵是满秩阵。

注意矩阵值函数 $\Phi(t; t_0)$ 是微分方程 (2.3.2) 的一个基本解矩阵。利用微分方程 (2.3.2) 的初值问题解的唯一性容易证明，对于任一 $n \times n$ 非降秩阵 $K$ ，线性矩阵微分方程的初值问题

$$
\left\{ \begin{array}{l} \dot {\Psi} (t) = A (t) \Psi (t), \\ \Psi (t _ {0}) = K \end{array} \right. \tag {2.3.8}
$$

的解 $\Psi(t; t_0)$ 就是微分方程 (2.3.2) 的一个基本解矩阵. 容易看出基本解矩阵 $\Psi(t; t_0)$ 和 $\Phi(t; t_0)$ 之间存在有线性关系式

$$\varPsi (t; t _ {0}) = \Phi (t; t _ {0}) K.$$

设 $W(t)=[w_{1}(t),w_{2}(t),\cdots,w_{n}(t)]$ 是由微分方程 (2.3.2) 的定义在区间 $(r_{1},r_{2})$ 内的 n 个解组成的方阵. 解方阵的行列式 $\det W(t)$ 称为解组 $w_{1}(t),w_{2}(t),\cdots,w_{n}(t)$ 的 Wronsky 行列式.

命题 2.3.2 $^{[12]}$ 对于方程 (2.3.2) 的解方阵 $W(t)$ ，有如下的 Liouville 公式：

$$\det \boldsymbol {W} (t) = \det \boldsymbol {W} \left(t _ {0}\right) \exp \left\{\int_ {t _ {0}} ^ {t} \sum_ {i = 1} ^ {n} a _ {i i} (s) \mathrm{d} s \right\}. \tag {2.3.9}$$

显然，以任意非降秩阵 K 为初始值的基本解阵 $\Psi(t;t_{0})$ 的 Liouville 公式为

$$\det \Psi (t; t _ {0}) = \det K \exp \left\{\int_ {t _ {0}} ^ {t} \sum_ {i = 1} ^ {n} a _ {i i} (s) \mathrm{d} s \right\}.$$

考虑线性非齐次向量微分方程 (2.3.1) 的解. 令 $(t_0, x_0)$ 是区域 $\pi$ 内任一固定点. 微分方程 (2.3.1) 的以 $(t_0, x_0)$ 为初值的解记为 $\varphi(t; t_0, x_0)$ . 利用 Picard 逐步逼近法, 不难求得 $\varphi(t; t_0, x_0)$ 的表示式为

$$\varphi (t; t _ {0}, x _ {0}) = \Phi (t; t _ {0}) x _ {0} + \int_ {t _ {0}} ^ {t} \Phi (t; s) b (s) \mathrm{d} s. \tag {2.3.10}$$

下面讨论线性常系数非齐次微分方程

$$\frac {\mathrm{d} x}{\mathrm{d} t} = A x + b \tag {2.3.11}$$

和线性定常齐次微分方程

$$\frac {\mathrm{d} x}{\mathrm{d} t} = A x. \tag {2.3.12}$$

从式 (2.3.4) 容易看到，线性定常微分方程的状态转移阵 $\Phi(t; t_0)$ 可以表示成

$$\Phi (t; t _ {0}) = \mathrm{e} ^ {\boldsymbol {A} (t - t _ {0})}.$$

我们有Taylor展开

$$\mathrm{e} ^ {\boldsymbol {A} (t - t _ {0})} = \boldsymbol {I} _ {n} + \frac {\boldsymbol {A}}{1 !} (t - t _ {0}) + \frac {\boldsymbol {A} ^ {2}}{2 !} (t - t _ {0}) ^ {2} + \dots , \tag {2.3.13}$$

这样，在定常情况下线性齐次向量微分方程的状态转移阵为 $\Phi(t;0) = \mathrm{e}^{At}$ .

因此微分方程 (2.3.11) 以 $x_0$ 为初值的解 $x(t; t_0, x_0)$ 为

$$\boldsymbol {x} (t; t _ {0}, \boldsymbol {x} _ {0}) = \mathrm{e} ^ {\boldsymbol {A} (t - t _ {0})} \boldsymbol {x} _ {0} + \int_ {t _ {0}} ^ {t} \mathrm{e} ^ {\boldsymbol {A} (t - s)} \boldsymbol {b} \mathrm{d} s, \quad t \in (- \infty , \infty). \tag {2.3.14}$$

# 数学期望、特征函数

在概率空间上可定义积分. 设 $\xi$ 为非负随机变量, 完全和式 (4.1.1) 类似地, 记

$$A _ {n i} \stackrel {\text { def }} {=} \{\omega : i 2 ^ {- n} \leqslant \xi < (i + 1) 2 ^ {- n} \}, \quad i = 0, 1, \dots , n 2 ^ {n} - 1.$$

由于 $\xi$ 是随机变量，所以 $A_{ni} \in \mathcal{F}$ . 定义

$$E \xi = \int_ {\Omega} \xi \mathrm{d} P \stackrel {\mathrm{def}} {=} \lim _ {n \rightarrow \infty} \left[ \sum_ {i = 0} ^ {n 2 ^ {n} - 1} i 2 ^ {- n} P (A _ {n i}) + n P (\xi \geqslant 1) \right], \tag {4.1.7}$$

这个极限可能无穷，叫 $\xi$ 的数学期望，或期望.

当 $\xi$ 不一定非负时，定义

$$\xi^ {+} \stackrel {\text { def }} {=} \max (\xi , 0), \quad \xi^ {-} \stackrel {\text { def }} {=} \max (- \xi , 0).$$

当 $E\xi^+$ 和 $E\xi^{-}$ 不同时为零时，则 $\xi$ 的期望定义为

$$E \xi \stackrel {\text { def }} {=} E \xi^ {+} - E \xi^ {-}.$$

注意到式 (4.1.7) 的右端可用 $\xi$ 的分布函数 $F_{\xi}(x)$ 来表达

$$\lim _ {n \rightarrow \infty} \left[ \sum_ {i = 0} ^ {n 2 ^ {n} - 1} i 2 ^ {- n} \big (F _ {\xi} ((i + 1) 2 ^ {- n}) - F _ {\xi} (i 2 ^ {- n}) \big) + n (1 - F _ {\xi} (n)) \right],$$

而上式正是Lebesgue-Stieltjes积分 $\int_{-\infty}^{\infty}x\mathrm{d}F_{\xi}(x)$ 的定义.

所以 $\xi$ 的期望可用分布函数来表达

$$E \xi = \int_ {- \infty} ^ {\infty} x \mathrm{d} F _ {\xi} (x).$$

当 $\xi$ 有密度 $f_{\xi}(\cdot)$ 时，则 $E\xi = \int_{-\infty}^{\infty}xf_{\xi}(x)\mathrm{d}x.$

当 $\xi$ 服从正态分布时，它的密度由(4.1.6)给出

$$
\begin{array}{l} E \xi = \frac {1}{(2 \pi) ^ {\frac {l}{2}} (\det R) ^ {\frac {1}{2}}} \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} \exp \left\{- \frac {1}{2} (x - \mu) ^ {\mathrm{T}} R ^ {- 1} (x - \mu) \right\} \\ \cdot \left[ \begin{array}{c} x ^ {1} \\ \vdots \\ x ^ {l} \end{array} \right] \mathrm{d} x ^ {1} \dots \mathrm{d} x ^ {l} = \mu , \tag {4.1.8} \\ \end{array}
$$

而

$$E (\xi - \mu) (\xi - \mu) ^ {\mathrm{T}} = R. \tag {4.1.9}$$

数学期望表示随机变量的加权平均，而 $E(\xi - \mu)^2$ 叫 $\xi$ 的方差，它表示随机变量的散布。当多维时， $E(\xi - \mu)(\xi - \mu)^{\mathrm{T}}$ 叫 $\xi$ 的协方差阵。

对随机变量 $\xi, E\xi = \mu, E\xi^k$ 叫它的 $k$ 阶矩，而 $E(\xi - \mu)^k$ 叫 $k$ 阶中心矩， $E|\xi|^k$ 叫 $k$ 阶绝对矩.

设随机变量 $\xi$ 的分布函数为 $F(\cdot), F(\cdot)$ 的Fourier-Stieltjes变换 $\phi(\lambda)$ 叫 $\xi$ 的特征函数：

$$\phi (\lambda) = E \mathrm{e} ^ {\mathrm{i} \lambda \xi} = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} \lambda x} \mathrm{d} F (x), \tag {4.1.10}$$

这里 i 是虚数单位，即 $i^{2} = -1$ .

特征函数有以下性质：

(1) $|\phi (\lambda)|\leqslant \phi (0) = 1;$   
(2) $\phi(\lambda)$ 对 $\lambda \in \mathbb{R}$ 一致连续；  
(3) $\phi (\lambda) = \overline{\phi} (-\lambda);$

(4) 若对某个 $n \geqslant 1$ 及 $\delta \in [0,1]$ , $E|\xi|^{n + \delta} < \infty$ , 则 $\phi(\lambda)$ 可 $n$ 次微分,

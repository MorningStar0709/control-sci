# 二次性能指标下的随机控制

我们讨论如下的线性随机系统：

$$x _ {k + 1} = \Phi_ {k + 1, k} x _ {k} + B _ {k} u _ {k} + D _ {k + 1} w _ {k + 1}, \tag {4.4.40}y _ {k} = C _ {k} x _ {k} + F _ {k} w _ {k}, \tag {4.4.41}$$

首先讨论系数阵 $\Phi_{k+1,k}, B_k, D_{k+1}, C_k, F_k$ 都是确定性阵，不依赖量测，也不要求 $\{w_k\}$ 正态，只设 $Ew_k = 0, Ew_k w_j^{\mathrm{T}} = \delta_{kj} I, \delta_{kj} = \begin{cases} 0, k \neq j \\ 1, k = j \end{cases}$ . 设 $x_0$ 和 $\{w_k\}$ 不相关， $Ex_0$ 和 $E(x_0 - Ex_0)(x_0 - Ex_0)^{\mathrm{T}} \stackrel{\mathrm{def}}{=} R$ 已知， $E \| y_0\|^2 < \infty$ .

设控制量 $u_{k}$ 是 r 维的，要求它是 $y_{0}, \cdots, y_{k}$ 的线性函数，也就是说，我们考虑线性反馈控制

$$u _ {k} = H _ {k} y ^ {k} + a _ {k}, \quad k = 0, 1, \dots , \tag {4.4.42}$$

$a_{k}$ 是 $r$ 维确定性向量， $H_{k}$ 是相应维数的确定性阵.

可以想像一个客观系统本身是非线性，但它和标称系统的偏差可接近线性。这样式(4.4.40)、(4.4.41)中的 $x_{k}$ 可看成这种偏差。所以很自然要求二次项尽可能小。这样，我们要设计控制(4.4.42)，使二次指标 $EJ(u)=\min$

$$J (u) = x _ {N} ^ {\mathrm{T}} Q _ {0} x _ {N} + \sum_ {k = 0} ^ {N - 1} \left(x _ {k} ^ {\mathrm{T}} Q _ {1} (k) x _ {k} + u _ {k} ^ {\mathrm{T}} Q _ {2} (k) u _ {k}\right), \tag {4.4.43}Q _ {0} \geqslant 0, \quad Q _ {1} (k) \geqslant 0, \quad Q _ {2} > 0, \quad k = 0, 1, \dots , N - 1.$$

对系统 (4.4.40), (4.4.41) 适用定理 4.4.1. 我们仍沿用那里的符号.

引理 4.4.7 记 $\xi_{k}\stackrel{\operatorname{def}}{=}x_{k}-\hat{x}_{k},\eta_{k}\stackrel{\operatorname{def}}{=}y_{k}-\hat{y}_{k}^{\prime}$ ，它们分别是滤波误差及量测预报误差。 $\xi_{k}$ 和 $y^{k}$ 不相关。 $\{\eta_{k}\}$ 为零均值互不相关的随机向量。

证明 把 $y$ 对应 $y^k, x$ 对应 $x_k$ , 用式 (4.4.4) 知

$$E (x _ {k} - \hat {x} _ {k}) (y ^ {k} - E y ^ {k}) ^ {*} = 0,$$

所以 $E(x_{k} - \hat{x}_{k})(y^{k})^{*} = 0$ ，也就是 $\xi_{k}$ 和 $y^{k}$ 不相关.

同理可知， $\eta_{k}$ 和 $y^{k-1}$ 不相关，但对任何 j, $\eta_{j}$ 是 $y_{0}, \cdots, y_{j-1}$ 的线性组合，所以 $\{\eta_{k}\}$ 互不相关.

引理4.4.8 设 $L_{k}$ 及 $M_{k}$ 是相应维数的确定性阵，则

$$
\begin{array}{l} E (u _ {k} + L _ {k} x _ {k}) ^ {*} M _ {k} (u _ {k} + L _ {k} x _ {k}) \\ = E (u _ {k} + L _ {k} \hat {x} _ {k}) ^ {*} M _ {k} (u _ {k} + L _ {k} \hat {x} _ {k}) + \operatorname{tr} L _ {k} P _ {k} L _ {k} ^ {*} M _ {k}. \\ \end{array}
$$

证明 由于 $u_{k}$ 及 $\hat{x}_k$ 都是 $y^{k}$ 的线性函数，据引理4.4.7,

$$E (x _ {k} - \hat {x} _ {k}) (u _ {k} + L _ {k} \hat {x} _ {k}) ^ {*} = 0.$$

所以

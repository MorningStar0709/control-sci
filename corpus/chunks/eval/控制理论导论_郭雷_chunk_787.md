# 时域乘子法

乘子法是偏微分方程理论中估计解的渐近行为的一种强有力的工具。在线性偏微分方程情形，通常选择形如 $ay + by_{t} + cy_{x}$ (高维情形 $y_{x}$ 代之以 $y_{x_i}$ 的线性组合)的乘子以构造一个正定二次型泛函，类似于常微分方程情形的Lyapunov泛函。设系统的能量是 $E(t)$ 。通常 $E(t) = \frac{1}{2} \| Y(t) \|_{\mathcal{H}}^{2}$ ，这里 $\|Y(t)\|_{\mathcal{H}}$ 表示系统解 $Y(t)$ 在状态空间 $\mathcal{H}$ 中的范数。因此，系统指数稳定等价于系统能量指数衰减。我们先给出一个一般的关于指数稳定的引理。

引理10.4.2 假定如下两个条件之一成立：(1) 设在所选择的乘子下，

$$E _ {\lambda} (t) = E (t) + G _ {\lambda} (t), \quad \frac {\mathrm{d}}{\mathrm{d} t} E _ {\lambda} (t) = - F _ {\lambda} (t), \quad t \geqslant 0,$$

其中 $\lambda$ 是待定正常数. 假定对于某个 $\lambda$ , 存在正常数 $\alpha_{1}, \alpha_{2}, \beta_{1}, \beta_{2}$ 使得

$$
\left\{ \begin{array}{l l} \alpha_ {1} E (t) \leqslant E _ {\lambda} (t) \leqslant \alpha_ {2} E (t), \\ \beta_ {1} E (t) \leqslant F _ {\lambda} (t) \leqslant \beta_ {2} E (t); \end{array} \right. \tag {10.4.19}
$$

(2) 设在所选择的乘子下

$$E _ {\varepsilon , \lambda} (t) = (1 - \varepsilon) t E (t) + G _ {\lambda} (t), \quad t \geqslant 0, \quad 0 < \varepsilon < 1, \lambda \in \mathbb {R}.$$

假定对于某个 $\lambda \in \mathbb{R}$ , 存在常数 $\mu > 0$ , 并且对于某个 $\varepsilon, 0 < \varepsilon < 1$ , 存在常数 $T_0 > 0$ , 使得

$$
\left\{ \begin{array}{l l} | G _ {\lambda} (t) | \leqslant \mu E (t), & \forall t \geqslant 0, \\ \dot {E} _ {\epsilon , \lambda} (t) \leqslant 0, & \forall t \geqslant T _ {0}. \end{array} \right. \tag {10.4.20}
$$

那么系统能量是指数衰减的，或者说，系统是指数稳定的。

证明 (1) 假设式 (10.4.19) 成立，则

$$\frac {\mathrm{d}}{\mathrm{d} t} E _ {\lambda} (t) \leqslant - \beta_ {1} E (t) \leqslant - \frac {\beta_ {1}}{\alpha_ {2}} E _ {\lambda} (t).$$

由此得到

$$\alpha_ {1} E (t) \leqslant E _ {\lambda} (t) \leqslant \mathrm{e} ^ {- \frac {\beta_ {1}}{\alpha_ {2}} t} E _ {\lambda} (0) \leqslant \alpha_ {2} \mathrm{e} ^ {- \frac {\beta_ {1}}{\alpha_ {2}} t} E (0).$$

这样，我们证明了

$$E (t) \leqslant \alpha_ {1} ^ {- 1} \alpha_ {2} \mathrm{e} ^ {- \frac {\beta_ {1}}{\alpha_ {2}} t} E (0), \quad t \geqslant 0.$$

(2) 假设式 (10.4.20) 成立，则

$$[ (1 - \varepsilon) t - \mu ] E (t) \leqslant E _ {\varepsilon , \lambda} (t) \leqslant [ (1 - \varepsilon) t + \mu ] E (t).$$

于是若令 $T_{1} = \max \{T_{0}, (1 - \varepsilon)^{-1}\mu\}$ ，则

$$E (t) \leqslant \frac {(1 - \varepsilon) T _ {0} + \mu}{(1 - \varepsilon) t - \mu} E (T _ {0}), \quad \forall t > T _ {1}.$$

这表明 $E(t) = O(t^{-1})$ 。因此系统是强 $L^4$ - 稳定的。根据定理 10.1.1，系统能量是指数衰减的。证毕。

注意这里 $E_{\lambda}(t)$ 和 $E_{\varepsilon, \lambda}(t)$ 是能量 $E(t)$ 的某种摄动，因此这一方法也叫做能量摄动法。寻找适当的乘子，在这里变成寻找合适的能量摄动泛函 $G_{\lambda}(t)$ 。

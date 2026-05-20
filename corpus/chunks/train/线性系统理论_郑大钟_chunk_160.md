其几何含义是，把 $\eta_{\min}$ 规定为状态空间中 $V(x) = 1$ 的超球面上的极小点处的标量 $\pmb{x}^T\pmb{Q}\pmb{x}$ 值。于是，在此基础上，就可导出如下的结论。

结论 对于线性定常系统(4.80)，设正定对称矩阵 $Q$ 和 $P$ 为已知，则成立：

$$\eta_ {\min} = \lambda_ {\min} (Q P ^ {- 1}) \tag {4.88}$$

其中 $\lambda_{\min}(\cdot)$ 表示 $(\cdot)$ 的最小特征值。

证 令 $\mu$ 为拉格朗日（Lagrange）乘子，则可把（4.87）等式右边所示的条件极值问题化为如下的无条件极值问题：

$$\min _ {\boldsymbol {x}} \left[ \boldsymbol {x} ^ {T} (Q - \mu P) \boldsymbol {x} \right] \tag {4.89}$$

且其所应满足的条件为：

$$\left. \left\{\frac {d \boldsymbol {x} ^ {T}}{d \boldsymbol {x}} (Q - \mu P) \boldsymbol {x} + \left[ \boldsymbol {x} ^ {T} (Q - \mu P) \frac {d \boldsymbol {x}}{d \boldsymbol {x} ^ {T}} \right] ^ {T} \right\} _ {\boldsymbol {x} = \boldsymbol {x} _ {\min}} = \mathbf {0} \right. \tag {4.90}$$

考虑到 $dx^{T}/dx = I$ ，所以上式可进而表为：

$$2 (Q - \mu P) x _ {\min} = 0 \tag {4.91}$$

注意到 $x_{\min} \neq 0$ ，故由上式又可导出

$$\det (Q - \mu P) = 0 \tag {4.92}$$

或将其表为如下形式

$$\det (\mu I - Q P ^ {- 1}) = 0 \tag {4.93}$$

于是，由 $\operatorname{det}(\mu I - QP^{-1}) = 0$ 即知， $\mu$ 就是 $QP^{-1}$ 的特征值，也即有

$$\mu = \lambda (Q P ^ {- 1}) \tag {4.94}$$

但是,根据(4.87),得到

$$\eta_ {\min} = \min _ {x} \left\{\boldsymbol {x} ^ {T} Q \boldsymbol {x}, \boldsymbol {x} ^ {T} P \boldsymbol {x} = 1 \right\} = \min _ {x} \left\{\boldsymbol {x} ^ {T} \mu P \boldsymbol {x}, \boldsymbol {x} ^ {T} P \boldsymbol {x} = 1 \right\} = \min [ \mu ] \tag {4.95}$$

利用（4.95）和（4.94）就可得到（4.88），从而证明完成。

# C. 19 证明定理 12.1

我们用9.6节的结果,把闭环系统(12.45)看成慢变系统进行分析。由于w在证明中不起作用,因此把 $g(\mathcal{X},\rho,w)$ 写为 $g(\mathcal{X},\rho)$ ,可以验证 $g(\mathcal{X},\rho)$ 在定义域 $D_{\mathcal{X}}\times D_{\rho}$ 上连续可微, $\mathcal{X}_{\mathrm{ss}}(\alpha)$

和 $A_{ms}(\alpha)$ 在 $D_{\rho}$ 上连续可微。因为对于所有 $\alpha \in D_{\rho}, A_{ms}(\alpha)$ 是赫尔维茨矩阵，所以对于所有 $\alpha \in S$ ( $D_{\rho}$ 的紧子集), $A_{ms}(\alpha)$ 对于 $\alpha$ 是一致赫尔维茨的。因此，对于 $\alpha \in S, A_{ms}$ 满足引理9.9中的所有假设。设 $P_{ms} = P_{ms}(\alpha)$ 是李雅普诺夫方程 $P_{ms}A_{ms} + A_{ms}^{\mathrm{T}}P_{ms} = -I$ 的解，以 $V(\mathcal{X}_{\delta}, \alpha) = \mathcal{X}_{\delta}^{\mathrm{T}}P_{ms}\mathcal{X}_{\delta}$ 作为冻结系统 $\dot{\mathcal{X}}_{\delta} = g(\mathcal{X}_{\delta} + \mathcal{X}_{\mathrm{ss}}(\alpha), \alpha)$ 的备选李雅普诺夫函数，引理9.9证明 $V(\mathcal{X}_{\delta}, \alpha)$ 满足式(9.41)、式(9.43)和式(9.44)，我们只需验证其满足式(9.42)。冻结系统可重写为

$$\dot {\mathcal {X}} _ {\delta} = A _ {m s} (\alpha) \mathcal {X} _ {\delta} + \Delta g (\mathcal {X} _ {\delta}, \alpha)$$

其中，在某个域 $\{\| \mathcal{X}_{\delta}\|_{2} < r_{1}\}$ 内

$$\| \Delta g (\mathcal {X} _ {\delta}, \alpha) \| _ {2} = \| g (\mathcal {X} _ {\delta} + \mathcal {X} _ {\mathrm{ss}} (\alpha), \alpha) - A _ {m s} (\alpha) \mathcal {X} _ {\delta} \| _ {2} \leqslant k _ {1} \| \mathcal {X} _ {\delta} \| _ {2} ^ {2}$$

这样，当 $\| \mathcal{X}_{\delta}\|_{2} < 1 / (4c_{2}k_{1})$ 时， $V$ 沿 $\dot{\mathcal{X}}_{\delta} = g(\mathcal{X}_{\delta} + \mathcal{X}_{\mathrm{ss}}(\alpha),\alpha)$ 轨线的导数满足

$$\dot {V} \leqslant - \| \mathcal {X} _ {\delta} \| _ {2} ^ {2} + 2 c _ {2} k _ {1} \| \mathcal {X} _ {\delta} \| _ {2} ^ {3} \leqslant - \frac {1}{2} \| \mathcal {X} _ {\delta} \| _ {2} ^ {2}$$

因此存在 $r > 0$ ，使得对于所有 $(\mathcal{X}_{\delta},\alpha)\in \{\| \mathcal{X}_{\delta}\|_{2} < r\} \times S,V(\mathcal{X}_{\delta},\alpha)$ 满足式(9.41）到式(9.44)。根据定理9.3即可证明定理12.1。

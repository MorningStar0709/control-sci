# C. 9 证明定理 4. 18

当 $\mu = 0$ 时，定理4.18即为定理4.9，因此该定理的证明借鉴了定理4.9的一些概念和名词。设 $\rho = \alpha_{1}(r)$ ，则 $\alpha_{2}(\mu) < \rho$ ，且 $\alpha_{2}(\| x(t_{0})\|) \leqslant \rho$ 。设 $\eta = \alpha_{2}(\mu)$ 并定义 $\Omega_{t,\eta} = \{x \in B_r | V(t,x) \leqslant \eta\}$ 和 $\Omega_{t,\rho} = \{x \in B_r | V(t,x) \leqslant \rho\}$ ，则

$$B _ {\mu} \subset \Omega_ {t, \eta} \subset \{\alpha_ {1} (\| x \|) \leqslant \eta \} \subset \{\alpha_ {1} (\| x \|) \leqslant \rho \} = B _ {r} \subset D$$

和 $\Omega_{t,\eta}\subset \Omega_{t,\rho}\subset B_r\subset D$

集合 $\Omega_{t,\eta}$ 和 $\Omega_{t,\rho}$ 具有始于这两个集合内的解不会离开该集合的性质，因为 $\dot{V}(t,x)$ 在边界上的值是负的。由

$$\alpha_ {2} (\| x (t _ {0}) \|) \leqslant \rho \Rightarrow x (t _ {0}) \in \Omega_ {t _ {0}, \rho}$$

可得对于所有 $t \geqslant t_0, x(t) \in \Omega_{t,\rho}$ 。始于 $\Omega_{t,\rho}$ 内的解在有限时间内一定会进入 $\Omega_{t,\eta}$ ，因为在集合 $\{\Omega_{t,\rho} - \Omega_{t,\eta}\}$ 上， $\dot{V}$ 满足

$$\dot {V} (t, x) \leqslant - k < 0$$

其中在包含 $\{\Omega_{t,\rho} - \Omega_{t,\eta}\}$ 的集合 $\{\mu \leqslant \| x\| \leqslant r\}$ 上， $k = \min \{W_3(x)\}$ 。上面的不等式表示

$$V (t, x (t)) \leqslant V (t _ {0}, x (t _ {0})) - k (t - t _ {0}) \leqslant \rho - k (t - t _ {0})$$

该式说明在时间区间 $[t_0, t_0 + (\rho - \eta) / k]$ 内 $V(t, x(t))$ 简化为 $\eta$ 。对于所有 $t \geqslant t_0$ ，始于 $\Omega_{t, \eta}$ 内的解都满足不等式(4.43)，因为 $\Omega_{t, \eta} \subset \{\alpha_1 (\|x\|) \leqslant \alpha_2(\mu)\}$ 。对于始于 $\Omega_{t, \rho}$ 内但在 $\Omega_{t, \eta}$ 外的解，设 $t_0 + T$ 是首次进入 $\Omega_{t, \eta}$ 的时刻。对于所有 $t \in [t_0, t_0 + T]$ ，

$$\dot {V} \leqslant - W _ {3} (x) \leqslant - \alpha_ {3} (\| x \|) \leqslant - \alpha_ {3} \left(\alpha_ {2} ^ {- 1} (V)\right) \stackrel {\mathrm{def}} {=} - \alpha (V)$$

其中 $\alpha_{3}$ 和 $\alpha$ 都是 $\mathcal{K}$ 类函数， $\alpha_{3}$ 的存在性是由引理4.3得出的。类似于定理4.9的证明，我们可证明存在一个 $\mathcal{KL}$ 类函数 $\sigma$ ，使得

$$V (t, x (t)) \leqslant \sigma (V (t _ {0}, x (t _ {0})), t - t _ {0}), \forall t \in [ t _ {0}, t _ {0} + T ]$$

定义 $\beta (r,s) = \alpha_1^{-1}(\sigma (\alpha_2(r),s))$ ，可得

$$\| x (t) \| \leqslant \beta (\| x (t _ {0}) \|, t - t _ {0}), \forall t \in [ t _ {0}, t _ {0} + T ]$$

如果 $D = R^n$ ，可选择 $\alpha_{3}$ 及 $\beta$ 与 $\rho$ 无关。如果 $\alpha_{1}$ 属于 $\mathcal{K}_{\infty}$ 类函数，则 $\alpha_{2}$ 也是 $\mathcal{K}_{\infty}$ 类函数，且可通过选取足够大的 $\rho$ ，使界 $\alpha_{2}^{-1}(\rho)$ 取得任意大，因此集合 $\{\| x\| \leqslant \alpha_2^{-1}(\rho)\}$ 内可包含任何初始状态 $x(t_0)$ 。

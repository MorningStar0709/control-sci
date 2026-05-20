根据 Perseval 恒等式，上述算子 $P_{+}M_{G}: L_{-}^{2} \to L_{+}^{2}$ 可以看做是 $H_{2}^{\perp} \to H_{2}$ 的算子，称为 Hankel 算子。对于此算子，我们有如下结论：

引理6.5.3 对于任意给定的 $G(s)$ , Hankel 算子 $P_{+}M_{G}:H_{2}^{\perp}\to H_{2}$ 满足

$$\sup _ {u \in B L _ {-} ^ {2}} \| P _ {+} y \| _ {2} ^ {2} = \sup _ {u \in B H _ {2} ^ {\perp}} \| P _ {+} M _ {G} u \| _ {2} ^ {2} = \rho (L _ {o} L _ {c}), \tag {6.5.7}$$

其中 $\rho (\cdot)$ 表示最大特征值， $L_{c}$ 和 $L_{o}$ 分别是满足如下Lyapunov方程的正定阵：

$$
\left\{ \begin{array}{l} A L _ {c} + L _ {c} A ^ {\mathrm{T}} = - B B ^ {\mathrm{T}}, \\ A ^ {\mathrm{T}} L _ {o} + L _ {o} A = - C ^ {\mathrm{T}} C. \end{array} \right. \tag {6.5.8}
$$

证明 由于 $(A, B)$ 是能控的，所以 $L_{c}$ 是非奇异阵，且对于任意给定的 $x_{0}$ ，存在 $u \in L_{-}^{2}$ 使得 $x(0) = x_{0}, x(-\infty) = 0$ 。利用方程 (6.5.8) 不难验证

$$\frac {\mathrm{d}}{\mathrm{d} t} (x ^ {\mathrm{T}} L _ {c} ^ {- 1} x) = \| u \| ^ {2} - \| u - B ^ {\mathrm{T}} L _ {c} ^ {- 1} x \| ^ {2},$$

其中 $\| u\|^2 = u^{\mathrm{T}}u$ ，于是对上式从 $t = -\infty$ 到 $t = 0$ 积分，并注意到 $x(-\infty) = 0,$ 得

$$x _ {0} ^ {\mathrm{T}} L _ {c} ^ {- 1} x _ {0} = | | u | | _ {2} ^ {2} - | | u - B ^ {\mathrm{T}} L _ {c} ^ {- 1} x | | _ {2} ^ {2} \leqslant | | u | | _ {2} ^ {2}. \tag {6.5.9}$$

令 $A_{c} = -(A + BB^{\mathrm{T}}L_{c}^{-1})$ ，则由方程(6.5.8)可知

$$L _ {c} ^ {- 1} A _ {c} + A _ {c} ^ {\mathrm{T}} L _ {c} ^ {- 1} = - L _ {c} ^ {- 1} B B ^ {\mathrm{T}} L _ {c} ^ {- 1},$$

即 $A_{c}$ 为稳定阵. 因此 $u = B^{\mathrm{T}}L_{c}^{-1}x(t) = B^{\mathrm{T}}L_{c}^{-1}\mathrm{e}^{-A_{\mathrm{c}}t}x_0 \in L_{2-}$ 时式 (6.5.9) 右端取等号. 故

$$\inf _ {u \in L ^ {2}} \left\{\| u \| _ {2} ^ {2} \mid x (0) = x _ {0} \right\} = x _ {0} ^ {\mathrm{T}} L _ {c} ^ {- 1} x _ {0}. \tag {6.5.10}$$

另一方面，当 $u(t) = 0, \forall t \geqslant 0$ 时， $G(s)$ 对初始条件 $x_0$ 的响应 $y = C\mathrm{e}^{At}x_0$ 满足

$$\left\| P _ {+} y \right\| _ {2} ^ {2} = \int_ {0} ^ {\infty} x _ {0} ^ {\mathrm{T}} \mathrm{e} ^ {A ^ {\mathrm{T}} t} C ^ {\mathrm{T}} C \mathrm{e} ^ {A t} x _ {0} \mathrm{d} t = x _ {0} ^ {\mathrm{T}} L _ {o} x _ {0}. \tag {6.5.11}$$

所以有

$$\sup _ {u \in B L _ {-} ^ {2}} \| P _ {+} y \| _ {2} ^ {2} = \sup _ {u \in L _ {-} ^ {2}} \frac {\| P _ {+} y \| _ {2} ^ {2}}{\| u \| _ {2} ^ {2}} = \max _ {x _ {0} \neq 0} \frac {x _ {0} ^ {\mathrm{T}} L _ {o} x _ {0}}{x _ {0} ^ {\mathrm{T}} L _ {c} ^ {- 1} x _ {0}}.$$

令 $L_{c}^{-1} = S^{\mathrm{T}}S, L_{o} = Q^{\mathrm{T}}Q, y_{0} = Sx_{0}$ 则

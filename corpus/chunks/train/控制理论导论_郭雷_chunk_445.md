$$
\begin{array}{l} T _ {1 1} (s) = C _ {F} \left(s I - A _ {F}\right) ^ {- 1} B _ {1}, \\ T _ {1 2} (s) = D _ {1 2} + C _ {F} \left(s I - A _ {F}\right) ^ {- 1} B _ {2}, \\ T _ {2 1} (s) = - D _ {2 1}, \\ T _ {2 2} (s) = 0. \\ \end{array}
$$

于是由 $w$ 至 $z$ 的闭环传递函数阵 $T_{zw}(s)$ 为

$$T _ {z w} (s) = T _ {1 1} (s) - T _ {1 2} Q _ {d} (s), \tag {6.4.30}$$

其中 $Q_{d}(s) = Q(s)D_{21}\in RH_{\infty}^{r\times q}$ 可以证明，如果 $\pmb{F}$ 是用Riccati方程(6.4.27）的半正定解 $P$ 构造的，那么根据式(6.4.27）和假设条件(A2)，有

$$P A _ {F} + A _ {F} ^ {\mathrm{T}} P + C _ {F} ^ {\mathrm{T}} C _ {F} = 0, \quad D _ {1 2} ^ {\mathrm{T}} C _ {F} + B _ {2} ^ {\mathrm{T}} P = 0, \tag {6.4.31}$$

故由引理6.4.2, $T_{12}(s)$ 是内函数阵，从而满足 $T_{12}^{\mathrm{T}}(-s)T_{12}(s) = I.$

令

$$
U (s) = \left[ \begin{array}{c} T _ {1 2} ^ {\mathrm{T}} (- s) \\ I - T _ {1 2} (s) T _ {1 2} ^ {\mathrm{T}} (- s) \end{array} \right],
$$

则 $U^{\mathbf{T}}(-s)U(s) = I$ ，所以

$$\left\| U (\cdot) T _ {z w} (\cdot) \right\| _ {\infty} = \left\| T _ {z w} (\cdot) \right\| _ {\infty} < 1. \tag {6.4.32}$$

根据定义，有

$$
\| U (\cdot) T _ {z w} (\cdot) \| _ {\infty} = \left\| \left[ \begin{array}{c} V (\cdot) \\ S (\cdot) \end{array} \right] \right\| _ {\infty} = \left\| \left[ \begin{array}{c} T _ {1 2} ^ {\mathrm{T}} (\cdot) T _ {1 1} (\cdot) - Q _ {d} (\cdot) \\ [ I - T _ {1 2} (\cdot) T _ {1 2} ^ {\mathrm{T}} (- \cdot) ] T _ {1 1} (\cdot) \end{array} \right] \right\| _ {\infty},
$$

于是

$$\| S (\cdot) \| _ {\infty} = \left\| \left[ I - T _ {1 2} (\cdot) T _ {1 2} ^ {\mathrm{T}} (- \cdot) \right] T _ {1 1} (\cdot) \right\| _ {\infty} < 1. \tag {6.4.33}$$

定义 $J(s) = I - S^{\mathrm{T}}(-s)S(s)$ ，则可以证明 $J(s)$ 能够表示为

$$J (s) = I + G _ {0} (s) + G _ {0} ^ {\mathrm{T}} (- s), \tag {6.4.34}$$

其中

$$G _ {0} (s) = - B _ {1} ^ {\mathrm{T}} P \left(s I - A _ {F}\right) ^ {- 1} Z B _ {1}, \quad Z = I - Y P,$$

而 $Y$ 是满足如下 Lyapunov 方程的半正定阵:

$$Y A _ {F} ^ {\mathrm{T}} + A _ {F} Y = - B _ {2} B _ {2} ^ {\mathrm{T}}. \tag {6.4.35}$$

注意到式 (6.4.33), 有

$$J (\mathrm{j} \omega) = I - S ^ {\mathrm{T}} (- \mathrm{j} \omega) S (\mathrm{j} \omega) > 0, \quad \forall \omega \in \mathbb {R}.$$

所以根据定理6.4.4, $J(s)$ 存在谱因子 $S_0(s)$ 满足

$$J (s) = S _ {0} ^ {\mathrm{T}} (- s) S _ {0} (s).$$

又根据式 (6.4.32), 有

$$I - S ^ {\mathrm{T}} (- \mathrm{j} \omega) S (\mathrm{j} \omega) - V ^ {\mathrm{T}} (- \mathrm{j} \omega) V (\mathrm{j} \omega) = S _ {0} ^ {\mathrm{T}} (- s) S _ {0} (s) - V ^ {\mathrm{T}} (- \mathrm{j} \omega) V (\mathrm{j} \omega) > 0, \forall \omega \in \mathbb {R},$$

因此

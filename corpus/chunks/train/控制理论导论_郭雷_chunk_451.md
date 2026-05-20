$$
\begin{array}{l} \sup _ {u \in B L _ {-} ^ {2}} \| P _ {+} y \| _ {2} ^ {2} = \max _ {y _ {0} \neq 0} \frac {y _ {0} ^ {\mathrm{T}} S ^ {- T} Q ^ {\mathrm{T}} Q S ^ {- 1} y _ {0}}{y _ {0} ^ {\mathrm{T}} y _ {0}} = \rho (S ^ {- T} Q ^ {\mathrm{T}} Q S ^ {- 1}) \\ = \rho (Q ^ {\mathrm{T}} Q S ^ {- 1} S ^ {- T}) = \rho (L _ {o} L _ {c}). \\ \end{array}
$$

最后，我们来讨论一个混合算子．考虑如下信号空间：

$$
\mathcal {U} \stackrel {\text { def }} {=} \left\{u = \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right] \mid u _ {1} \in H _ {2} ^ {\perp}, u _ {2} \in L ^ {2} \right\}, \tag {6.5.12}
$$

其中 $u_{1}$ 和 $u_{2}$ 分别为适当维的向量函数。考虑一适当的有理函数阵 $G(s) = [G_1(s)G_2(s)]$ ，其中 $G_{1}$ 和 $G_{2}$ 是行数相同且列数分别与 $u_{1}$ 和 $u_{2}$ 的维数匹配的有理函数阵。

定义 6.5.3 对于给定的 $G(s) = [G_{1}(s) G_{2}(s)]$ , Hankel-Toeplitz 算子 $\Gamma: U \to H_{2}$ 定义为

$$
y = \Gamma u = \Gamma \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right] = P _ {+} [ G _ {1} G _ {2} ] \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right] = P _ {+} (G _ {1} (s) u _ {1} + G _ {2} (s) u _ {2}). \tag {6.5.13}
$$

引理6.5.4 设 $G(s) = [G_1(s)G_2(s)]$ 的状态空间实现为

$$
\left\{ \begin{array}{l} \dot {x} = A x + B u, \\ y = C x, \end{array} \right. \tag {6.5.14}
$$

其中 $B = [B_{1}, B_{2}]$ 且 $(A, B)$ 是能控的，则

$$\sup _ {u \in B U} \| \Gamma u \| _ {2} < 1. \tag {6.5.15}$$

当且仅当如下条件成立：

(1) 如下 Riccati 方程有半正定解 $X$ ，且 $A + B_{2}B_{2}^{\mathrm{T}}X$ 是稳定阵

$$X A + A ^ {\mathrm{T}} X + X B _ {2} B _ {2} ^ {\mathrm{T}} X + C ^ {\mathrm{T}} C = 0;$$

(2) $\rho(XL_c) < 1$ , 其中 $L_{c}$ 是满足 $AL_{c} + L_{c}A^{\mathrm{T}} = -BB^{\mathrm{T}}$ 的正定阵, 且

$$B \mathcal {U} = \{u \in \mathcal {U} \mid \| u \| _ {2} = 1 \}.$$

证明 注意从不等式 (6.5.15) 可推出

$$\sup _ {u _ {2} \in B H _ {2}} \| P _ {+} G _ {2} u _ {2} \| _ {2} < 1,$$

从而有 $\| G_2(s)\|_{\infty} < 1$ 。所以根据定理6.2.1, 条件(1)是不等式(6.5.15)成立的必要条件。因此现在我们只需证明不等式(6.5.15)与条件(2)等价。

事实上根据 $\mathcal{U}$ 的定义，对于 $u\in \mathcal{U}$ ，有

$$\left\| P _ {+} y \right\| _ {2} ^ {2} - \left\| u \right\| _ {2} ^ {2} = \left\| P _ {+} y \right\| _ {2} ^ {2} - \left(\left\| P _ {+} u \right\| _ {2} ^ {2} + \left\| P _ {-} u \right\| _ {2} ^ {2}\right) \tag {6.5.16}= \| P _ {+} y \| _ {2} ^ {2} - \| P _ {+} u \| _ {2} ^ {2} - \| P _ {-} u \| _ {2} ^ {2}. \tag {6.5.17}$$

注意上式的最后一项只能通过 $x_0$ 来影响 $\| P_{+}y\| _2^2$ 的值，因此利用引理6.5.2及与其证明过程类似的讨论，可得

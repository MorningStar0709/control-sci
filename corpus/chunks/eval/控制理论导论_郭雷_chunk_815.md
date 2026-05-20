$$
\begin{array}{l} J (\widetilde {u}; t _ {0}, t _ {1}, x _ {0}) = J _ {1} \left(u ^ {0}; t, t _ {1}, x \left(t; u ^ {0}, x _ {0}\right)\right) + J \left(u ^ {1}; t, t _ {1}, x \left(t; u ^ {0}, x _ {0}\right)\right) \\ <   J _ {1} \left(u ^ {0}; t, t _ {1}, x \left(t; u ^ {0}, x _ {0}\right)\right) + J \left(u ^ {0}; t, t _ {1}, x \left(t; u ^ {0}, x _ {0}\right)\right) \\ = J \left(u ^ {0}; t _ {0}, t _ {1}, x _ {0}\right), \\ \end{array}
$$

其中

$$
\widetilde {u} \stackrel {\text { def }} {=} \left\{ \begin{array}{l l} u ^ {0} (s), & 0 \leqslant s \leqslant t, \\ u ^ {1} (s), & t <   s \leqslant t _ {1}, \end{array} \right.
$$

但这是不可能的，因为 $u^0$ 是最优控制.

定理 10.6.3 设 $x_{0} \in H$ ，则泛函 $J(\cdot; t_{0}, t_{1}, x_{0})$ 在唯一的点 $u^{0} \in L^{2}(t_{0}, t_{1}; U)$ 处达到其在 $L^{2}(t_{0}, t_{1}; U)$ 上的极小， $u_{0}$ 满足如下积分方程：

$$u ^ {0} (t) = - R ^ {- 1} B ^ {*} \left(\int_ {t} ^ {t _ {1}} T ^ {*} (s - t) Q x ^ {0} (s) \mathrm{d} s + T ^ {*} (t _ {1} - t) Q x ^ {0} (t _ {1})\right), \tag {10.6.12}$$

其中 $x^{0}(t)$ 是相应的最优轨线.

证明 定义线性算子 $\Lambda(t): L^2(t_0, t; U) \to H$ 如下:

$$\Lambda (t) u = \int_ {t _ {0}} ^ {t} T (t - s) B u (s) \mathrm{d} s.$$

于是

$$
\Lambda^ {*} (t) x = B ^ {*} T ^ {*} (t - s) x, \quad t _ {0} \leqslant s \leqslant t,
\begin{array}{l} J (u; t _ {0}, t _ {1}, x _ {0}) = \left(G x \left(t _ {1}\right), x \left(t _ {1}\right)\right) _ {H} + \int_ {t _ {0}} ^ {t _ {1}} \left[ \left(Q x (s), x (s)\right) _ {H} + \left(R u (s), u (s)\right) _ {U} \right] d s \\ = \left(G T \left(t _ {1} - t _ {0}\right) x _ {0}, T \left(t _ {1} - t _ {0}\right) x _ {0}\right) _ {H} + \int_ {t _ {0}} ^ {t _ {1}} \left(Q T (s - t _ {0})\right) x _ {0}, T \left(s - t _ {0}\right) x _ {0}) _ {H} d s \\ + 2 \left(u, \Lambda^ {*} (t _ {1}) G T (t _ {1} - t _ {0}) x _ {0}\right) _ {L ^ {2} \left(t _ {0}, t _ {1}; U\right)} + \int_ {t _ {0}} ^ {t _ {1}} \left(u, \Lambda^ {*} (s) Q \Lambda (s) u\right) _ {L ^ {2} \left(t _ {0}, s; U\right)} d s \\ + 2 \int_ {t _ {0}} ^ {t _ {1}} (u, \Lambda^ {*} (s) Q T (s - t _ {0}) x _ {0}) _ {L ^ {2} \left(t _ {0}, s; U\right)} d s \\ + (R u, u) _ {L ^ {2} \left(t _ {0}, t _ {1}; U\right)} + \left(u, \Lambda^ {*} \left(t _ {1}\right) G \Lambda \left(t _ {1}\right) u\right) _ {L ^ {2} \left(t _ {0}, t _ {1}; U\right)}. \\ \end{array}
$$

如果我们记

$$\alpha = \left(G T (t _ {1} - t _ {0}) x _ {0}, T (t _ {1} - t _ {0}) x _ {0}\right) + \int_ {t _ {0}} ^ {t _ {1}} \left(Q T (s - t _ {0}) x _ {0}, T (s - t _ {0}) x _ {0}\right) d s,$$

并分别定义线性算子 $\Gamma_1, \Gamma_2: L^2(t_0, t_1; U) \to L^2(t_0, t_1; U)$ , 和 $\Gamma_3, \Gamma_4: H \to L^2(t_0, t_1; U)$

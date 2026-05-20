# 指数镇定

现在我们讨论 Hilbert 空间 $H = X$ 和 $U$ 中系统 (10.3.1) 的能稳性。这里为了更确切和方便起见，我们用 $T^{A}(t)$ 表示由 $A$ 生成的 $C_{0}$ 半群。

定理10.3.1 (1) 如果系统(10.3.1)在某个区间 $[0, t_1]$ 上精确零能控, 则 $(A, B)$ 是指数能稳的;

(2) 如果 $A$ 生成一 $C_0$ 群 $T'(t)$ , 并且 $(A, B)$ 在某个区间 $[0, t_1]$ 上精确零能控, 则 $(A, B)$ 可按任意指定的衰减指数指数能稳.

证明 (1) 由于系统 (10.3.1) 在 $[0, t_1]$ 上精确零能控，故对任意 $x_0 \in H$ ，存在 $u \in L^2(0, t_1; U)$ 使得

$$0 = T (t _ {1}) x _ {0} + \int_ {0} ^ {t _ {1}} T (t _ {1} - s) B u (s) \mathrm{d} s.$$

现在我们对于 $s > t_1$ 定义 $u(s) = 0$ , 并令

$$x (t) = T (t) x _ {0} + \int_ {0} ^ {t _ {1}} T (t - s) B u (s) \mathrm{d} s, \quad \forall t \geqslant 0.$$

于是当 $t \geqslant t_1$ 时，

$$
\begin{array}{l} x (t) = T \left(t - t _ {1}\right) T \left(t _ {1}\right) x _ {0} + \int_ {0} ^ {t _ {1}} T \left(t - t _ {1}\right) T \left(t _ {1} - s\right) B u (s) d s \\ = T (t - t _ {1}) \left[ T (t _ {1}) x _ {0} + \int_ {0} ^ {t _ {1}} T (t _ {1} - s) B u (s) d s \right] = 0. \\ \end{array}
$$

因此 $u(\cdot) \in L^2(0, \infty; U)$ , 并且 $x(\cdot) \in L^2(0, \infty; H)$ . 这样, 根据推论 10.6.1 (其证明与这里的讨论是独立的), 存在一非负算子 $P \in \mathcal{L}(H)$ 使得 $A - BB^{*}P$ 生成一指数稳定的 $C_0$ 半群, 从而 $(A, B)$ 是指数能稳的;

(2) 首先注意，由于 $T(t)$ 是 $C_0$ 群，故 $(A, B)$ 在区间 $[0, t_1]$ 上精确零能控当且仅当 $(A, B)$ 在 $[0, t_1]$ 上精确能控。此外，注意到 $T(t)$ 对于所有 $t \in \mathbb{R}$ 都是有界可逆的，并且对于 $x \in H$ 和 $u \in L^2(0, t_1; U)$ ，

$$0 = T (t _ {1}) x + \int_ {0} ^ {t _ {1}} T (t _ {1} - s) B u (s) \mathrm{d} s$$

蕴含

$$0 = T (- t _ {1}) T (t _ {1}) x + \int_ {0} ^ {t _ {1}} T (- t _ {1} + s) B u (t _ {1} - s) \mathrm{d} s,$$

从而 $(-A, B)$ 在 $[0, t_1]$ 上也是精确能控的。于是若 $(A, B)$ 在 $[0, t_1]$ 上精确零能控，则根据定理10.2.1，存在 $\gamma > 0$ 使得

$$\int_ {0} ^ {t _ {1}} \| B ^ {*} T ^ {*} (- s) x \| _ {U} ^ {2} \mathrm{d} s \geqslant \gamma \| x \| ^ {2}, \quad \forall x \in H. \tag {10.3.2}$$

任给 $\omega > 0$ ，定义线性算子

$$P _ {\omega} x = \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- 2 \omega t} T (- t) B B ^ {*} T ^ {*} (- t) x \mathrm{d} t, \quad x \in H,$$

其中 $T(t)$ 是由 $A$ 生成的 $C_0$ 群. 于是 $P_{\omega} \in \mathcal{L}(H)$ 是对称的, 并且根据 (10.3.2), $P_{\omega}$ 有有界逆. 现在我们考虑控制系统

$$\dot {x} (t) = (A + \omega I) x (t) + B u (t). \tag {10.3.3}$$

将反馈控制 $u(t) = -B^{*}P_{\omega}^{-1}x(t)$ 代入(10.3.3)，可见 $(A + \omega I) - BB^{*}P_{\omega}^{-1}$ 是 $H$ 上某个 $C_0$ 群 $S(t)$ 的生成算子．记 $y(t) = S^{*}(t)y_{0}, y_{0} \in \mathcal{D}(A^{*})$ ，则

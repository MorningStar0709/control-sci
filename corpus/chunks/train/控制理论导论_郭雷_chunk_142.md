并记 $t_1 = \inf \{\widetilde{t} \mid \varphi(\widetilde{t}) \geqslant x(\widetilde{t})\}$ ，则存在适当小 $\varepsilon > 0$ ，使得

$$\varphi (t _ {1}) = x (t _ {1}), \quad \varphi (t) > x (t), \quad t \in (t _ {1}, t _ {1} + \varepsilon).$$

所以当 $t \in (t_1, t_1 + \varepsilon)$ 时有

$$\frac {\varphi (t) - \varphi (t _ {1})}{t - t _ {1}} > \frac {x (t) - x (t _ {1})}{t - t _ {1}}.$$

从而得

$$\overline {{{D}}} _ {+} \varphi (t _ {1}) \geqslant \dot {x} (t _ {1}) = f (t _ {1}, \varphi (t _ {1})),$$

与式 (2.2.12) 矛盾. 因此在条件 (2.2.12) 下, $\varphi(t) < x(t)$ 在 $(t_0, b)$ 上成立.

其次证明在条件 (2.2.10) 下必有 $\varphi(t) \leqslant \bar{x}(t), t \in [t_0, b)$ . 事实上, 如果存在 $\bar{t} \in [t_0, b)$ 使得 $\varphi(\bar{t}) > \bar{x}(\bar{t})$ , 则有 $\bar{\varepsilon}$ 和 $t_2$ , $0 < \varepsilon < b - t_2$ , 使得

$$\varphi (t _ {2}) = \bar {x} (t _ {2}), \quad \varphi (t) > \bar {x} (t), \quad t \in (t _ {2}, \bar {t} _ {2} + \bar {\varepsilon}).$$

引入辅助方程

$$\dot {x} = f (t, x) + \frac {1}{m}, \qquad m \text {为自然数}. \tag {2.2.13}$$

记式 (2.2.13) 过点 $(t_2, \varphi(t_2))$ 并在区间 $[t_2, t_2 + \delta]$ , $0 < \delta \leqslant \bar{\varepsilon}$ , 上定义的解为 $x_m(t)$ , 可以证明, 当 $t \in [t_2, t_2 + \delta]$ 时, 成立

$$\lim _ {m \rightarrow \infty} x _ {m} (t) = \bar {x} (t), \quad \varphi (t) > x _ {m} (t).$$

另一方面，由已证部分知，当 $t \in [t_2, t_2 + \delta]$ 时应有

$$\varphi (t) < x _ {m} (t),$$

导致矛盾. 因此在条件 (2.2.10) 下必有 $\varphi(t) \leqslant \bar{x}(t), t \in [t_0, b)$ . 同理可证, 当 $\underline{D}_+ \varphi(t) \geqslant f(t, \varphi(t))$ 时, 必有 $\varphi(t) \geqslant \underline{x}(t), t \in (a, t_0]$ .

用类似方法能够证明 (2) 中的结论.

推论2.2.2 设 $\varphi(t)$ 为定义在区间 $[a, b]$ 上的连续非负函数，且存在左、右导数 $\dot{\varphi}_{+}$ 、 $\dot{\varphi}_{-}$ 如果 $\varphi(t)$ 在 $[a, b]$ 上满足微分不等式

$$| \dot {\varphi} _ {\pm} (t) | \leqslant k \varphi (t) + h, \qquad k > 0, h > 0 (\text {常数}),$$

则对任意 $t_0 \in (a, b)$ ，当 $t \in [t_0, b)$ 时有

$$\widetilde {r} _ {0} \mathrm{e} ^ {- k (t - t _ {0})} + \frac {h}{k} (\mathrm{e} ^ {- k (t - t _ {0})} - 1) \leqslant \varphi (t) \leqslant r _ {0} \mathrm{e} ^ {k (t - t _ {0})} + \frac {h}{k} (\mathrm{e} ^ {k (t - t _ {0})} - 1),$$

而当 $t \in (a, t_0]$ 时有

$$\widetilde {r} _ {0} \mathrm{e} ^ {k (t - t _ {0})} + \frac {h}{k} (\mathrm{e} ^ {k (t - t _ {0})} - 1) \leqslant \varphi (t) \leqslant r _ {0} \mathrm{e} ^ {- k (t - t _ {0})} + \frac {h}{k} (\mathrm{e} ^ {- k (t - t _ {0})} - 1),$$

其中 $\widetilde{r}_0\leqslant \varphi (t_0)\leqslant r_0$ ，特别可取 $\widetilde{r}_0 = r_0 = \varphi (t_0).$

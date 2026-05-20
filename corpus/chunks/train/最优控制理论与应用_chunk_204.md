$$\boldsymbol {a} _ {\mathrm{p}} (t) = \boldsymbol {u} ^ {*} (t) = - \frac {\left(t _ {\mathrm{f}} - t\right) \left[ \tilde {\boldsymbol {x}} + \left(t _ {\mathrm{f}} - t\right) \tilde {\boldsymbol {v}} \right]}{c _ {\mathrm{p}} \left[ \frac {1}{k} + \frac {\left(c _ {\mathrm{e}} - c _ {\mathrm{p}}\right)}{3 c _ {\mathrm{p}} c _ {\mathrm{e}}} \left(t _ {\mathrm{f}} - t\right) ^ {3} \right]}\boldsymbol {a} _ {\mathrm{e}} (t) = \boldsymbol {v} ^ {*} (t) = - \frac {\left(t _ {\mathrm{f}} - t\right) \left[ \tilde {\boldsymbol {x}} + \left(t _ {\mathrm{f}} - t\right) \tilde {\boldsymbol {v}} \right]}{c _ {\mathrm{e}} \left[ \frac {1}{k} + \frac {\left(c _ {\mathrm{e}} - c _ {\mathrm{p}}\right)}{3 c _ {\mathrm{p}} c _ {\mathrm{e}}} \left(t _ {\mathrm{f}} - t\right) ^ {3} \right]} \tag {10-117}$$

下面讨论导弹(p方)的最优控制 $u^{*}(t)$ 。从性能指标式(10-111)可见，当 $k \to \infty$ 时，应有 $\| \widetilde{x}(t_{\mathrm{f}}) \|_2 = \| r_p(t_f) - r_e(t_f) \|_2 = 0$ ，即脱靶量为0。当 $k \to \infty$ 时，从式(10-117)得

$$\boldsymbol {u} ^ {*} (t) = - \frac {3 [ \tilde {\boldsymbol {x}} + (t _ {\mathrm{f}} - t) \tilde {\boldsymbol {v}} ]}{(1 - \frac {c _ {\mathrm{p}}}{c _ {\mathrm{e}}}) (t _ {\mathrm{f}} - t) ^ {2}} \tag {10-118}$$

式中， $t_{f}$ 取值不同将影响 $u^{*}(t)$ 。

若希望在 t 时刻的相对位置 $\tilde{\boldsymbol{x}}(t)$ 由于相对速度 $\tilde{\boldsymbol{v}}(t)$ 而逐渐变小，经过 $(t_{\mathrm{f}}-t)$ 后 $\tilde{x}$ 变为 0（零脱靶量），并假设 $\tilde{\boldsymbol{v}}(t)$ 为常数 $\tilde{\boldsymbol{v}}$ ，则有

$$\tilde {\boldsymbol {x}} (t) = - \tilde {\boldsymbol {v}} \left(t _ {\mathrm{f}} - t\right) \tag {10-119}$$

于是

$$\left(t _ {\mathrm{f}} - t\right) = - \frac {\tilde {\boldsymbol {x}} ^ {\mathrm{T}} \tilde {\boldsymbol {x}}}{\tilde {\boldsymbol {x}} ^ {\mathrm{T}} \tilde {\boldsymbol {v}}} = - \frac {\langle \tilde {\boldsymbol {x}} , \tilde {\boldsymbol {x}} \rangle}{\langle \tilde {\boldsymbol {x}} , \tilde {\boldsymbol {v}} \rangle} \tag {10-120}$$

将上式代入式(10-118)，得

$$\frac {\mathrm{d} \boldsymbol {K} ^ {- 1}}{\mathrm{d} t} = - \boldsymbol {K} ^ {- 1} \frac {\mathrm{d} \boldsymbol {K}}{\mathrm{d} t} \boldsymbol {K} ^ {- 1} = - \boldsymbol {K} ^ {- 1} \left[ \boldsymbol {K} \left(\boldsymbol {G} _ {\mathrm{p}} \boldsymbol {R} _ {\mathrm{p}} ^ {- 1} \boldsymbol {G} _ {\mathrm{p}} ^ {\mathrm{T}} - \boldsymbol {G} _ {\mathrm{e}} \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}}\right) \boldsymbol {K} \right] \boldsymbol {K} ^ {- 1}= - \left(\boldsymbol {G} _ {\mathrm{p}} \boldsymbol {R} _ {\mathrm{p}} ^ {- 1} \boldsymbol {G} _ {\mathrm{p}} ^ {\mathrm{T}} - \boldsymbol {G} _ {\mathrm{e}} \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}}\right)$$

将上式从 $t$ 到 $t_{\mathrm{f}}$ 积分，并注意 $\pmb {K}(t_{\mathrm{f}}) = \pmb{I}$ ，可得

$$\boldsymbol {K} ^ {- 1} \left(t _ {\mathrm{f}}\right) - \boldsymbol {K} ^ {- 1} (t) = - \int_ {t} ^ {t _ {\mathrm{f}}} \left[ \boldsymbol {G} _ {\mathrm{p}} (t) \boldsymbol {R} _ {\mathrm{p}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{p}} ^ {\mathrm{T}} (t) - \right.\left. \boldsymbol {G} _ {\mathrm{e}} (t) \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}} (t) \right] \mathrm{d} t$$

注意到 $K^{-1}(t_{\mathrm{f}}) = I$ ，于是有

$$\boldsymbol {K} (t) = \{\boldsymbol {I} + \int_ {t} ^ {t _ {\mathrm{f}}} [ \boldsymbol {G} _ {\mathrm{p}} (t) \boldsymbol {R} _ {\mathrm{p}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{p}} ^ {\mathrm{T}} (t) -\left. \boldsymbol {G} _ {\mathrm{e}} (t) \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}} (t) \right] \mathrm{d} t \} ^ {- 1} \tag {10-105}$$

上式即为 $K(t)$ 的解析解。

将(10-102)代入(10-101)，得

$$
\left\{ \begin{array}{l} \boldsymbol {u} ^ {*} (t) = - \boldsymbol {R} _ {\mathrm{p}} ^ {- 1} \boldsymbol {G} _ {\mathrm{p}} ^ {\mathrm{T}} \boldsymbol {K} (t) \boldsymbol {x} (t) \\ \boldsymbol {v} ^ {*} (t) = - \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}} \boldsymbol {K} (t) \boldsymbol {x} (t) \end{array} \right. \tag {10-106}
$$

这样， $u^{*}(t),v^{*}(t)$ 成为 $\pmb {x}(t)$ 的函数，即构成了一种反馈控制。

下面来验证 $\boldsymbol{u}^{*}(t)$ 、 $\boldsymbol{v}^{*}(t)$ 确实满足鞍点条件：

$$J (\boldsymbol {u} ^ {*}, \boldsymbol {v}) \leqslant J (\boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}) \leqslant J (\boldsymbol {u}, \boldsymbol {v} ^ {*})$$

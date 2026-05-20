$$\dot {\boldsymbol {\lambda}} ^ {T} (t) = (- \partial H / \partial \boldsymbol {x}) ^ {T} = - \boldsymbol {p} ^ {T} (t) - \boldsymbol {\lambda} ^ {T} (t) \boldsymbol {A} (t) \tag {10-63}$$

利用式 $(10-59)$ 、 $(10-62)$ 和 $(10-63)$ ，可得

$$
\begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} \left\{\boldsymbol {\lambda} ^ {\mathrm{T}} (t) [ \boldsymbol {x} (t) - \boldsymbol {x} ^ {*} (t) ] \right\} \\ = \dot {\boldsymbol {\lambda}} ^ {T} [ \boldsymbol {x} (t) - \boldsymbol {x} ^ {*} (t) ] + \boldsymbol {\lambda} ^ {T} (t) [ \dot {\boldsymbol {x}} (t) - \dot {\boldsymbol {x}} ^ {*} (t) ] \\ = \left[ - \boldsymbol {p} ^ {\mathrm{T}} (t) - \boldsymbol {\lambda} ^ {\mathrm{T}} (t) \boldsymbol {A} (t) \right] \left[ \boldsymbol {x} (t) - \boldsymbol {x} ^ {*} (t) \right] + \\ \boldsymbol {\lambda} ^ {T} (t) [ \boldsymbol {A} (t) \boldsymbol {x} (t) + f _ {1} (\boldsymbol {u}, t) + f _ {2} (\boldsymbol {v} ^ {*}, t) - \\ \boldsymbol {A} (t) \boldsymbol {x} ^ {*} (t) - f _ {1} (\boldsymbol {u} ^ {*}, t) - f _ {2} (\boldsymbol {v} ^ {*}, t) ] \\ = - \boldsymbol {p} ^ {\mathrm{T}} (t) \boldsymbol {x} (t) + \boldsymbol {p} ^ {\mathrm{T}} \boldsymbol {x} ^ {*} (t) + \\ \boldsymbol {\lambda} ^ {T} (t) f _ {1} (\boldsymbol {u}, t) - \boldsymbol {\lambda} ^ {T} (t) f _ {1} (\boldsymbol {u} ^ {*}, t) \\ \end{array}
$$

将上式从 $t_0$ 积分到 $t_\mathrm{f}$ ，且注意到 $\pmb{x}^{\star}(t_0) = \pmb{x}(t_0) = \pmb{x}_0$ 和 $\pmb{\lambda}^{\mathrm{T}}(t_{\mathrm{f}}) = \partial c^{\mathrm{T}}\pmb{x}(t_{\mathrm{f}}) / \partial \pmb{x}(t_{\mathrm{f}}) = \pmb{c}^{\mathrm{T}}$ ，可得

$$
\begin{array}{l} \boldsymbol {c} ^ {\mathrm{T}} \boldsymbol {x} (t _ {\mathrm{f}}) + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} [ \boldsymbol {p} ^ {\mathrm{T}} (t) \boldsymbol {x} (t) - \boldsymbol {\lambda} ^ {\mathrm{T}} (t) f _ {1} (\boldsymbol {u}, t) ] \mathrm{d} t \\ = \boldsymbol {c} ^ {\mathrm{T}} \boldsymbol {x} ^ {*} (t _ {\mathrm{f}}) + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} [ \boldsymbol {p} ^ {\mathrm{T}} (t) \boldsymbol {x} ^ {*} (t) - \boldsymbol {\lambda} ^ {\mathrm{T}} (t) f _ {1} (\boldsymbol {u} ^ {*}, t) ] \mathrm{d} t \\ \end{array}
$$

将上式左右积分号下同减 $\pmb{\lambda}^{\mathrm{T}}(t)[\pmb{A}(t)\pmb{x}^{*}(t) + f_{2}(\pmb{v}^{*},t)] - \pmb{p}^{\mathrm{T}}\pmb{x}^{*}(t)$ ，得
